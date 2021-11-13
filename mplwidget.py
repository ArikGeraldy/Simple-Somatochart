# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

    
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

# class MplWidget2(QWidget):
    
#     def __init__(self, parent = None):

#         QWidget.__init__(self, parent)
        
#         self.canvas2 = FigureCanvas(Figure())
#         vertical_layout = QVBoxLayout()
#         vertical_layout.addWidget(self.canvas2)
#         self.canvas2.axes = self.canvas2.figure.add_subplot(111)
#         self.setLayout(vertical_layout)

# class MplWidget3(QWidget):
    
#     def __init__(self, parent = None):

#         QWidget.__init__(self, parent)
        
#         self.canvas3 = FigureCanvas(Figure())
        
#         vertical_layout = QVBoxLayout()
#         vertical_layout.addWidget(self.canvas3)
        
#         self.canvas3.axes = self.canvas3.figure.add_subplot(111)
#         self.setLayout(vertical_layout)

# class MplWidget4(QWidget):
    
#     def __init__(self, parent = None):

#         QWidget.__init__(self, parent)
        
#         self.canvas4 = FigureCanvas(Figure())
        
#         vertical_layout = QVBoxLayout()
#         vertical_layout.addWidget(self.canvas4)
        
#         self.canvas4.axes = self.canvas4.figure.add_subplot(111)
#         self.setLayout(vertical_layout)

# class MplWidget5(QWidget):
    
#     def __init__(self, parent = None):

#         QWidget.__init__(self, parent)
        
#         self.canvas5 = FigureCanvas(Figure())
        
#         vertical_layout = QVBoxLayout()
#         vertical_layout.addWidget(self.canvas5)
        
#         self.canvas5.axes = self.canvas5.figure.add_subplot(111)
#         self.setLayout(vertical_layout)