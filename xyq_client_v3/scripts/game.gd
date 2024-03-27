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
var b_choose_piece = false
var b_choose_checkerboard = false

func _ready():
	b_my_turn = Global.mora_res
	_GameInit()

# 初始化棋盘
func _GameInit():
	var game_init_json_data = read("res://config/init_game_test.json")
	assert(game_init_json_data!=null)
	_setup_player_hands(game_init_json_data["data"]["pai"])
	
	var node = $CanvasLayer/main_qipan/Qipan/GridContainer
	for i in range(5):
		for j in range(5):
			var btn = checkerboard_scene.instance()
			btn.rect_min_size = Vector2(100, 100)
			btn.set_idx(j, i)
			btn.connect("confirm_cherkerboard", self, "_confirm_cherkerboard")
			node.add_child(btn)

	for item in game_init_json_data["data"]["pan"]["chess"]:
		var pos = item["pos"]
		var camp = item["camp"]
		var role = item["role"]
		_draw_piece(pos, camp, role)
	
	# 初始化完成
	b_game_init_complete = true

func _confirm_card(args):
	print(args)

func _confirm_piece(camp, x, y):
	if camp:
		print(x, y)

func _confirm_cherkerboard(arg1, arg2):
	print(arg1, arg2)

func _setup_player_hands(cards:Array): # arg - array for hand cards
	var pai = pai_scene.instance()
	pai.rotation_degrees = 180 # 需要旋转，原因不明。
	pai.init(cards[0])
	$CanvasLayer/myHand/left.add_child(pai)
	pai.connect("confirm_card", self, "_confirm_card")

	pai = pai_scene.instance()
	pai.init(cards[1])
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

func _end_turn():
	b_my_turn = false
	b_choose_card = false
	b_choose_piece = false
	b_choose_checkerboard = false

# game loop
func _process(delta):
	if !b_game_init_complete:
		return

	# TODO 轮询到回合没

	if b_my_turn:
		if b_choose_card && b_choose_piece:
			# TODO 高亮行动区域
			if b_choose_checkerboard:
				# TODO 下棋
				print("我下棋了")
				_end_turn()
		else:
			b_choose_checkerboard = false

