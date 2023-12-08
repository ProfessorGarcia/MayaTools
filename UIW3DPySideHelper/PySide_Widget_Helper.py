from PySide2 import QtWidgets, QtCore, QtGui

class MayaToolHelper(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MayaToolHelper, self).__init__(parent)
        self.setWindowTitle("PySide Widget Helper")#Set the window title
        self.resize(600, 800)#Set the window size
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)#Set the window on top

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        
        # Container Widget
        container = QtWidgets.QWidget()
        self.scrollArea.setWidget(container)

        # Main layout
        layout = QtWidgets.QVBoxLayout(container)

        # QLabel
        label = QtWidgets.QLabel("This is a QLabel")
        layout.addWidget(label)

        # QLineEdit
        lineEdit = QtWidgets.QLineEdit()
        lineEdit.setPlaceholderText("This is a QLineEdit")
        layout.addWidget(lineEdit)

        # QPushButton
        button = QtWidgets.QPushButton("This is a QPushButton")
        layout.addWidget(button)

        # QCheckBox
        checkBox = QtWidgets.QCheckBox("This is a QCheckBox")
        layout.addWidget(checkBox)

        # QRadioButton
        radioButton = QtWidgets.QRadioButton("This is a QRadioButton")
        layout.addWidget(radioButton)

        # QComboBox
        comboBox = QtWidgets.QComboBox()
        comboBox.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(comboBox)

        # QSpinBox
        spinBox = QtWidgets.QSpinBox()
        layout.addWidget(spinBox)

        # QDoubleSpinBox
        doubleSpinBox = QtWidgets.QDoubleSpinBox()
        layout.addWidget(doubleSpinBox)

        # QSlider
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        layout.addWidget(slider)

        # QListWidget
        listWidget = QtWidgets.QListWidget()
        listWidget.addItems(["Item 1", "Item 2", "Item 3"])
        layout.addWidget(listWidget)

        # QTextEdit
        textEdit = QtWidgets.QTextEdit()
        textEdit.setPlaceholderText("This is a QTextEdit")
        layout.addWidget(textEdit)

        # QProgressBar
        progressBar = QtWidgets.QProgressBar()
        progressBar.setValue(50)
        layout.addWidget(progressBar)

        # QTabWidget
        tabWidget = QtWidgets.QTabWidget()
        tab1 = QtWidgets.QWidget()
        tab2 = QtWidgets.QWidget()
        tabWidget.addTab(tab1, "Tab 1")
        tabWidget.addTab(tab2, "Tab 2")
        layout.addWidget(tabWidget)

        # QDialogButtonBox
        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        layout.addWidget(buttonBox)

        # QGroupBox
        groupBox = QtWidgets.QGroupBox("This is a QGroupBox")
        groupBoxLayout = QtWidgets.QVBoxLayout()
        groupBox.setLayout(groupBoxLayout)
        groupBoxLayout.addWidget(QtWidgets.QLabel("Content in GroupBox"))
        layout.addWidget(groupBox)

        # QScrollBar
        scrollBar = QtWidgets.QScrollBar()
        layout.addWidget(scrollBar)

        # QSplitter
        splitter = QtWidgets.QSplitter()
        splitter.addWidget(QtWidgets.QLabel("Splitter Item 1"))
        splitter.addWidget(QtWidgets.QLabel("Splitter Item 2"))
        layout.addWidget(splitter)

        # QToolButton
        toolButton = QtWidgets.QToolButton()
        toolButton.setText("This is a QToolButton")
        layout.addWidget(toolButton)
        
        # QMenuBar
        menuBar = QtWidgets.QMenuBar()
        fileMenu = menuBar.addMenu("This is a QMenuBar")
        fileMenu.addAction("Open")
        fileMenu.addAction("Save")
        fileMenu.addAction("Exit")
        layout.setMenuBar(menuBar)

        # QToolBar
        toolBar = QtWidgets.QToolBar()
        toolBar.addAction("These are a QToolBar -->")
        toolBar.addAction("Cut")
        toolBar.addAction("Copy")
        toolBar.addAction("Paste")
        layout.addWidget(toolBar)

        # QStatusBar
        statusBar = QtWidgets.QStatusBar()
        statusBar.showMessage("This is a status bar")
        layout.addWidget(statusBar)

        # QDockWidget (Note: This needs to be added to a QMainWindow)
        dockWidget = QtWidgets.QDockWidget("Dockable")
        dockWidget.setWidget(QtWidgets.QLabel("DockWidget Content"))
        # Cannot add QDockWidget directly to a QVBoxLayout

        # QGraphicsView
        graphicsScene = QtWidgets.QGraphicsScene()
        graphicsScene.addText("Graphics Scene")
        graphicsView = QtWidgets.QGraphicsView(graphicsScene)
        layout.addWidget(graphicsView)

        # QTreeView
        treeView = QtWidgets.QTreeView()
        layout.addWidget(treeView)

        # QTableView
        tableView = QtWidgets.QTableView()
        layout.addWidget(tableView)

        # QDialogButtonBox
        dialogButtonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        layout.addWidget(dialogButtonBox)

        # QFrame
        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.Box)
        layout.addWidget(frame)

        # QSpacerItem
        layout.addSpacerItem(QtWidgets.QSpacerItem(100, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # QScrollArea
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollAreaContent = QtWidgets.QLabel("Scroll Area Content")
        scrollArea.setWidget(scrollAreaContent)
        layout.addWidget(scrollArea)

        # QSplitter
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(QtWidgets.QLabel("Left Panel"))
        splitter.addWidget(QtWidgets.QLabel("Right Panel"))
        layout.addWidget(splitter)

        # QToolButton
        toolButton = QtWidgets.QToolButton()
        toolButton.setText("Tool Button")
        layout.addWidget(toolButton)
        
        # Set the layout for the main window
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.scrollArea)

# Show the window
my_tool = MayaToolHelper()
my_tool.show()

