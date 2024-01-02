extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var mora_res = false

# Called when the node enters the scene tree for the first time.
func _ready():
	
	pass # Replace with function body.

func _on_bu_pressed():
	show_res()

func _on_shitou_pressed():
	show_res()

func _on_jiandao_pressed():
	show_res()

func show_res():
	$bottom_plane.hide()
	$result_plane.show()
	# res = get_mora_res_from_server(_) # 获取猜拳结果
	var res = "先手"
	if res == "先手":
		mora_res = true
	$result_plane/win_label.text = res

func _on_mora_timer_timeout():
	$close_timer.start()

func _on_close_timer_timeout():
	swtich_scene("res://scene/game.tscn")
	Global.mora_res =  mora_res

func swtich_scene(_str):
	Global.goto_scene(_str)
