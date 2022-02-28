import src.view as View
import src.controller as Controller
import src.model as Model
# Main function
if __name__=='__main__':

	model = Model.Model()
	view = View.View()
	controller = Controller.Controller(model, view)
	view.setController(controller)
	view.window.mainloop()
