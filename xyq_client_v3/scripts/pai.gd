extends Node2D
# 单张牌类

var _card_id
var viable_area = []
var viable_area_offset = []
var begin_point

func init(card_name):
	_card_id = card_name
	var card_details = PieceProcessor.read_card_detail(card_name)
	_init_pai(card_details)
	_init_offset()

func _init_offset():
	assert(begin_point)
	for v2 in viable_area:
		viable_area_offset.push_back(v2 - begin_point)

func _init_pai(arr):
	for j in arr.size():
		for i in arr[j].size():
			if arr[j][i] == 1:
				var Sp = Sprite.new()
				$Qipan/lu.add_child(Sp)
				Sp.texture=load("res://pic/kexingqu.png")
				Sp.position = Vector2(100*i, 100*j)
				viable_area.append(Vector2(j, i))
			elif arr[j][i] == -1:
				var Sp = Sprite.new()
				$Qipan/lu.add_child(Sp)
				Sp.texture=load("res://pic/qiziweizhi.png")
				Sp.position = Vector2(100*i, 100*j)
				begin_point = Vector2(j, i)

func add_sprite(args):
	var node = Sprite.new()
	$Qipan/lu.add_child(node)
	node.texture=load(args)
	return node

var _normal_mat = load("res://material/normal.tres");
var _fire_mat = load("res://material/fire_outline.tres");

func set_choice(state):
	if state:
		self.get_child(0).material = _fire_mat
	else:
		self.get_child(0).material = _normal_mat

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

signal confirm_card(instance)

func _on_Button_button_down():
	emit_signal("confirm_card", self)




