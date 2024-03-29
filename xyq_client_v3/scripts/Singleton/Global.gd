extends Node
## 全局类，存储着单例、全局方法和变量。
# import 存储的脚本。没有挂在节点上。
const TCPrelated = preload("res://scripts/Network/TCPrelated.gd")   #import 

# 变量
var current_scene = null
var TCP_client = null
var mora_res = false

# function
func _ready():
	var root = get_tree().root
	current_scene = root.get_child(root.get_child_count() - 1)
	TCP_client = TCPrelated.new()

func goto_scene(path):
	call_deferred("_deferred_goto_scene", path) # 延后切换场景避免出问题。

func _deferred_goto_scene(path):
	current_scene.free()
	var s = ResourceLoader.load(path)
	current_scene = s.instance()
	get_tree().root.add_child(current_scene)
	# Optionally, to make it compatible with the SceneTree.change_scene() API.
	get_tree().current_scene = current_scene
