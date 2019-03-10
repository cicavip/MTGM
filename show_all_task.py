import pymysql
from ui4_dialog_showalltask import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QHeaderView

class Showalltask(QWidget, Ui_Dialog_showalltask):

	def __init__(self):
		super(Showalltask, self).__init__()
		self.initUI()

	def initUI(self):
		self.setupUi(self)
		self.tasktable.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.tasktable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.selecteddata()



	def database(self):
		from create_db import CreateDatabase
		# db = pymysql.connect('localhost', 'root', 'mysql', 'MT_TASK', charset='utf8')
		db_01 = CreateDatabase()
		db = db_01.logon_mysql()
		return db

	def selecteddata(self):
		db=self.database()
		cur = db.cursor()
		sql = """select * from `VW331`"""
		cur.execute(sql)
		rows = cur.fetchall()

		row = cur.rowcount  # 取得记录个数，用于设置表格的行数
		vol = len(rows[0])
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


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window =Showalltask()
	main_window.show()
	sys.exit(app.exec_())
