extends Node2D

var _card_id

func init(card_name):
	_card_id = card_name
	var card_details = PieceProcessor.read_card_detail(card_name)
	_init_pai(card_details)

func _init_pai(arr):
	for j in arr.size():
		for i in arr[j].size():
			if arr[j][i] == 1:
				var can_move_point = Sprite.new()
				$Qipan/lu.add_child(can_move_point)
				can_move_point.texture=load("res://pic/kexingqu.png")
				can_move_point.position = Vector2(100*i, 100*j)
			elif arr[j][i] == -1:
				var begin_point = Sprite.new()
				$Qipan/lu.add_child(begin_point)
				begin_point.texture=load("res://pic/qiziweizhi.png")
				begin_point.position = Vector2(100*i, 100*j)

func add_sprite(args):
	var node = Sprite.new()
	$Qipan/lu.add_child(node)
	node.texture=load(args)
	return node


	# var data = {}
	# var scene = "sceneName"
	
	# #写入
	# func _on_write():
	# 	data = {
	# 		"minLevel":1
	# 	}
	# 	var file = File.new()
	# 	file.open("user://"+scene+".json",File.WRITE)
	# 	var json = to_json(data)
	# 	file.store_line(json)
	# 	file.close()
	# 	pass
	
	# #读取
	# func _on_read():
	# 	var file = File.new()
	# 	file.open("user://"+scene+".json",File.READ)
	# 	var json = parse_json(file.get_as_text())
	# 	print("json===    ",json)
	# 	file.close()


func _on_Button_mouse_entered():
	$Qipan.scale *= 1.2;

func _on_Button_mouse_exited():
	$Qipan.scale /= 1.2;

signal confirm_card(card_id)

func _on_Button_button_down():
	emit_signal("confirm_card", _card_id)




