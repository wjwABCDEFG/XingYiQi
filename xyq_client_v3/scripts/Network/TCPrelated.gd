
var client

func _init():
    client = StreamPeerTCP.new()
    client.connect_to_host("26.26.26.1", 9999)

func get_str():
    var data = client.get_utf8_string(client.get_available_bytes())
    if data != null && data != "":
        print(data)
        return data

func put_str(_str):
    client.put_data(_str.to_ascii())


signal sv_match_complete(player_id, game_id)
func parse_match(dic: Dictionary):
    # emit_signal("sv_match_complete", dic["player_id"], dic["game_id"]) # TODO 未应用
    Global.player_id = dic["player_id"]
    Global.game_id = dic["game_id"]
    Global.power = dic["power"]

signal sv_begin_complte(dic)
func parse_begin(dic: Dictionary):
    emit_signal("sv_begin_complte", dic)