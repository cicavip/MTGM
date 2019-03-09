import sys
from PyQt5.QtWidgets import *
import win32api, win32con
import traceback
from MTGM.show_today_task import *
from MTGM.ui3_dialog_task import Ui_Dialog_task
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import *


class Dialog_showtodaytask(QWidget, Ui_Dialog_task):

	def __init__(self,date= "Unknown"):
		super(Dialog_showtodaytask, self).__init__()
		self.initUI()

		date_set_1 = date
		if date_set_1 == "Unknown":
			date_0 = str(datetime.now().date()) + "_" + "星期" + str(datetime.now().weekday() + 1)
			self.date_setted = date_0
		else:
			self.date_setted = date



	def database(self):
		db = pymysql.connect('localhost', 'root', 'mysql', 'MT_TASK', charset='utf8')
		return db

	def initUI(self):
		self.setupUi(self)

		self.tasktable.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取
		self.tasktable.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置选取方式为单个选取
		self.tasktable.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # 默认是每栏等宽显示，但是用户可以根据需要自己调整每列的宽度
		# 设置每列的宽度
		self.tasktable.horizontalHeader().resizeSection(0, 60)  # 第一行列宽
		self.tasktable.horizontalHeader().resizeSection(1, 200)  # 第二行列宽
		self.tasktable.horizontalHeader().resizeSection(2, 60)  # 第三行列宽
		self.tasktable.horizontalHeader().resizeSection(5, 60)
		self.tasktable.horizontalHeader().resizeSection(6, 60)
		self.tasktable.horizontalHeader().resizeSection(7, 60)
		self.tasktable.horizontalHeader().resizeSection(8, 230)
		self.tasktable.horizontalHeader().resizeSection(9, 60)

		# # 窗口弹出后直接显示今日任务状态
		# self.table_showtodaytask()
		"""显示今天任务状态"""
		self.refresh.clicked.connect(self.table_showtodaytask)
		"""重置今天任务内容"""
		self.resettask.clicked.connect(self.table_resettask)

		# 每次更改内容，自动保存更新到数据库
		self.tasktable.itemChanged.connect(self.table_update)
		self.savechanged.clicked.connect(self.table_update)

		"""显示更改界面"""
		self.change.clicked.connect(self.table_changetaskstatus)

	def table_showtodaytask(self):
		# 显示今天任务
		try:
			self.setWindowTitle("最新任务状态")
			self.tasktable.clearContents()
			tbl_list = self.task_confirm()  # c查询今天任务的table是否以及生成
			# today_number = datetime.now().weekday() + 1
			# today_week = "星期" + str(today_number)
			# table_name = str(datetime.now().date()) + "_" + today_week
			table_name = self.date_setted
			if table_name in tbl_list:  # 判断是已经生成今天任务表

				db = self.database()
				cur = db.cursor()
				sql = """select * from `%s`""" % (table_name)
				cur.execute(sql)

				rows = cur.fetchall()
				row = cur.rowcount  # 取得记录个数，用于设置表格的行数
				vol = len(rows[0])  # 取得字段数，用于设置表格的列数
				db.commit()
				for i in range(row):
					for j in range(vol):
						temp_data = rows[i][j]  # 临时记录，不能直接插入表格
						data = QTableWidgetItem(str(temp_data))
						data.setTextAlignment(Qt.AlignCenter)  # 转换后可插入表
						row = self.tasktable.rowCount()
						# self.tasktable.insertRow(row)
						self.tasktable.setItem(i, j, data)
						self.tasktable.setEditTriggers(QAbstractItemView.NoEditTriggers)
			else:
				aks_1 = win32api.MessageBox(0, "今天还没创建任务列表，是否建立？？", "提示！", win32con.MB_YESNOCANCEL)
				if aks_1 == 6:
					self.add_todaytask()
					self.table_showtodaytask()
		except Exception as e:
			traceback.print_exc()

	def table_resettask(self, ):
		# 重置今天任务
		TT = win32api.MessageBox(0, "您正在重置今天任务，‘测量类别’，‘取消任务’，‘备注’，‘测量过程’都将清除内容，是否继续？", "提示！", win32con.MB_YESNOCANCEL)
		if TT == 6:  # yes
			try:
				self.add_todaytask()
				self.tasktable.clearContents()
				table_name = self.date_setted

				db = self.database()
				cur = db.cursor()
				sql = """select * from `%s`""" % (table_name)
				cur.execute(sql)
				rows = cur.fetchall()
				row = cur.rowcount  # 取得记录个数，用于设置表格的行数
				vol = len(rows[0])  # 取得字段数，用于设置表格的列数
				db.commit()

				for i in range(row):
					for j in range(vol):
						temp_data = rows[i][j]  # 临时记录，不能直接插入表格
						data = QTableWidgetItem(str(temp_data))
						data.setTextAlignment(Qt.AlignCenter)  # 转换后可插入表
						row = self.tasktable.rowCount()
						# self.tasktable.insertRow(row)
						self.tasktable.setItem(i, j, data)
						self.tasktable.setEditTriggers(QAbstractItemView.NoEditTriggers)
			except Exception as e:
				traceback.print_exc()
			self.table_showtodaytask()
		else:
			return

	def table_changetaskstatus(self, ):
		# 更改任务  excle表格 内
		try:
			self.setWindowTitle("更改任务状态")
			table_name = self.date_setted

			db = self.database()
			cur = db.cursor()
			sql = """select * from `%s`""" % (table_name)
			cur.execute(sql)
			rows = cur.fetchall()
			row = cur.rowcount  # 取得记录个数，用于设置表格的行数
			vol = len(rows[0])  # 取得字段数，用于设置表格的列数
			db.commit()
			for i in range(row):
				for j in range(vol):
					temp_data = rows[i][j]  # 临时记录，不能直接插入表格
					data = QTableWidgetItem(str(temp_data))  # 转换后可插入表
					data.setTextAlignment(Qt.AlignCenter)  # 将数据设置 居中显示
					row = self.tasktable.rowCount()
					# self.tasktable.insertRow(row)
					self.tasktable.setItem(i, j, data)
					self.tasktable.setEditTriggers(QAbstractItemView.DoubleClicked)
				# self.tasktable.setEnabled(True)
				# 添加选择框
				# 1.选择测量过程
				# comBox = QComboBox()
				# comBox.addItems(['未完成', '完成', '其他'])
				# # comBox.addItem('中途取消')
				# comBox.setStyleSheet('QComboBox{margin:3px}')
				# self.tasktable.setCellWidget(i, 9, comBox)
				# self.tasktable.setItem(i, 9, QTableWidgetItem(comBox.currentText()))
				# # 2.选择测量类别
				# comBox = QComboBox()
				# comBox.addItems(['批量', '分析', '其他'])
				# # comBox.addItem('中途取消')
				# comBox.setStyleSheet('QComboBox{margin:3px}')
				# self.tasktable.setCellWidget(i, 5, comBox)
				# self.tasktable.cellWidget(i, 5).currentText()
				# self.tasktable.setItem(i, 5, QTableWidgetItem(comBox.currentText()))

		except Exception as e:
			traceback.print_exc()

	def add_todaytask(self):
		#  更新今天任务状态
		tt = Showtadaytask()
		tt.data_into_taday_task()

	def table_update(self, ):
		# 更改table内容以后，保存到数据库。
		try:
			info = []
			row_select = self.tasktable.selectedItems()
			if len(row_select) == 0:
				return
			task_name = row_select[1].text()

			for i in range(10):
				info_0 = row_select[i].text()
				info_1 = str(info_0)
				info.append(info_1)
			print("info： " + str(info))
			'''判断 测量类别 是否是 批量或者分析'''
			cllb = ['批量', '分析']
			if info[5] not in cllb:
				win32api.MessageBox(0, "请输入 " + cllb[0] + "或者" + cllb[1], "提示！", win32con.MB_OK)
			else:

				'''
				 以下可以加入保存数据到数据的操作'''
				table_name = self.date_setted
				conn = pymysql.connect('localhost', 'root', 'mysql', 'MT_TASK', charset='utf8')
				cur = conn.cursor()
				# arg_1= []
				arg_1 = info[:]
				arg_1.insert(1, table_name)
				print("arg_1: " + str(arg_1))
				sql = "UPDATE `MT_TASK`.`%s` SET `测量类别` = '%s',`取消任务` = '%s',`更换任务` = '%s',`备注` = '%s',`测量过程` = '%s'" % (
					str(arg_1[1]), str(arg_1[6]), str(arg_1[7]), str(arg_1[8]), str(arg_1[9]),
					str(arg_1[10])) + " where `id` = %s" % (arg_1[0])
				print(sql)

				try:
					cur.execute(sql)
					conn.commit()
					conn.close()
				except Exception as e:
					traceback.print_exc()

				win32api.MessageBox(0, "任务名称:  {}".format(task_name) + " 已经更新并存储", "提示！", win32con.MB_OK)
		except Exception as e:
			traceback.print_exc()
			if e == pymysql.err.ProgrammingError:
				self.table_resettask()
			else:
				return

	def task_confirm(self):
		# 确认今天的数据库是否已经生成。

		db = self.database()
		cur = db.cursor()
		sql = """show tables"""
		cur.execute(sql)
		rows = cur.fetchall()
		db.commit()

		tbl_list = []
		for tbl in rows:
			tbl_1 = tbl[0]
			tbl_list.append(tbl_1)
		return tbl_list



if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_window = Dialog_showtodaytask()
	main_window.show()
	sys.exit(app.exec_())
