from tkinter import END
class Controller:

	# Default constructor
	def __init__(self, model, view):
		self.model = model
		self.view = view
	
	# Method to query database for player id
	def query_db(self, id, name, team_dict):
		# grab id from entry field
		str = id.get()
		# if id entry has text check if it is in database
		if str:
			# if the name exists in the database set it to the codename field
			codename = self.model.search_for_player_by_id(str)
			if codename:
				name.config(state = 'normal')
				name.delete(0,END)
				name.insert(0, codename)
				# skip placing curor inside name box and make read-only
				name.config(state = 'readonly',takefocus=0)
				# add to team dictionary for passing to play screen
				if id not in team_dict:
					team_dict[name.get()] = 0
			# otherwise, allow user to enter a name for the id to be stored with
			else:
				name.config(state = "normal")
	
	# Method for storing name into database
	def store_db(self, id, name, team_dict):
		# checks if the entry is available and will store in database then change field back to read only
		if name["state"] == "normal":
			self.model.insert_new_player(id.get(), name.get())
			name.config(state = "readonly")
			# add to team dictionary for passing to play screen
			if id not in team_dict:
				team_dict[name.get()] = 0
