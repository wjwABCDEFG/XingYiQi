class_name i_wrapper

# 组装参数成标准接口发送tcp，接口见接口文档。

static func assemble_login(user_name, password):
	var msg = {
		"types": 1,
		"sender": "",
		"data": {"method": "login", 
			"user_name": user_name, 
			"password": password
		}
	}
	return JSON.print(msg)


static func assemble_mora(gameid, quan):
	var msg = {
		"types": 1,
		"sender": "",
		"data": {
			"game_id": gameid,
			"quan": quan
		}
	}
	return JSON.print(msg)

static func assemble_move(chess_id, pai_id,from_pos, to_pos):
	var msg = {
		"types": 1,
		"sender": "",
		"data": {"method": "move", 
			'params': {
                   'player_id': Global.player_id,
                   'chess_id': chess_id,
                   'pai_id': pai_id,
                   'from_pos': from_pos, # [0, 0],
                   'to_pos': to_pos #[1, 1]
               }
		}
	}
	return JSON.print(msg)

static func assemble_match(openid):
	var msg = {
		"types": 1,
		"sender": "",
		"data": {"method": "match", 
				"params": {"open_id": openid}
		}
	}
	return JSON.print(msg)

static func assemble_begin(player_id):
	var msg = {
		"types": 1,
		"sender": "",
		"data": {"method": "begin",
				"params": {"player_id": player_id}
		}
	}
	return JSON.print(msg)
