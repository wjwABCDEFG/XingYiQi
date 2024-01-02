extends Node2D

export(PackedScene) var pai_scene

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

var game_init_complete = false
var is_my_turn = false

func _ready():
	is_my_turn = Global.mora_res
	_GameInit()

func _GameInit():
	# 初始化棋盘
	var game_init_json_data = read("res://config/init_game_test.json")
	assert(game_init_json_data!=null)
	_setup_player_hands(game_init_json_data["data"]["pai"])
	for item in game_init_json_data["data"]["pan"]["chess"]:
		var pos = item["pos"]
		var camp = item["camp"]
		var role = item["role"]
		_draw_chess(pos, camp, role)
	
	# 初始化完成
	game_init_complete = true

func _setup_player_hands(cards:Array): # arg - array for hand cards
	var pai = pai_scene.instance()
	pai.rotation_degrees = 180 # 需要旋转，原因不明。
	pai.init(cards[0])
	$CanvasLayer/myHand/left.add_child(pai)
	pai = pai_scene.instance()
	pai.init(cards[1])
	pai.rotation_degrees = 180
	$CanvasLayer/myHand/right.add_child(pai)
	# 先不给敌人手牌显示
	# pai = pai_scene.instance()
	# $CanvasLayer/yourHand/left.add_child(pai)
	# pai = pai_scene.instance()
	# $CanvasLayer/yourHand/right.add_child(pai)

func _draw_chess(pos:Array, camp:bool, role:int):
	var chess = Sprite.new()
	var node = $CanvasLayer/main_qipan/Qipan/lu
	if role:
		chess.texture = load("pic/bing.jpg")
	else:
		chess.texture = load("pic/wang.jpg")
	if !camp:
		chess.rotation_degrees = 180
	chess.position = Vector2(100*pos[1], 100*pos[0])
	node.add_child(chess)

func _process(delta):
	if game_init_complete:
		pass
	
