extends Node

var _x
var _y

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

func set_idx(a, b):
	_x = a
	_y = b

signal confirm_cherkerboard(arg1, arg2)

func _on_Button_button_up():
	emit_signal("confirm_cherkerboard", _x, _y)
