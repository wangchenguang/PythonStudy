import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='test',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
try:
    with conn.cursor() as cursor:
        cursor.execute('select * from region where RegionID=%s', ('110100',))
        values = cursor.fetchall()
        print(values)
finally:
    conn.close()
