extends Node

var _x
var _y

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

func set_idx(a, b):
	_x = a
	_y = b

func on_mouse_up():
	print(_x, _y)
