import pymysql

# xlrd 为 python 中读取 excel 的库，支持.xls 和 .xlsx 文件
import xlrd
#  导入excel 任务到数据中。
#  文件存放到程序目录下，命名：MT_TASK.xlsx
#
def ts(t):
    import time
    if t!="":
        timestamp = float(t)*24*3600

        t_1 = time.strftime('%Y%m%d', time.localtime())
        r_1 = time.strptime(t_1, "%Y%m%d")
        tp = int(time.mktime(r_1))+timestamp

        # 转换成localtime
        time_local = time.localtime(tp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime("%H:%M:%S", time_local)

        return dt
    else:
        return "-"

def importExcelToMysql(path):
    ### xlrd版本
    # 读取excel文件
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    workbook_name = path.split("\\")[3].split('.')[0]
    ###


    # 将表中数据读到 sqlstr 数组中
    t=worksheet.nrows
    for i in range(2, t):
        row = worksheet.row(i)

        sqlstr = []
        for str in sqlstr:
            if str =="-":
                str ="0"
        for j in range(0, worksheet.ncols):
            sqlstr.append(worksheet.cell_value(i, j))
            ###


        value = (sheets[0],sqlstr[0], sqlstr[1], ts(sqlstr[2]), ts(sqlstr[3]),sqlstr[4],
                 ts(sqlstr[5]),ts(sqlstr[6]),sqlstr[7],ts(sqlstr[8]),ts(sqlstr[9]),sqlstr[10],
                 ts(sqlstr[11]),ts(sqlstr[12]),sqlstr[13],ts(sqlstr[14]),ts(sqlstr[15]),sqlstr[16],ts(sqlstr[17]),
                 ts(sqlstr[18]),sqlstr[19],ts(sqlstr[20]),ts(sqlstr[21]))

        print(value)

        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "mysql", "MT_TASK", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 插入语句
        sql = """INSERT INTO `MT_TASK`.`%s` (`part_name`,`part_num_1`,`sent_time_1`,`get_time_1`,
        `part_num_2`,`sent_time_2`,`get_time_2`,
        `part_num_3`,`sent_time_3`,`get_time_3`,
        `part_num_4`,`sent_time_4`,`get_time_4`,
        `part_num_5`,`sent_time_5`,`get_time_5`,
        `part_num_6`,`sent_time_6`,`get_time_6`,
        `part_num_7`,`sent_time_7`,`get_time_7`
        ) values ('%s', '%s','%s','%s','%s','%s','%s','%s','%s',
        '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') """ % value
        print(sql)
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()


        # 关闭数据库连接
        # db.close()



# if __name__ == "__main__":
#
#     pro_addr =  os.path.realpath('.')
#     path = os.path.join(pro_addr ,"MT_TASK.xlsx")
#     # 和数据库建立连接
#     conn = pymysql.connect('localhost', 'root', 'mysql', 'MT_TASK', charset='utf8')
#     # 创建游标链接
#     cur = conn.cursor()
#     cur.execute("DROP TABLE IF EXISTS VW331")
#     sql = """CREATE TABLE IF NOT EXISTS VW331(
#             part_name VARCHAR(100),
#             part_num_1  CHAR(50),
#             sent_time_1 CHAR(50),
#             get_time_1 CHAR(50) ,
#             part_num_2  CHAR(50),
#             sent_time_2 CHAR(50),
#             get_time_2 CHAR(50),
#             part_num_3  CHAR(50),
#             sent_time_3 CHAR(50),
#             get_time_3 CHAR(50),
#             part_num_4  CHAR(50),
#             sent_time_4 CHAR(50),
#             get_time_4 CHAR(50),
#             part_num_5  CHAR(50),
#             sent_time_5 CHAR(50),
#             get_time_5 CHAR(50),
#             part_num_6  CHAR(50),
#             sent_time_6 CHAR(50),
#             get_time_6 CHAR(50),
#             part_num_7  CHAR(50),
#             sent_time_7 CHAR(50),
#             get_time_7 CHAR(50)
#         )ENGINE=InnoDB DEFAULT CHARSET=utf8
#         """
#
#     try:
#         # 执行sql语句
#         cur.execute(sql)
#         # 提交到数据库执行
#         conn.commit()
#     except:
#         # Rollback in case there is any error
#         conn.rollback()
#
#     # 关闭数据库连接
#     conn.close()
#     importExcelToMysql(path)

