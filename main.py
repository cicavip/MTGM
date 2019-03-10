#程序主入口
from gm_main import *

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main_ui = Parentwindow()
	"""窗口UI"""
	mtgm_ui = MTGM_window()
	showtodaytask_ui = Dialog_showtodaytask()
	"""按钮动作"""
	btn = main_ui.main_ui.mtgm_btn
	btn.clicked.connect(mtgm_ui.show)
	btn_3 = mtgm_ui.showtodaytask
	btn_3.clicked.connect(showtodaytask_ui.show)
	main_ui.show()
	sys.exit(app.exec_())
