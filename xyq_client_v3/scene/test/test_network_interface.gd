extends Node


func _ready():
	pass

var openid = "8899"

func _on_match_button_down():
	var msg = i_wrapper.assemble_match(openid)
	Global.TCP_client.put_str(msg)

func _on_move_button_down():
	var msg = i_wrapper.assemble_move()
	Global.TCP_client.put_str(msg)

# func _on_mora_button_down():
# 	var msg = i_wrapper.assemble_mora()
# 	Global.TCP_client.put_str(msg)


func _on_begin_button_down():
	assert(Global.player_id)
	var msg = i_wrapper.assemble_begin(Global.player_id)
	Global.TCP_client.put_str(msg)

# func _on_mora_button_down():
# 	var msg = i_wrapper.assemble_mora()
# 	Global.TCP_client.put_str(msg)

func _process(delta):
	sever_despatch.continuous_get_message()
