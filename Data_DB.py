import pymysql
import write_file

def write_to_sql(data):

    connect = pymysql.Connect(
        host='localhost',
        port=8806,
        user='root',
        passwd='123456',
        db='python3',
        charset='utf8'
    )

    cur = connect.cursor()

    for i in data:
        """这里的data参数是指正则匹配并处理后的列表数据(是一个大列表，包含所有电影信息，每个电影信息都存在各自的一个列表中；
        对大列表进行迭代，提取每组电影信息，这样提取到的每组电影信息都是一个小列表，然后就可以把每组电影信息写入数据库了)"""

        movie = i  # 每组电影信息，这里可以看做是准备插入数据库的每组电影数据
        write_file.write_to_file(movie)
        sql = "insert into maoyantop100(ranking,image,title,actor,release_time,score) values(%s, %s, %s, %s,%s, %s)"  # sql插入语句
        try:
            cur.execute(sql, movie)  # 执行sql语句，movie即是指要插入数据库的数据
            connect.commit()  # 插入完成后，不要忘记提交操作
            #print('导入成功')

        except:
            #print('导入失败')
            return None
    cur.close()  # 关闭游标
    connect.close()  # 关闭连接