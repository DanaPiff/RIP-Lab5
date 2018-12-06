import pymysql

pymysql.install_as_MySQLdb()


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        #Параметры соединения
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db)

    def disconnect(self):
        if self._connection:
            self._connection.close()

class Product:

    def __init__(self, db_connection, product_name, cost):
        self.db_connection = db_connection.connection
        self.product_name = product_name
        self.cost = cost

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO product (product_name, cost) VALUES (%s, %s)", (self.product_name, self.cost))
        self.db_connection.commit()
        c.close()

con = Connection("root","M97c2d6l","first_db")

with con:
    product = Product(con, 'Бананчик', '15')
    product.save()