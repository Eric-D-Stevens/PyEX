import sys
from IEX_wrap import *

from PyQt5.QtWidgets import *
from DayChart import Ui_DayChart
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt

from datetime import datetime

plt.style.use('seaborn')

class DayChartGui(QMainWindow, Ui_DayChart):

    def __init__(self):
        super(DayChartGui, self).__init__()

        # set up ui from designer
        self.ui = Ui_DayChart()
        self.ui.setupUi(self)

        # init date
        self.ui.date_in.setDate(datetime.today())

        # set up connections
        self.ui.get_btn.clicked.connect(self.test_btn)

        self.addToolBar(NavigationToolbar(self.ui.MplGraph.canvas, self))

    def test_btn(self):
        '''
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)

        self.ui.MplGraph.canvas.axes.clear()
        self.ui.MplGraph.canvas.axes.plot(t, cosinus_signal)
        self.ui.MplGraph.canvas.axes.plot(t, sinus_signal)
        self.ui.MplGraph.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.ui.MplGraph.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.ui.MplGraph.canvas.draw()
        '''


        p_token = 'pk_23b0ae9746c642de9500a533c740e06a'
        Api = api(p_token)
        sym = self.ui.sym_in.text()
        day = Api.get_day(sym)

        self.ui.MplGraph.canvas.axes.clear()
        self.ui.MplGraph.canvas.axes.plot(day['highs'], 'g')
        self.ui.MplGraph.canvas.axes.plot(day['lows'], 'r')
        self.ui.MplGraph.canvas.axes.legend(('high', 'low'), loc='upper right')
        self.ui.MplGraph.canvas.axes.set_title(sym)
        self.ui.MplGraph.canvas.draw()





app = QApplication(sys.argv)
widget = DayChartGui()
widget.show()
sys.exit(app.exec_())