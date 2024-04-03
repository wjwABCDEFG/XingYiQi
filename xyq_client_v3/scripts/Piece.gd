extends Node

var b_our_camp = false
var posX = 0
var posY = 0
var id = null
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func set_texture(args):
	self.get_child(0).texture = args

func set_camp(args):
	b_our_camp = args

func set_id(args):
	id = args

func set_pos(x, y):
	posX = x
	posY = y

func _on_Button_mouse_exited():
	if b_our_camp:
		self.scale /= 1.2

func _on_Button_mouse_entered():
	if b_our_camp:
		self.scale *= 1.2

signal confirm_piece(instance)

func _on_Button_button_up():
	emit_signal("confirm_piece", self)
	

var _normal_mat = load("res://material/normal.tres");
var _fire_mat = load("res://material/fire_outline.tres");

func set_choice(state):
	if state:
		self.get_child(0).material = _fire_mat
	else:
		self.get_child(0).material = _normal_mat