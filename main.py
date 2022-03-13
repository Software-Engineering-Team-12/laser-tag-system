from src.view import View
from src.controller import Controller
from src.model import Model
# Main function
if __name__=='__main__':

	model = Model()
	model.get_db_cred()
	view = View()
	controller = Controller(model, view)
	view.setController(controller)
	view.root.mainloop()
