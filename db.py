import pymysql


def get_conn():
    """
    获取mysql的链接
    ：return：mysql connection
    """
    return pymysql.connect(
          host = '127.0.0.1',
          user = 'root',
          password = '123456',
          database = 'test',
          charset = 'utf8'
          )

def query_data(sql):
    """
    根据sql查询数据并返回
    ：param sql：sql语句
    ：return：list[dict]
    """
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()
        
        
def insert_or_update_data(sql):
    """
    执行新增insert或者update的sql
    ：param sql：sql语句
    ：return：不返回内容
    """
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()