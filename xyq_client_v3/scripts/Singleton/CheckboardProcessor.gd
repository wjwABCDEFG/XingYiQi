extends Node2D
# 综合处理棋盘和棋盘格子

var _arr_checkboard_pieces = []
# var _pre_checkboard = null
var _checkboard_choice = null
var arr_aviable_piece = []

func add_piece(args):
	_arr_checkboard_pieces.append(args)

func clear_high_light():
	for item in _arr_checkboard_pieces:
		item.set_high_light(false)

func add_high_light(card_choice, piece_choice):
	arr_aviable_piece.clear()
	var arr = card_choice.viable_area_offset
	for v2 in arr:
		var x = v2.x + piece_choice.posX
		var y = v2.y + piece_choice.posY
		if(x >= 0 && x < 5 && y >= 0 && y < 5):
			_arr_checkboard_pieces[x * 5 + y].set_high_light(true)
			arr_aviable_piece.push_back(Vector2(x, y))

func check_aviable(i, j):
	for item in arr_aviable_piece:
		if i == item.x && j == item.y:
			return true
	return false

func choose_checkboard(i, j):
	if check_aviable(i, j):
		_checkboard_choice = Vector2(i, j)
		return true
	return false;

func get_cheakerboard():
	return _checkboard_choice
