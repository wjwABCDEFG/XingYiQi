# -*- coding: utf-8 -*-
"""
测试用的UI，包含左侧请求按钮和右侧返回窗口，需要换成godot展示
@Time    : 2023/11/1 22:47
@Author  : wenjiawei
"""
from PySide6.QtWidgets import QMainWindow

from ui_main import Ui_MainWindow


class UIManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        self.show()
