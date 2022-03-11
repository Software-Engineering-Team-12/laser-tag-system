from tkinter import END
class Controller:

	# Default constructor
	def __init__(self, model, view):
		self.model = model
		self.view = view
	
	# Method to query database for player id
	def query_db(self,id,name):
		# grab id from entry field
		str = id.get()
		# if id entry has text check if it is in database
		if str:
			# if the name exists in the database set it to the codename field
			codename = model.search_for_player_by_id(str)
			if codename:
				name.config(state = 'normal')
				name.delete(0,END)
				name.insert(0, codename)
				name.config(state = 'readonly')
			# otherwise, allow user to enter a name for the id to be stored with
			else:
				name.config(state = "normal")

	# Method for storing name into database
	def store_db(self, id, name):
		# checks if the entry is available and will store in database then change field back to read only
		if name["state"] == "normal":
			model.insert_new_player(id.get(), name.get())
			name.config(state = "readonly")
	
	# Method to add all of the entries to arrays for storage
	# def gatherEntries(self, red_entries_id, red_entries_codename, green_entries_id, green_entries_codename):
	# 	red_entries = []
	# 	green_entries = []
	# 	for n in range(20):
	# 		red_id = red_entries_id[n].get()
	# 		red_codename = red_entries_codename[n].get()
	# 		green_id = green_entries_id[n].get()
	# 		green_codename = green_entries_codename[n].get()
	# 		red_dict = {"id": red_id, "codename": red_codename}
	# 		green_dict = {"id": green_id, "codename": green_codename}
	# 		red_entries.append(red_dict)
	# 		green_entries.append(green_dict)

