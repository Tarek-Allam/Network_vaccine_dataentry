import sqlite3
from sqlite3 import Error


class VaccineDB:
    def __init__(self):
        self.connection = None

        sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                    national_id VARCHAR(14) PRIMARY KEY,
                                    name text NOT NULL,
                                    vaccine_code VARCHAR(20),
                                    vaccine_name text NOT NULL,
                                    status text NOT NULL 
                                ); """

        self.create_connection(r'database/vaccineDB.db')
        self.create_table(sql_create_users_table)

    def create_connection(self, db_file_path: str):
        """
        create a database connection to the SQLite database
        specified by db_file
        :param db_file_path
        :return:
        """
        try:
            self.connection = sqlite3.connect(db_file_path)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        """
        create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.connection.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_user(self, data):
        """
        Create a new project into the projects table
        :param data: (national_id: str,name: str, vaccine_code: str, vaccine_name: str, status: str)
        :return: user id
        """
        sql = ''' INSERT INTO users(national_id ,name , vaccine_code, vaccine_name, status)
                VALUES(?,?,?,?,?) '''
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, data)
            self.connection.commit()
            return 'added successfully'
        except sqlite3.IntegrityError as e:
            print(e)

    def update_user_status(self, data):
        """
        update bmi of a user
        :param data: (status: str, national_id:str)
        :return:
        """
        sql = ''' UPDATE users
                SET status = ? 
                WHERE national_id = ?'''
        cur = self.connection.cursor()
        cur.execute(sql, data)
        self.connection.commit()

    def find_one(self, national_id: str):
        """
        Query users by nid
        :param national_id: str
        :return: the row as a triple (national_id, name, vaccine_code, vaccine_name, status)
        """

        cur = self.connection.cursor()
        cur.execute("SELECT * FROM users WHERE national_id=?", (national_id,))

        rows = cur.fetchall()  # this should be a single row since iam fetching using a unique identifier
        try:
            return rows[0]
        except IndexError as e:
            return 'User not found'

    def find_all(self):
        """
        Query all rows in the users table
        :return:
        """
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM users")

        rows = cur.fetchall()

        return rows

    def delete_user(self, national_id):
        """
        Delete a user by user name
        :param name: name, of the user
        :return:
        """
        sql = 'DELETE FROM users WHERE national_id=?'
        cur = self.connection.cursor()
        try:
            cur.execute(sql, (national_id,))
            self.connection.commit()
        except:
            print('user does NOT exits')

    def delete_all_users(self):
        """
        Delete all rows in the users table
        :return:
        """
        sql = 'DELETE FROM users'
        cur = self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()

# if __name__ == '__main__':
#     db = VaccineDB()
#     db.create_user(('12345678912344', 'test', '12345678912345678911', 'test vaccine', 'first'))
#     test = db.find_all()
#     print(test)
#     # user = db.find_one('12345678912345')
#     # print(user)
