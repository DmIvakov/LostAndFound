from src.uiMainWindow import QtWidgets, Ui_MainWindow

def toggle_beautiful_style(app_or_widget, enable: bool = True):
    modern_dark_qss = """
        QWidget {
            background-color: #1e1e2e;
            color: #cdd6f4;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 15px;
        }
        QMainWindow, QDialog {
            background-color: #1e1e2e;
        }
        QPushButton {
            background-color: #313244;
            color: #cdd6f4;
            border: 1px solid #45475a;
            border-radius: 6px;
            padding: 3px 8px;
            min-height: 22px;
        }
        QPushButton:hover {
            background-color: #45475a;
            border-color: #585b70;
        }
        QPushButton:pressed {
            background-color: #585b70;
        }
        QLineEdit, QTextEdit, QPlainTextEdit, QDateEdit, QComboBox {
            background-color: #11111b;
            color: #cdd6f4;
            border: 1px solid #313244;
            border-radius: 6px;
            padding: 4px 8px;
            selection-background-color: #89b4fa;
            selection-color: #11111b;
        }
        QLineEdit:focus, QTextEdit:focus, QDateEdit:focus, QComboBox:focus {
            border: 1px solid #89b4fa;
        }
        QComboBox::drop-down, QDateEdit::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            border-left: 1px solid #313244;
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
        }
        QComboBox::down-arrow, QDateEdit::down-arrow {
            image: none;
        }
        QComboBox QAbstractItemView, QDateEdit QAbstractItemView {
            background-color: #11111b;
            color: #cdd6f4;
            selection-background-color: #45475a;
            selection-color: #cdd6f4;
            border: 1px solid #313244;
            outline: none;
        }
        QCalendarWidget QWidget {
            background-color: #1e1e2e;
            color: #cdd6f4;
        }
        QCalendarWidget QToolButton {
            background-color: #313244;
            color: #cdd6f4;
            border-radius: 4px;
            margin: 2px;
        }
        QCalendarWidget QToolButton:hover {
            background-color: #45475a;
        }
        QCalendarWidget QMenu {
            background-color: #11111b;
            color: #cdd6f4;
        }
        QCalendarWidget QSpinBox {
            background-color: #11111b;
            color: #cdd6f4;
            border: 1px solid #313244;
            border-radius: 4px;
        }
        QCalendarWidget QAbstractItemView:enabled {
            background-color: #11111b;
            color: #cdd6f4;
            selection-background-color: #89b4fa;
            selection-color: #11111b;
        }
        QTabWidget::pane {
            border: 1px solid #313244;
            border-radius: 6px;
            background-color: #1e1e2e;
            top: -1px;
        }
        QTabBar::tab {
            background-color: #181825;
            color: #6c7086;
            padding: 6px 12px;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            border: 1px solid #313244;
            border-bottom: none;
            margin-right: 2px;
        }
        QTabBar::tab:selected {
            background-color: #313244;
            color: #cdd6f4;
            border-color: #45475a;
        }
        QTabBar::tab:hover:not(:selected) {
            background-color: #11111b;
            color: #a6adc8;
        }
        QListView, QTreeView {
            background-color: #11111b;
            color: #cdd6f4;
            border: 1px solid #313244;
            border-radius: 6px;
        }
        QTableView, QTableWidget {
            background-color: #11111b;
            color: #cdd6f4;
            border: 1px solid #313244;
            border-radius: 6px;
            gridline-color: #313244;
        }
        QTableView::item, QTableWidget::item {
            background-color: #11111b;
            color: #cdd6f4;
        }
        QTableView::item:selected, QTableWidget::item:selected {
            background-color: #45475a;
            color: #cdd6f4;
        }
        QScrollBar:vertical {
            background: #1e1e2e;
            width: 8px;
        }
    """
    if enable:
        app_or_widget.setStyleSheet(modern_dark_qss.strip())
    else:
        app_or_widget.setStyleSheet("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.tblReports.setAlternatingRowColors(False)
    
    header_style = "QHeaderView::section { background-color: #181825; color: #89b4fa; border: 1px solid #313244; padding: 4px; }"
    ui.tblReports.horizontalHeader().setStyleSheet(header_style)
    ui.tblReports.verticalHeader().setStyleSheet(header_style)
    
    toggle_beautiful_style(app)

    MainWindow.show()
    sys.exit(app.exec_())
