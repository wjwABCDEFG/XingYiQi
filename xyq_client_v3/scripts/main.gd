extends Node2D

func _ready():
	yield(get_tree().create_timer(1), "timeout")

func swtich_scene(_str):
	Global.goto_scene(_str)

func _on_stop_button_down():
	#匹配
	$stop.hide()
	$start.disabled = false

func _on_start_button_down():
	$stop.show()
	$start.disabled = true
	yield(get_tree().create_timer(1), "timeout")
	swtich_scene("res://scene/mora.tscn")

