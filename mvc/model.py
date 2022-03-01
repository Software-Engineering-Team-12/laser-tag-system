import psycopg2
import os

class Model:

	# Default constructor
	def __init__(self):
	
		# Database connection
		self.db_connection = None
		
		# Used to interact with the database
		self.cursor = None


	def get_db_cred(self):

		# Name of file
		file_name = 'db-cred.txt'

		# Sub directory
		sub_dir = 'mvc'	

		# Form location
		location = os.path.join(os.getcwd(), sub_dir)
		location = os.path.join(location, file_name)

		# test print 
		print(location)


	def db_open(self):

		# Holds the database url
		database_url = None

		#hardcoded database url
		database_url = "postgres://qozokrewqjtyqa:4809a75a9fdebd8c152ab487c17d78b0afd2f82cb7ac56f90500e6d5bef5f51d@ec2-44-192-245-97.compute-1.amazonaws.com:5432/d81h6qe173j5pl"
		
		# Try and connect to the database
		try:
		
			#line to open the database itself using the database URL
			self.db_connection = psycopg2.connect(database_url, sslmode='require') 
			
			#If the connection is successful print out how awesome Michael the creator is
			if(self.db_connection):
				print("Michael is awesome and the databse is Connected")
				
			#sets the cursor value
			self.cursor = self.db_connection.cursor()
			
		except:
		
			print("Error has occured trying to connect to the database")
			
			
			
	#This method closes the database
	def db_close(self):
		
		
		#This will try to close the database
		try:
		
			#This will close the database connection
			self.db_connection.close()
		
			#This will print out a message if we successfully closed the database
			print("Michael is still awesome and the database is closed")
				
		except:
		
			print("An error has occured and the database did not close successfully")
			
		#Setting the db connection and the cursor back to their original state of empty
		self.db_connection = None
		self.cursor = None
