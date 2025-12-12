import pymysql
import getpass
from sshtunnel import SSHTunnel

class Database:
	def __init__(self):
		self.group_name = "ht25_2_1dl305_group_2"
		self.group_password = "pasSWd_2"
		self.tunnel = None
		self.connection = None
	
	def show_tables(self):
		self.cursor.execute("SHOW TABLES")
		for x in self.cursor:
			print(x)

		# self.cursor.close()

	def connect(self):
		ssh_username = input("Enter your Studium username: ")
		ssh_password = getpass.getpass("Enter your Studium password A: ")

		self.tunnel = SSHTunnel(
			ssh_username, ssh_password, 
			'fries.it.uu.se',
			22)
		
		self.tunnel.start(
			local_host='127.0.0.1', 
			local_port=3306, 
			remote_host='127.0.0.1', 
			remote_port=3306
			)

		self.connection = pymysql.connect(
			database=self.group_name,
			user=self.group_name,
			password=self.group_password, 
			host=self.tunnel.local_host, 
			port=self.tunnel.local_port
		)

	def cursor(self):
		return self.connection.cursor()

	def commit(self):
		self.connection.commit()

	def rollback(self):
		self.connection.rollback()

	def close(self):
		if self.connection:
			self.connection.close()
			self.connection = None
		if self.tunnel:
			self.tunnel.stop()
			self.tunnel = None

if __name__ == "__main__":
	db = Database()
	db.connect()