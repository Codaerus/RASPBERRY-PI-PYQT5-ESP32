import pymysql

pot1 = 22
pot2 = 62

con = pymysql.connect(user="admin",password="Raspi@2022#1", host="localhost", database= "MONITOREO")
cursor = con.cursor()
insert_query = f"INSERT INTO sensores(id,tiempo,pot1,pot2) VALUES (NULL, current_timestamp(),{pot1},{pot2});"
cursor.execute(insert_query)
con.commit()
cursor.close()
con.close()
