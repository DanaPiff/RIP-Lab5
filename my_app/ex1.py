import pymysql

pymysql.install_as_MySQLdb()

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="M97c2d6l",
    db="first_db"
)

# курсор

c = db.cursor()

# Вставка

#c.execute("INSERT INTO product (product_name, cost) VALUES (%s, %s)", ('пироженка', '75'))
#db.commit()
c.execute('SELECT * FROM product;')
entries = c.fetchall()

for e in entries:
    print(e)
c.close()
db.close()