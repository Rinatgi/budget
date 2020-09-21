import ui
import widgets
import db

window = ui.create_window()
widgets.create_widget(window)
db.read_file()
    
window.mainloop()

