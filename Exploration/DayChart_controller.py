import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
from DyChart import Ui_DayChart

# get todays date
today = datetime.datetime.today().strftime('%Y-%m-%d')
print(today)

app = QApplication(sys.argv)
app.setStyle('Fusion')

window = QMainWindow()
ui = Ui_DayChart()

print(dir(ui))
ui.setupUi(window)

window.show()
sys.exit(app.exec_())

