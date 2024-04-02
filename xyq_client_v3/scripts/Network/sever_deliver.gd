class_name sever_deliver

static func continuous_get_message():
	var msg = Global.TCP_client.get_str()
	if(msg):
		print("=======begin=======")
		print(msg)
		print("=======end=======")
		var p = JSON.parse(msg)
		if typeof(p.result) == TYPE_DICTIONARY:
			var code = p.result["data"]["code"]
			if code == 500:
				push_error("-- error 500" + p.result["data"]["msg"])
				return
			var data = p.result["data"]["data"]
			if typeof(data) == TYPE_STRING:  # 链接成功
				# print(data)
				pass
			elif typeof(data) == TYPE_DICTIONARY:
				if data.has("state"): # 有state 说明是匹配
					Global.TCP_client.parse_match(data)
				if data.has("pan"): # 绘制棋盘
					Global.TCP_client.parse_begin(data)
		else:
			push_error("Unexpected results." + msg) # 可能粘包
