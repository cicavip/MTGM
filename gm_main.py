# 界面主窗口 + 测量管理窗口
import win32ui
from ui_main import *
from ui2_mtgm import *
from ui3_dialog_task_show import *
from task_updatesheet import *
from show_all_task import *
from add_task import AddTask


from PyQt5.QtWidgets import QCalendarWidget



class Parentwindow(QMainWindow, Ui_MainWindow):
	""" 开始窗口： 连接窗口 """

	def __init__(self, parent=None):
		super(Parentwindow, self).__init__(parent)
		self.main_ui = Ui_MainWindow()
		self.main_ui.setupUi(self)

class MTGM_window(Ui_Form, Ui_Dialog_task, QtWidgets.QMainWindow, QCalendarWidget):  # 从自动生成的界面类继承
	"""显示测量管理子窗口
		1,Ui_Form 是主界面
		2，Ui_Dialog_task 是 弹出的今天任务状态
	"""

	def __init__(self, parent=None):
		super(MTGM_window, self).__init__()
		self.setupUi(self)  # 在此设置界面

		# 在此，可添加自定义的信号绑定
		# 导入新任务
		self.updatetask.clicked.connect(self.taskupdate_button)
		# 根据选定日期显示任务状态
		self.cal = self.calendarWidget
		self.cal.setGridVisible(True)  # 网格显示
		self.cal.selectionChanged.connect(self.showselecteddatetask)
		#显示全部任务
		self.showalltask.clicked.connect(self.showalltasktable)

		#添加删除任务
		self.add_del_task.clicked.connect(self.add_delete_task)


	def taskupdate_button(self):
		# 更新任务总表
		dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
		dlg.SetOFNInitialDir(r'E:\01_MProject\MTGM')  # 设置打开文件对话框中的初始显示目录
		dlg.DoModal()
		path = dlg.GetPathName()

		# 和数据库建立连接
		if path != "":
			conn = pymysql.connect('localhost', 'root', 'mysql', 'MT_TASK', charset='utf8')

			# 创建游标链接
			cur = conn.cursor()
			cur.execute("DROP TABLE IF EXISTS VW331")
			sql = """CREATE TABLE IF NOT EXISTS VW331(
							part_name VARCHAR(100),
							part_num_1  CHAR(50),
							sent_time_1 CHAR(50),
							get_time_1 CHAR(50) ,
							part_num_2  CHAR(50),
							sent_time_2 CHAR(50),
							get_time_2 CHAR(50),
							part_num_3  CHAR(50),
							sent_time_3 CHAR(50),
							get_time_3 CHAR(50),
							part_num_4  CHAR(50),
							sent_time_4 CHAR(50),
							get_time_4 CHAR(50),
							part_num_5  CHAR(50),
							sent_time_5 CHAR(50),
							get_time_5 CHAR(50),
							part_num_6  CHAR(50),
							sent_time_6 CHAR(50),
							get_time_6 CHAR(50),
							part_num_7  CHAR(50),
							sent_time_7 CHAR(50),
							get_time_7 CHAR(50)
						)ENGINE=InnoDB DEFAULT CHARSET=utf8
						"""
			#
			try:
				# 执行sql语句
				cur.execute(sql)
				# 提交到数据库执行
				conn.commit()
			except:
				# Rollback in case there is any error
				conn.rollback()
			#
			# # 关闭数据库连接
			conn.close()
			importExcelToMysql(path)
			# 将任务按照星期进行分布
			todaytask = Showtadaytask()
			todaytask.create_today_db_table()
			todaytask.data_into_taday_task()
		else:
			return

	def showselecteddatetask(self):
		try:
			date = self.selecte_date()# 返回日期
			aks_1 = win32api.MessageBox(0, "您选择显示的日期为 --"+date+"-- \n\n 即将为您显示~", "提示！", win32con.MB_YESNOCANCEL)
			if aks_1 == 6:
				self.dlg_1 = Dialog_showtodaytask(date)
				self.dlg_1.show()
		except Exception as e:
			traceback.print_exc()

	def selecte_date(self):
		# 返回选择的日期 格式为 ’2019-02-20_星期3‘
		try:
			self.cal = self.calendarWidget
			self.cal.setGridVisible(True)
			d = self.cal.selectedDate()
			date_1 = d.toString("yyyy-MM-dd")
			date_2 = d.dayOfWeek()
			date = str(date_1) + "_星期" + str(date_2)
			return date
		except Exception as e:
			traceback.print_exc()

	def showalltasktable(self):
		try:
			self.dlg_2 = Showalltask()
			self.dlg_2.show()

		except Exception as e:
			traceback.print_exc()

	def add_delete_task(self):
		self.dlg_2 = AddTask()
		self.dlg_2.show()



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main_ui = Parentwindow()

	"""窗口UI"""
	mtgm_ui = MTGM_window()  # 测量管理ui
	# kfgm_ui = KFMG_window()#库房管理ui
	showtodaytask_ui = Dialog_showtodaytask()  # 今天任务窗口Ui


	"""按钮动作"""
	# 主界面1 测量管理按钮 单击后显示测量管理窗口
	btn = main_ui.main_ui.mtgm_btn
	btn.clicked.connect(mtgm_ui.show)
	# 主界面2 测量管理按钮 单击后显示库房管理窗口
	# btn_2 = main_ui.main_ui.kfgm_btn
	# btn_2.clicked.connect(child_ui.show)

	# 测量管理按钮1 单击后显示今天任务状态
	btn_3 = mtgm_ui.showtodaytask
	btn_3.clicked.connect(showtodaytask_ui.show)


	# # 显示
	main_ui.show()
	sys.exit(app.exec_())
