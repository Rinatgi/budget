import ui
import widgets
import db


window = ui.create_window()
widgets.create_widget(window)
widgets.update_article_list()
    
window.mainloop()

