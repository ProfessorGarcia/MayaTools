from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds

class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.Signal()

    def __init__(self, parent=None):
        super(ClickableLabel, self).__init__(parent)

    def mouseReleaseEvent(self, event):
        self.clicked.emit()

class ProductionTool(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ProductionTool, self).__init__(parent)
        self.setWindowTitle("Uiw3d Production Tool")
        self.resize(400, 300)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        
        # Container Widget
        container = QtWidgets.QWidget()
        self.scrollArea.setWidget(container)

        # Main layout
        layout = QtWidgets.QVBoxLayout(container)

        # Tab widget
        tabWidget = QtWidgets.QTabWidget()
        layout.addWidget(tabWidget)

        # Add tabs
        tabWidget.addTab(self.createModelCheckerTab(), "ModelChecker")
        tabWidget.addTab(self.createLookDevTab(), "LookDev")
        tabWidget.addTab(self.createRiggingTab(), "Rigging")

        # Set layout for the main window
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.scrollArea)

    def createModelCheckerTab(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)

        # Instructions - Step 1: Cleanup Normals
        step1label = QtWidgets.QLabel("Step 1: Cleanup your normals")
        layout.addWidget(step1label)

        # Button - Toggle Vertex Normals
        toggleNormalsButton = QtWidgets.QPushButton("Toggle Vertex Normals")
        layout.addWidget(toggleNormalsButton)
        toggleNormalsButton.clicked.connect(self.toggleVertexNormals)

        # Button - Cleanup Normals
        cleanupNormalsButton = QtWidgets.QPushButton("Cleanup Normals")
        layout.addWidget(cleanupNormalsButton)
        cleanupNormalsButton.clicked.connect(self.cleanupNormals)

        # Instructions - Step 2: Cleanup UV Sets Button
        step2label = QtWidgets.QLabel("Step 2: Cleanup your uv's")
        layout.addWidget(step2label)

        # Horizontal layout for icons
        iconLayout = QtWidgets.QHBoxLayout()

        # Icon - UV Editor as ClickableLabel
        uvEditorIcon = QtGui.QPixmap(r"C:\Users\thear\Documents\maya\2024\prefs\icons\textureEditor.png")
        uvEditorLabel = ClickableLabel()
        uvEditorLabel.setPixmap(uvEditorIcon)
        uvEditorLabel.setScaledContents(True)
        uvEditorLabel.setFixedSize(40, 40)  # Adjust size as needed
        iconLayout.addWidget(uvEditorLabel)
        uvEditorLabel.clicked.connect(self.openUVEditor)

        # Icon - Camera-Based UV as ClickableLabel
        cameraUVIcon = QtGui.QPixmap(r"C:\Users\thear\Documents\maya\2024\prefs\icons\polyCameraUVs.png")  # Update with the correct path
        cameraUVLabel = ClickableLabel()
        cameraUVLabel.setPixmap(cameraUVIcon)
        cameraUVLabel.setScaledContents(True)
        cameraUVLabel.setFixedSize(40, 40)  # Adjust size as needed
        iconLayout.addWidget(cameraUVLabel)
        cameraUVLabel.clicked.connect(self.createCameraBasedUVs)

        # Add the icon layout to the main layout
        layout.addLayout(iconLayout)

        # Icon - Delete All History as ClickableLabel
        deleteHistoryIcon = QtGui.QPixmap(r"C:\Users\thear\Documents\maya\2024\prefs\icons\menuIconEdit.png")  # Update with the correct path
        deleteHistoryLabel = ClickableLabel()
        deleteHistoryLabel.setPixmap(deleteHistoryIcon)
        deleteHistoryLabel.setScaledContents(True)
        deleteHistoryLabel.setFixedSize(40, 40)  # Adjust size as needed
        iconLayout.addWidget(deleteHistoryLabel)
        deleteHistoryLabel.clicked.connect(self.deleteAllHistory)

        layout.addLayout(iconLayout)

        # Button - Clean UV Sets
        cleanupUVButton = QtWidgets.QPushButton("Cleanup UV Sets")
        layout.addWidget(cleanupUVButton)
        cleanupUVButton.clicked.connect(self.cleanupUVSets)

        return widget

    def createLookDevTab(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        # Add LookDev specific widgets here
        return widget

    def createRiggingTab(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        # Add Rigging specific widgets here
        return widget

    def toggleVertexNormals(self):
        selected_objects = cmds.ls(selection=True, type='transform')
        if not selected_objects:
            cmds.warning("No objects selected")
            return

        # Toggling the display of vertex normals
        for obj in selected_objects:
            current_state = cmds.polyOptions(obj, query=True, displayNormal=True)
            new_state = not current_state[0]
            cmds.polyOptions(obj, displayNormal=new_state, sizeNormal=1)

        print("Toggled vertex normals for selected objects")

    def cleanupNormals(self):
        # Maya commands to cleanup normals
        selected_objects = cmds.ls(selection=True)
        if selected_objects:
            for obj in selected_objects:
                cmds.polyNormalPerVertex(obj, ufn=True)
                cmds.polySoftEdge(obj, angle=180)
                cmds.delete(obj, ch=True)
            print("Normals cleaned up for selected objects")
        else:
            cmds.warning("No objects selected")

    def openUVEditor(self):
        # Function to open UV Editor in Maya
        cmds.TextureViewWindow()

    def createCameraBasedUVs(self):
        selected_objects = cmds.ls(selection=True, type='transform')
        if not selected_objects:
            cmds.warning("No objects selected for UV projection")
            return

        for obj in selected_objects:
            cmds.polyProjection(obj, type="Planar", md="p", constructionHistory=True)

        print("Camera-based UVs created for selected objects")

    def deleteAllHistory(self):
        selected_objects = cmds.ls(selection=True, type='transform')
        if not selected_objects:
            cmds.warning("No objects selected for history deletion")
            return

        for obj in selected_objects:
            cmds.delete(obj, constructionHistory=True)

        print("Deleted all history for selected objects")

    def cleanupUVSets(self):
        # Maya commands to cleanup UV sets
        selected_objects = cmds.ls(selection=True, type='transform')
        if selected_objects:
            for obj in selected_objects:
                uvSets = cmds.polyUVSet(obj, query=True, allUVSets=True)
                if uvSets:
                    # Ensure the first UV set is named 'map1'
                    if uvSets[0] != 'map1':
                        cmds.polyUVSet(obj, uvSet=uvSets[0], newUVSet='map1', rename=True)
                        uvSets[0] = 'map1'
                    # Delete all UV sets except for 'map1'
                    for uvSet in uvSets:
                        if uvSet != 'map1':
                            cmds.polyUVSet(obj, delete=True, uvSet=uvSet)
            print("UV sets cleaned up for selected objects")
        else:
            cmds.warning("No objects selected")

def showTool():
    global production_tool
    try:
        production_tool.close()
    except:
        pass
    production_tool = ProductionTool()
    production_tool.show()

showTool()
