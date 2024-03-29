extends Node
# 全局脚本，处理棋子和牌

var _cards_json_path = "res://config/pai.json"
# Called when the node enters the scene tree for the first time.
func _ready():
	_pre_read_cards(_cards_json_path)

func _pre_read_cards(path):
	var file = File.new()
	file.open(path, File.READ)
	card_details = parse_json(file.get_as_text())
	file.close()

# 获取牌的信息
var card_details
func read_card_detail(card_name):
	assert(card_details!=null)
	return card_details[card_name]
