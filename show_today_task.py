from datetime import datetime


class Showtadaytask():
	"""显示当天的任务状态
	"""

	def __init__(self):
		pass
		'数据库的登录信息'
	# 	self.host = 'localhost'  # mysql的ip或者本地的地址
	# 	self.user = 'root'  # mydql的用户
	# 	self.pw = 'mysql'  # mysql的密码
	#
	# def logon_mysql(self, database_name='MT_TASK'):
	# 	'''prompt：数据库连接
	# 			1.inputdata:数据库名称（可选）
	#
	# 	'''
	# 	db = pymysql.connect(self.host, self.user, self.pw, database_name,
	# 						 charset='utf8')
	# 	return db
	def logon_mysql(self):
		from create_db import CreateDatabase
		# db = pymysql.connect('localhost', 'root', 'mysql', 'MT_TASK', charset='utf8')
		db_01 = CreateDatabase()
		db = db_01.logon_mysql()
		return db

	def create_today_db_table(self):
		today_number = datetime.now().weekday() + 1
		today_week = "星期" + str(today_number)
		table_name = str(str(datetime.now().date()) + "_" + today_week)
		cur = self.logon_mysql().cursor()
		cur.execute("show tables")
		cur.execute("drop table if exists`%s`" % (table_name))

		sql = """CREATE TABLE IF NOT EXISTS `%s`(
				`id` int(11) NOT NULL AUTO_INCREMENT, 
				任务名称 VARCHAR(100),
				任务数量  CHAR(50),
				预计送检时间 CHAR(50),
				预计取件时间 CHAR(50) ,
				测量类别  CHAR(50) NOT NULL DEFAULT "批量",
				取消任务 CHAR(50) NOT NULL DEFAULT "否",
				更换任务 CHAR(50) NOT NULL DEFAULT "否",
				备注  CHAR(50) NOT NULL DEFAULT "无",
				测量过程 CHAR(50)NOT NULL DEFAULT "未测量",
				PRIMARY KEY (`id`)
			)ENGINE=InnoDB DEFAULT CHARSET=utf8
			""" % table_name

		try:
			# 执行sql语句
			cur.execute(sql)
			# 提交到数据库执行
			self.logon_mysql().commit()
		except:
			# Rollback in case there is any error
			self.logon_mysql().rollback()

		# 关闭数据库连接
		self.logon_mysql().close()

	def select_today_task(self):
		"""按照时间从总任务中选择当天的任务信息
			#return 当天的任务信息
		"""

		# 判断时间为周几
		today = datetime.now().weekday() + 1
		part_num = 'part_num_' + str(today)
		sent_time = 'sent_time_' + str(today)
		get_time = 'sent_time_' + str(today)
		part_name = "part_name"

		cur = self.logon_mysql().cursor()
		values = (part_name, part_num, sent_time, get_time, part_num)
		sql = """select %s,%s,%s,%s from `MT_TASK`.`VW331` WHERE %s <> ""
				""" % values

		# 执行sql语句
		cur.execute(sql)
		# 提交到数据库执行
		self.logon_mysql().commit()
		results = cur.fetchall()
		# 当天的任务信息
		return results

	def data_into_taday_task(self):
		"""将选择的当天的信息写入当天的任务表中
		"""
		today_number = datetime.now().weekday() + 1
		today_week = "星期" + str(today_number)
		table_name = str(str(datetime.now().date()) + "_" + today_week)
		data = self.select_today_task()
		self.create_today_db_table()

		for each_data in data:
			each_data_list = list(each_data)
			each_data_list.insert(0, table_name)
			each_data2 = tuple(each_data_list)
			db = self.logon_mysql()
			# 使用cursor()方法获取操作游标
			cur = db.cursor()
			sql = """INSERT INTO `%s` (`任务名称`,`任务数量`,`预计送检时间`,`预计取件时间`) VALUES ('%s','%s','%s','%s'); """ % \
				  each_data2
			# 执行sql语句
			cur.execute(sql)
			# 提交到数据库执行
			db.commit()
			db.close()

	def select_show_data(self):
		today_number = datetime.now().weekday() + 1
		today_week = "星期" + str(today_number)
		""""选择出今天的任务状态"""
		db = self.logon_mysql()
		# 使用cursor()方法获取操作游标
		cur = db.cursor()
		sql = """select * from `%s`""" % (today_week)
		print(sql)
		cur.execute(sql)
		date_will_be_showed = cur.fetchall()

		# 提交到数据库执行
		db.commit()
		db.close()
		return date_will_be_showed




if __name__ == "__main__":
	tt = Showtadaytask()
	tt.create_today_db_table()
	#     tt.select_today_task()
	# tt.data_into_taday_task()
# print(tt.select_show_data())
