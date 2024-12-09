import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCalendarWidget, QPushButton, QLabel
from PyQt5.QtCore import QDate, Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QPalette, QColor, QFont, QLinearGradient, QPainter
from datetime import date
import calendar

class AgeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Magical Age Calculator")
        self.setFixedSize(600, 700)
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #2c3e50, stop:1 #3498db);")

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        # Title Label
        title = QLabel("✨Rafi's Magical Age Calculator ✨")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setStyleSheet("color: #ecf0f1; background: transparent;")
        layout.addWidget(title)

        # Calendar Widget
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setStyleSheet("""
            QCalendarWidget QWidget { 
                alternate-background-color: #34495e;
                color: #ecf0f1;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: #ecf0f1;
                background-color: #2c3e50;
                selection-background-color: #e74c3c;
                selection-color: #ecf0f1;
            }
            QCalendarWidget QMenu {
                color: #ecf0f1;
                background-color: #2c3e50;
            }
            QCalendarWidget QSpinBox {
                color: #ecf0f1;
                background-color: #2c3e50;
            }
        """)
        layout.addWidget(self.calendar)

        # Calculate Button
        self.calc_button = QPushButton("Calculate My Age 🎈")
        self.calc_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.calc_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        self.calc_button.clicked.connect(self.calculate_age)
        layout.addWidget(self.calc_button)

        # Result Label
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("Arial", 16))
        self.result_label.setStyleSheet("""
            QLabel {
                color: #ecf0f1;
                background: rgba(44, 62, 80, 0.7);
                padding: 20px;
                border-radius: 10px;
            }
            QLabel strong.years { color: #e74c3c; }
            QLabel strong.months { color: #f1c40f; }
            QLabel strong.days { color: #2ecc71; }
        """)
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

        # Animation setup
        self.animation = QPropertyAnimation(self.result_label, b"geometry")
        self.animation.setDuration(1000)

    def calculate_age(self):
        birth_date = self.calendar.selectedDate().toPyDate()
        today = date.today()
        
        # Calculate age
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            days += calendar.monthrange(today.year, today.month - 1)[1]
        if months < 0:
            years -= 1
            months += 12

        # Animate result with HTML formatting for bold and colored text
        self.result_label.setText(
            f"🎉 You are <strong style='color: #e74c3c'>{years} years</strong>, "
            f"<strong style='color: #f1c40f'>{months} months</strong>, and "
            f"<strong style='color: #2ecc71'>{days} days</strong> old! 🎉"
        )
        
        # Create bounce animation
        current_geometry = self.result_label.geometry()
        self.animation.setStartValue(QRect(current_geometry.x(), current_geometry.y() + 50,
                                         current_geometry.width(), current_geometry.height()))
        self.animation.setEndValue(current_geometry)
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = AgeCalculator()
    calculator.show()
    sys.exit(app.exec_())