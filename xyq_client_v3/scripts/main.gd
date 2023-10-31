
extends Node2D

const TCPrelated = preload("Network/TCPrelated.gd")   #import 
var client

func _ready():
	client = TCPrelated.new()
	yield(get_tree().create_timer(1), "timeout")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func swtich_scene(_str):
	Global.goto_scene(_str)

func _on_stop_button_down():
	$stop.hide()
	$start.disabled = false

func _on_start_button_down():
	$stop.show()
	$start.disabled = true
	yield(get_tree().create_timer(1), "timeout")
	swtich_scene("res://scene/game.tscn")

