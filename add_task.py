from ui5_dialog_addtask import *
import sys
import traceback
import win32api, win32con
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AddTask(QWidget, Ui_Dialog_addtask):

	def __init__(self):
		super(AddTask, self).__init__()
		self.initUI()

		today_number = datetime.now().weekday() + 1
		today_week = "星期" + str(today_number)
		self.table_name = str(datetime.now().date()) + "_" + today_week

	def initUI(self):
		self.setupUi(self)
		self.comfirm_btn.clicked.connect(self.update_task)
		self.comfirm_btn_2.clicked.connect(self.showtdtask)
		self.del_btn.clicked.connect(self.dele_task)

		# tasktable setting

		self.tasktable.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.tasktable.setSelectionMode(QTableWidget.SingleSelection)
		self.tasktable.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
		self.tasktable.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置可编辑

		self.tasktable.horizontalHeader().resizeSection(0, 60)  # 第一行列宽
		self.tasktable.horizontalHeader().resizeSection(1, 200)  # 第二行列宽
		self.tasktable.horizontalHeader().resizeSection(2, 60)  # 第三行列宽
		self.tasktable.horizontalHeader().resizeSection(5, 60)
		self.tasktable.horizontalHeader().resizeSection(6, 60)
		self.tasktable.horizontalHeader().resizeSection(7, 60)
		self.tasktable.horizontalHeader().resizeSection(8, 230)
		self.tasktable.horizontalHeader().resizeSection(9, 60)

		"""index 默认为1 """
		temp_data = 1
		data = QTableWidgetItem(str(temp_data))
		self.addtasktable.setItem(0, 0, data)
		for j in range(1, 10):
			temp_data = ''  # 临时记录，不能直接插入表格
			data = QTableWidgetItem(str(temp_data))
			self.addtasktable.setItem(0, j, data)

	def database(self):
		from create_db import CreateDatabase
		# db = pymysql.connect('localhost', 'root', 'mysql', 'MT_TASK', charset='utf8')
		db_01 = CreateDatabase()
		db = db_01.logon_mysql()
		return db

	def comfirm_addtask(self):
		'表格中的数据填进列表'
		try:
			text_list = []
			for i in range(10):
				text_list.append(self.addtasktable.item(0, i).text())
			return text_list
		except Exception as e:
			traceback.print_exc()

	def update_task(self):
		'类表中的数据写入数据库'
		try:
			add_list = self.comfirm_addtask()
			for u in range(1, len(add_list)):
				dic_1 = {1: '任务名称', 2: '任务数量', 3: '预计送检时间', 4: '预计取件时间', 5: '测量类别', 6: '取消任务', 7: '更换任务', 8: '备注',
						 9: '测量过程'}
				if add_list[u] == "":
					win32api.MessageBox(0, "信息不全！请完善  " + dic_1[u] + "  列信息", "提示！", win32con.MB_OK)
					break
				else:

					text_mesg = '请确认要添加的任务 ' + add_list[1] + ' ' + add_list[2] + ' ' + add_list[3] + ' ' + add_list[
						4] + ' ' + \
								add_list[5] + ' ' + add_list[6] + ' ' + add_list[7] + ' ' + add_list[8] + ' ' + \
								add_list[9]

					add_list[0] = self.table_name
					print(add_list, len(add_list))

					aks_1 = win32api.MessageBox(0, text_mesg, "提示！", win32con.MB_YESNOCANCEL)
					try:
						if aks_1 == 6:
							db = self.database()
							cur = db.cursor()
							sql = """INSERT INTO `%s` (`任务名称`,`任务数量`,`预计送检时间`,`预计取件时间`,`测量类别`,`取消任务`,`更换任务`,`备注`,`测量过程`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')
								""" % tuple(add_list)
							print(sql)
							cur.execute(sql)
							db.commit()
							db.close()

							self.showtdtask()
							self.addtasktable.clearContents()
							break
					except Exception as e:
						traceback.print_exc()

		except Exception as e:
			traceback.print_exc()

	def showtdtask(self):
		db = self.database()
		cur = db.cursor()
		sql = """select * from `%s`""" % (self.table_name)
		cur.execute(sql)

		rows = cur.fetchall()
		row = cur.rowcount  # 取得记录个数，用于设置表格的行数
		vol = len(rows[0])  # 取得字段数，用于设置表格的列数
		db.commit()
		db.close()
		for i in range(row):
			for j in range(vol):
				temp_data = rows[i][j]  # 临时记录，不能直接插入表格
				data = QTableWidgetItem(str(temp_data))
				data.setTextAlignment(Qt.AlignCenter)  # 转换后可插入表
				# row = self.tasktable.rowCount()
				self.tasktable.setItem(i, j, data)
				self.tasktable.setEditTriggers(QAbstractItemView.NoEditTriggers)


	def dele_task(self):

		try:
			self.showtdtask()
			row = self.tasktable.selectedItems()
			print(row[0].text())
			msg_text = "您确认要删除 " + chr(10) + str(row[0].text()) + "." + str(row[1].text()) + "." + str(row[2].text())
			TT = win32api.MessageBox(0, msg_text, "提示！", win32con.MB_YESNOCANCEL)
			if TT == 6:  # yes
				db=self.database()
				cur=db.cursor()
				sql_1 = """ DELETE FROM `%s` WHERE `id` = '%s' """%(self.table_name,row[0].text())
				print(sql_1)
				cur.execute(sql_1)
				db.commit()
				db.close()
			self.tasktable.clearContents()
			self.showtdtask()





		except Exception as e:
			traceback.print_exc()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = AddTask()
	main_window.show()
	sys.exit(app.exec_())
