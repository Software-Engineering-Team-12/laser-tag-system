import psycopg2

class Model:

	# Default constructor
	def __init__(self):
	
		# creating the db_connection value and starting with a empty value
		self.db_connection = None
		
		#creating a cursor variable and starting it with an empty value
		self.cursor = None


	def db_open(self):
		#hardcoded database url
		DATABASE_URL = "postgres://qozokrewqjtyqa:4809a75a9fdebd8c152ab487c17d78b0afd2f82cb7ac56f90500e6d5bef5f51d@ec2-44-192-245-97.compute-1.amazonaws.com:5432/d81h6qe173j5pl"
		
		#This will try to connect to the database
		try:
		
			#line to open the database itself using the database URL
			self.db_connection = psycopg2.connect(DATABASE_URL, sslmode='require') 
			
			#If the connection is successful print out how awesome Michael the creator is
			if(self.db_connection):
				print("Michael is awesome")
				
			#sets the cursor value
			self.cursor = self.db_connection.cursor()
			
		except:
		
			print("Error has occured trying to connect to the database")
