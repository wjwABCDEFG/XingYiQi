extends Node

var b_our_camp = false
var posX = 0
var posY = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func set_texture(args):
	self.get_child(0).texture = args

func set_camp(args):
	b_our_camp = args

func set_pos(x, y):
	posX = x
	posY = y

func _on_Button_mouse_exited():
	if b_our_camp:
		self.scale /= 1.2

func _on_Button_mouse_entered():
	if b_our_camp:
		self.scale *= 1.2

signal confirm_piece(camp, x, y)

func _on_Button_button_up():
	emit_signal("confirm_piece", b_our_camp, posX, posY)
	
