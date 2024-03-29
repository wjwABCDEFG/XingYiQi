extends Node

var normal_material = null
var board_material = null

func _ready():
    normal_material = load("res://material/normal.tres")
    board_material = load("res://material/board.tres")