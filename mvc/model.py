import psycopg2
import os

class Model:

	# Default constructor
	def __init__(self):
	
		# Database connection
		self.db_connection = None
		
		# Used to interact with the database
		self.cursor = None


	# Gets the database url from the text file
	def get_db_cred(self):

		# Name of text file
		file_name = 'db-cred.txt'

		# Sub directory file resides in
		sub_dir = 'mvc'	

		# Form location to file
		location = os.path.join(os.getcwd(), sub_dir)
		location = os.path.join(location, file_name)

		# Try and open the db-cred file		
		try:

			# Open file and return the url
			with open(location, 'r') as file:

				return file.read()

		# If it fails, handle error
		except IOError:
			
			print('An error occured while opening the db-cred.txt file. Please make sure it exists with the proper name.')


	# Opens the database for reading/writing
	def db_open(self):

		# Holds the database url
		database_url = self.get_db_cred() 

		# Try and connect to the database
		try:
		
			# Create connection to the database
			self.db_connection = psycopg2.connect(database_url, sslmode='require') 
			
			# Sets the cursor value
			self.cursor = self.db_connection.cursor()

			print('Database connection successful!')

		# If it fails, handle error
		except:
		
			print('Connection failed! Double check the database credentials are correct.')


	#This method closes the database
	def db_close(self):
		
		#This will try to close the database
		try:
		
			# This will close the database connection
			self.db_connection.close()
		
			# This will print out a message if we successfully closed the database
			print("Database connection closed successfully!")
				
		except:
		
			print("An error has occured and the database did not close successfully")
			
		# Setting the db connection and the cursor back to their original state of empty
		self.db_connection = None
		self.cursor = None
			
