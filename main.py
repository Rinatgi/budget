import ui
import widgets
import db
import article

window = ui.create_window()
widgets.create_widget(window)
article.print_article()
    
window.mainloop()

