import mysql.connector

cnx = mysql.connector.connect(user='root', password='qwerty',
                              host='127.0.0.1',
                              database='paymentsDB_v_1_3_SQLExpress')
cnx.close()