
var client

func _init():
	client = StreamPeerTCP.new()
	client.connect_to_host("192.168.0.104",9999)

func get_str():
	var data = client.get_utf8_string(client.get_available_bytes())
	if data != null && data != "":
		print(data)
		return data

func put_str(_str):
	client.put_data(_str.to_ascii())