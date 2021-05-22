import pymysql

# localhost = 127.0.0.1
conn=pymysql.connect(host='localhost', port=3306, user="root",passwd="123456",db="fintech")
# 建立工作環境(游標)
cur = conn.cursor()
# 執行select sql query
cur.execute('select * from stock_daily')
# 將select 結果取出
for row in cur:
    print(row)
    
# 執行 (insert update delete) sql query -----
cur.execute("insert into stock_daily value ('2014','2021/01/04','16.50','16.85','15.90','16.50','96986569','24502','1586464254');")
conn.commit()
# 執行 (insert update delete) sql query end--