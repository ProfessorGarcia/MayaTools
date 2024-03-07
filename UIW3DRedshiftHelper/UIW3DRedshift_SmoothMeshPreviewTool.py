import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets, QtCore, QtGui

def get_maya_main_window():
    """
    Retrieves Maya's main window.
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class SmoothMeshPreviewTool(QtWidgets.QDialog):
    def __init__(self, parent=get_maya_main_window()):
        super(SmoothMeshPreviewTool, self).__init__(parent)

        self.setWindowTitle("Smooth Mesh Preview Tool")
        self.setMinimumWidth(250)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.division_level_slider_label = QtWidgets.QLabel("Preview Division Levels:")
        self.division_level_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.division_level_slider.setMinimum(0)
        self.division_level_slider.setMaximum(3)
        self.division_level_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.division_level_slider.setTickInterval(1)
        self.division_level_value = QtWidgets.QLineEdit("0")
        self.division_level_value.setFixedWidth(40)
        self.division_level_value.setValidator(QtGui.QIntValidator(0, 3))

        self.render_division_slider_label = QtWidgets.QLabel("Render Division Levels:")
        self.render_division_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.render_division_slider.setMinimum(0)
        self.render_division_slider.setMaximum(3)
        self.render_division_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.render_division_slider.setTickInterval(1)
        self.render_division_value = QtWidgets.QLineEdit("0")
        self.render_division_value.setFixedWidth(40)
        self.render_division_value.setValidator(QtGui.QIntValidator(0, 3))

        self.use_preview_for_rendering_cb = QtWidgets.QCheckBox("Use Preview Level for Rendering")
        self.apply_btn = QtWidgets.QPushButton("Apply")

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        division_layout = QtWidgets.QHBoxLayout()
        division_layout.addWidget(self.division_level_slider_label)
        division_layout.addWidget(self.division_level_slider)
        division_layout.addWidget(self.division_level_value)

        render_division_layout = QtWidgets.QHBoxLayout()
        render_division_layout.addWidget(self.render_division_slider_label)
        render_division_layout.addWidget(self.render_division_slider)
        render_division_layout.addWidget(self.render_division_value)

        main_layout.addLayout(division_layout)
        main_layout.addLayout(render_division_layout)
        main_layout.addWidget(self.use_preview_for_rendering_cb)
        main_layout.addWidget(self.apply_btn)

    def create_connections(self):
        self.apply_btn.clicked.connect(self.apply_settings)
        self.division_level_slider.valueChanged.connect(self.update_preview_division_value)
        self.division_level_value.textChanged.connect(self.update_preview_division_slider)
        self.render_division_slider.valueChanged.connect(self.update_render_division_value)
        self.render_division_value.textChanged.connect(self.update_render_division_slider)

    def apply_settings(self):
        division_level = self.division_level_slider.value()
        render_division_level = self.render_division_slider.value()
        use_preview_for_rendering = self.use_preview_for_rendering_cb.isChecked()

        selected_objects = cmds.ls(selection=True)
        
        if not selected_objects:
            cmds.warning("No objects selected. Please select one or more mesh objects.")
            return

        for obj in selected_objects:
            shapes = cmds.listRelatives(obj, children=True, shapes=True) or []
            for shape in shapes:
                if cmds.nodeType(shape) == "mesh":
                    cmds.setAttr(f"{shape}.displaySmoothMesh", 2)  # Enable Smooth Mesh Preview
                    cmds.setAttr(f"{shape}.smoothLevel", division_level)
                    cmds.setAttr(f"{shape}.useSmoothPreviewForRender", use_preview_for_rendering)
                    cmds.setAttr(f"{shape}.renderSmoothLevel", render_division_level)
                else:
                    cmds.warning(f"{obj} does not contain a mesh shape or does not support smooth mesh preview.")

    def update_preview_division_value(self, value):
        self.division_level_value.setText(str(value))

    def update_preview_division_slider(self, value):
        self.division_level_slider.setValue(int(value))

    def update_render_division_value(self, value):
        self.render_division_value.setText(str(value))

    def update_render_division_slider(self, value):
        self.render_division_slider.setValue(int(value))

def show_ui():
    global smooth_mesh_preview_tool_ui
    try:
        smooth_mesh_preview_tool_ui.close()
        smooth_mesh_preview_tool_ui.deleteLater()
    except:
        pass

    smooth_mesh_preview_tool_ui = SmoothMeshPreviewTool()
    smooth_mesh_preview_tool_ui.show()

show_ui()
