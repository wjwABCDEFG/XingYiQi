# 组装参数成标准接口发送tcp，接口见接口文档。

func assemble_login(user_name, password):
	# var data = {
	#    "method": "login",
	# 	"user_name" : user_name,
	# 	"password" : password
	# }

	var msg = {
		"types": 0,
		"sender": "26.26.26.1:9905",
		"data": {"method": "login", 
			"user_name": user_name, 
			"password": password
		}
	}
	print(JSON.print(msg))
	return JSON.print(msg)
