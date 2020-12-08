import pandas as pd
import matplotlib.pyplot as plt 
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 

class Window(QDialog):  
	def __init__(self, parent=None): 
		super(Window, self).__init__(parent) 
		self.figure = plt.figure(figsize = (15,5)) 
		self.canvas = FigureCanvas(self.figure)  
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.setWindowTitle('Matplotlib In PyQt5') 

		self.button_full_time = QPushButton('Plot College Rank vs Full Time Jobs')  
		self.button_full_time.clicked.connect(self.plot_full_time)

		self.button_part_time = QPushButton('Plot College Rank vs Part Time Jobs')  
		self.button_part_time.clicked.connect(self.plot_part_time)

		self.button_unemp_rate = QPushButton('Plot College Rank vs Unemployment Time Jobs')  
		self.button_unemp_rate.clicked.connect(self.plot_unemp_rate) 

		self.button_college_degree = QPushButton('Plot College Rank vs Jobs requiring College Degree')  
		self.button_college_degree.clicked.connect(self.plot_college_degree)

		self.button_non_college_degree = QPushButton('Plot College Rank vs Jobs not requiring College Degree')  
		self.button_non_college_degree.clicked.connect(self.plot_non_college_degree)

		layout = QVBoxLayout() 
		layout.addWidget(self.toolbar) 
		layout.addWidget(self.canvas) 
		layout.addWidget(self.button_full_time) 
		layout.addWidget(self.button_part_time)
		layout.addWidget(self.button_unemp_rate)
		layout.addWidget(self.button_college_degree)
		layout.addWidget(self.button_non_college_degree)
		self.setLayout(layout)

	def plot_full_time(self):  
		self.figure.clear()  
		ax = self.figure.add_subplot() 
		ax.set_title('College Rank vs Students getting Full Time Job')
		ax.plot(data.Rank, data.Full_time)  
		ax.set_ylabel('Number of Students who got Full Time Job')
		ax.set_xlabel('College Rank')
		self.canvas.draw() 

	def plot_part_time(self):  
		self.figure.clear()  
		ax = self.figure.add_subplot() 
		ax.set_title('College Rank vs Students getting Part Time Job')
		ax.plot(data.Rank, data.Part_time)  
		ax.set_ylabel('Number of Students who got Part Time Job')
		ax.set_xlabel('College Rank')
		self.canvas.draw() 

	def plot_unemp_rate(self):  
		self.figure.clear()  
		ax = self.figure.add_subplot() 
		ax.set_title('College Rank vs Unemployment Rate')
		ax.plot(data.Rank, data.Unemployment_rate)  
		ax.set_ylabel('Unemployment Rate')
		ax.set_xlabel('College Rank')
		self.canvas.draw() 

	def plot_college_degree(self):
		self.figure.clear()  
		ax = self.figure.add_subplot() 
		ax.set_title('College Rank vs Jobs requiring College Degree')
		ax.bar(data.Rank, data.College_jobs, color='green')  
		ax.set_ylabel('Number of Jobs')
		ax.set_xlabel('College Rank')
		self.canvas.draw()

	def plot_non_college_degree(self):
		self.figure.clear()  
		ax = self.figure.add_subplot() 
		ax.set_title('College Rank vs Jobs not requiring College Degree')
		ax.bar(data.Rank, data.Non_college_jobs, color='green')  
		ax.set_ylabel('Number of Jobs')
		ax.set_xlabel('College Rank')
		self.canvas.draw()  

data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv')
app = QApplication([]) 
app.setStyle('Fusion')
main = Window() 
main.show()
app.exec_() 