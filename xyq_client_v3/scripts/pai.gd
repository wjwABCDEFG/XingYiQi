extends Node2D

var json_path = "res://config/pai.json"
var car_details

func init(car_name):
	read(json_path)
	assert(car_details!=null)
	var arr = car_details[car_name]
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

func read(path):
	var file = File.new()
	file.open(path, File.READ)
	car_details = parse_json(file.get_as_text())
	file.close()

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

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
