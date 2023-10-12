using System.Reflection.Metadata.Ecma335;
using System.IO.Pipes;
using System.Xml.Xsl.Runtime;
using Godot;
using System;

public partial class pai : Sprite2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{

	}


	public InitPai(int[,] pai){ 
		for (int i = 0; i < pai.GetLength(0); i++){
			for (int j = 0; j < pai.GetLength(1); j++)
			{
				int value = pai[i, j];
				if value == "1":
					return;
			}
		}
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{

	}
}
