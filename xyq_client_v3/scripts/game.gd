extends Node2D

export(PackedScene) var pai_scene
export(PackedScene) var piece_scene
export(PackedScene) var checkerboard_scene

# 1.  *   对局开始：

#         *   初始化棋盘。
#         *   5张牌置于牌库，洗牌。
#         *   双方玩家从牌库抽取2张牌（随机）。剩下一张留置牌库。
#     *   猜拳环节：决定先后手。
#     *   玩家回合步骤：

#         *   挑选一张手牌。
#         *   选择要移动的棋子。
#         *   选择要移动的格子。
#         *   判断操作合法性。
#     *   判定：

#         *   判断是否吃子
#         *   若有，且吃掉对方玩家的王，对局结束，己方获胜。
#     *   回合结算：

#         *   将玩家使用的手牌置于牌库底部。
#         *   该回合玩家从牌库顶部抽取一张新的手牌。（补充至2张手牌）


# Called when the node enters the scene tree for the first time.


func read(path):
	var file = File.new()
	file.open(path, File.READ)
	var res = parse_json(file.get_as_text())
	file.close()
	return res

var b_game_init_complete = false
var b_my_turn = false
var b_choose_card = false
var card_choice = null
var b_choose_piece = false
var piece_choice = null
var b_choose_checkerboard = false
var mgr_checkboard = null
var map_playing_card = {}

func _ready():
	mgr_checkboard = CheckboardProcessor
	# b_my_turn = Global.mora_res
	b_my_turn = true
	_GameInit()

# 初始化棋盘
func _GameInit():
	var game_init_json_data = read("res://config/init_game_test.json")
	assert(game_init_json_data!=null)
	_setup_player_hands(game_init_json_data["data"]["pai"])
	
	var node = $CanvasLayer/main_qipan/Qipan/checkerboard
	for i in range(5):
		for j in range(5):
			var btn = checkerboard_scene.instance()
			btn.set_idx(i, j)
			btn.position = Vector2(100 * j, 100 * i)
			btn.connect("confirm_cherkerboard", self, "_confirm_cherkerboard")
			node.add_child(btn)
			mgr_checkboard.add_piece(btn)

	for item in game_init_json_data["data"]["pan"]["chess"]:
		var pos = item["pos"]
		var camp = item["camp"]
		var role = item["role"]
		_draw_piece(pos, camp, role)
	
	# 初始化完成
	b_game_init_complete = true

func _high_light_ckboard():
	mgr_checkboard.clear_high_light()
	# 根据card high light 格子
	assert(card_choice)
	mgr_checkboard.add_high_light(card_choice, piece_choice)

func _confirm_card(ins):
	if card_choice:
		card_choice.set_choice(false)
	b_choose_card = true
	card_choice = ins
	card_choice.set_choice(true)
	if b_choose_piece:
		_high_light_ckboard()

func _confirm_piece(ins):
	if piece_choice:
		piece_choice.set_choice(false)
	b_choose_piece = true
	piece_choice = ins
	piece_choice.set_choice(true)
	if b_choose_card:
		_high_light_ckboard()

func _confirm_cherkerboard(arg1, arg2):
	# VisualServer.material_set_param(arr_checkboard_mgr[arg1 * 5 + arg2].get_child(0).material, "visible", false) # 参数名对应的是shader中的命名， 这样会统一改掉同一个shader的材质。所以需要改成更换材质的做法。
	b_choose_checkerboard = mgr_checkboard.choose_checkboard(arg1, arg2)

func _setup_player_hands(cards:Array): # arg - array for hand cards
	var pai
	if map_playing_card.has(cards[0]):
		pai = map_playing_card[cards[0]]
	else:
		pai = pai_scene.instance()
		pai.init(cards[0])
		map_playing_card[cards[0]] = pai
	pai.rotation_degrees = 180 # 需要旋转，原因不明。
	$CanvasLayer/myHand/left.add_child(pai)
	pai.connect("confirm_card", self, "_confirm_card")

	if map_playing_card.has(cards[1]):
		pai = map_playing_card[cards[1]]
	else:
		pai = pai_scene.instance()
		pai.init(cards[1])
		map_playing_card[cards[1]] = pai
	pai.rotation_degrees = 180
	$CanvasLayer/myHand/right.add_child(pai)
	pai.connect("confirm_card", self, "_confirm_card")

func _draw_piece(pos:Array, camp:bool, role:int):
	var piece = piece_scene.instance()
	var node = $CanvasLayer/main_qipan/Qipan/lu
	if !camp:
		piece.rotation_degrees = 180
		if role:
			piece.set_texture( load("pic/blue_solider.png") )
		else:
			piece.set_texture( load("pic/blue_king.png") )
	else:
		if role:
			piece.set_texture( load("pic/red_solider.png") )
		else:
			piece.set_texture( load("pic/red_king.png") )
	piece.set_camp(camp)
	piece.set_pos(pos[0], pos[1])
	piece.position = Vector2(100 * pos[1], 100 * pos[0])
	piece.scale = Vector2.ONE * 0.8
	piece.connect("confirm_piece", self, "_confirm_piece")
	node.add_child(piece)

func _clear_card_choice():
	card_choice.set_choice(false)
	card_choice = null
	b_choose_card = false

func _clear_piece_choice():
	piece_choice.set_choice(false)
	piece_choice = null
	b_choose_piece = false

func _clear_piece_checkerboard():
	b_choose_checkerboard = false
	mgr_checkboard.clear_high_light()

func _end_turn():
	b_my_turn = false
	_clear_card_choice()
	_clear_piece_choice()
	_clear_piece_checkerboard()

# game loop
func _process(delta):
	if !b_game_init_complete:
		return

	# TODO 轮询到回合没

	if b_my_turn:
		if b_choose_card && b_choose_piece:
			if b_choose_checkerboard:
				print(CheckboardProcessor.get_cheakerboard())
				print(piece_choice.posX, piece_choice.posY)
				print(card_choice.begin_point)
				print("我下棋了")
				_end_turn()
		else:
			_clear_piece_checkerboard()

