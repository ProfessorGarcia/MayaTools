from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds

from PySide2 import QtWidgets, QtGui, QtCore

class CollapsibleSection(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleSection, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(text=title, checkable=True, checked=False)
        self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.toggled.connect(self.toggle)

        self.content_area = QtWidgets.QWidget()
        self.content_layout = QtWidgets.QVBoxLayout()
        self.content_area.setLayout(self.content_layout)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.toggle_button)
        main_layout.addWidget(self.content_area)
        main_layout.addStretch()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(main_layout)

    def toggle(self):
        if self.toggle_button.isChecked():
            self.content_area.setVisible(True)
            self.toggle_button.setArrowType(QtCore.Qt.DownArrow)
            self.setMaximumHeight(self.sizeHint().height())
        else:
            self.content_area.setVisible(False)
            self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
            self.setMaximumHeight(self.toggle_button.sizeHint().height())

        
class UIW3DRedshiftHelper(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIW3DRedshiftHelper, self).__init__(parent)
        self.setWindowTitle("UIW3D Redshift Helper")
        self.setMinimumSize(800, 600)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        icon_path = r"C:\Users\thear\Documents\maya\2024\prefs\icons\iconUIW3D.png"
        icon = QtGui.QIcon(icon_path)
        self.setWindowIcon(icon)

        self.layout = QtWidgets.QVBoxLayout(self)

        # Create Render Settings Group
        custom_settings_group = QtWidgets.QGroupBox("Render Settings")
        custom_settings_layout = QtWidgets.QVBoxLayout(custom_settings_group)
        

        # Create sub-group for Custom Settings fields
 
        custom_settings_fields_group = QtWidgets.QGroupBox("Custom Settings Fields")
        custom_settings_fields_layout = QtWidgets.QFormLayout()

        self.width_input = QtWidgets.QLineEdit("1920")
        self.height_input = QtWidgets.QLineEdit("1080")
        
        trace_depth_settings_fields_group = QtWidgets.QGroupBox("Trace Depth Settings")
        trace_depth_settings_fields_layout = QtWidgets.QFormLayout()
        
        self.combined_depth_input = QtWidgets.QLineEdit("6")
        self.num_gi_bounces_input = QtWidgets.QLineEdit("4")
        self.reflection_depth_input = QtWidgets.QLineEdit("2")
        self.refraction_depth_input = QtWidgets.QLineEdit("2")
        self.volume_max_trace_depth_input = QtWidgets.QLineEdit("2")
        self.transparency_max_trace_depth_input = QtWidgets.QLineEdit("2")

        custom_settings_fields_layout.addRow("Width:", self.width_input)
        custom_settings_fields_layout.addRow("Height:", self.height_input)
        trace_depth_settings_fields_layout.addRow("Combined:", self.combined_depth_input)
        trace_depth_settings_fields_layout.addRow("Global Illumination:", self.num_gi_bounces_input)
        trace_depth_settings_fields_layout.addRow("Reflection:", self.reflection_depth_input)
        trace_depth_settings_fields_layout.addRow("Refraction:", self.refraction_depth_input)
        trace_depth_settings_fields_layout.addRow("Volume:", self.volume_max_trace_depth_input)
        trace_depth_settings_fields_layout.addRow("Transparency:", self.transparency_max_trace_depth_input)

        custom_settings_fields_group.setLayout(custom_settings_fields_layout)
        custom_settings_layout.addWidget(custom_settings_fields_group)
        

        
        testLayout = CollapsibleSection(title="Settings")
        self.layout.addWidget(testLayout)
        testLayout.content_layout.addWidget(custom_settings_fields_group)
        
        trace_depth_settings_fields_group.setLayout(trace_depth_settings_fields_layout)
        custom_settings_layout.addWidget(trace_depth_settings_fields_group)
        testLayout.content_layout.addWidget(trace_depth_settings_fields_group)
        
        # Apply Custom Settings Button
        self.apply_custom_settings_button = QtWidgets.QPushButton("Apply Custom Settings")
        self.apply_custom_settings_button.clicked.connect(self.apply_custom_settings)
        self.apply_custom_settings_button.setStyleSheet("QPushButton { background-color: #c9103b; border: 10px solid #c9103b; color: white; } QPushButton:pressed { background-color: #8e0922; border: 10px solid #8e0922; color: white; }")

        # Quick Render Settings Button
        self.quick_render_settings_button = QtWidgets.QPushButton("Quick Render Settings")
        self.quick_render_settings_button.clicked.connect(self.apply_quick_settings)
        self.quick_render_settings_button.setStyleSheet("QPushButton { background-color: #c9103b; border: 10px solid #c9103b; color: white; } QPushButton:pressed { background-color: #8e0922; border: 10px solid #8e0922; color: white; }")

        #custom_settings_layout.addWidget(self.apply_custom_settings_button)
        custom_settings_layout.addWidget(self.quick_render_settings_button)
        
        
        testLayout.content_layout.addWidget(self.apply_custom_settings_button)
        self.layout.addWidget(custom_settings_group)

        # Convert Lambert to Redshift Group
        convert_to_redshift_group = QtWidgets.QGroupBox("Convert Lambert to Redshift")
        convert_to_redshift_layout = QtWidgets.QVBoxLayout(convert_to_redshift_group)

        # Create Lambert to Redshift button
        self.convert_lambert_button = QtWidgets.QPushButton("Convert Lambert to Redshift")
        self.convert_lambert_button.clicked.connect(self.convert_selected_lambert_to_redshift)
        self.convert_lambert_button.setStyleSheet("QPushButton { background-color: #c9103b; border: 10px solid #c9103b; color: white; } QPushButton:pressed { background-color: #8e0922; border: 10px solid #8e0922; color: white; }")

        convert_to_redshift_layout.addWidget(self.convert_lambert_button)
        self.layout.addWidget(convert_to_redshift_group)
    
    def create_settings_fields(self, layout):
            # Create layout for settings
            settings_layout = QtWidgets.QFormLayout()
    
            # Resolution
            self.width_input = QtWidgets.QLineEdit("1920")
            self.height_input = QtWidgets.QLineEdit("1080")
            settings_layout.addRow("Resolution Width:", self.width_input)
            settings_layout.addRow("Resolution Height:", self.height_input)
    
            # Reflection Trace Depth
            self.reflection_depth_input = QtWidgets.QLineEdit("2")
            settings_layout.addRow("Reflection Trace Depth:", self.reflection_depth_input)
    
            # Refraction Trace Depth
            self.refraction_depth_input = QtWidgets.QLineEdit("2")
            settings_layout.addRow("Refraction Trace Depth:", self.refraction_depth_input)
    
            # Combined Trace Depth
            self.combined_depth_input = QtWidgets.QLineEdit("6")
            settings_layout.addRow("Combined Trace Depth:", self.combined_depth_input)
    
            # Apply Custom Settings Button
            self.apply_custom_settings_button = QtWidgets.QPushButton("Apply Custom Settings")
            self.apply_custom_settings_button.clicked.connect(self.apply_custom_settings)
            settings_layout.addRow(self.apply_custom_settings_button)
    
            layout.addLayout(settings_layout)

    
    def apply_quick_settings(self):
        # Apply predefined quick settings
        cmds.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")
        cmds.setAttr("redshiftOptions.imageFormat", 2)  # PNG
        cmds.setAttr("defaultResolution.width", 1920)
        cmds.setAttr("defaultResolution.height", 1080)
        cmds.setAttr("redshiftOptions.primaryGIEngine", 4)  # GI Engine to Brute Force
        cmds.setAttr("redshiftOptions.reflectionMaxTraceDepth", 2)
        cmds.setAttr("redshiftOptions.refractionMaxTraceDepth", 2)
        cmds.setAttr("redshiftOptions.combinedMaxTraceDepth", 6)
        cmds.setAttr("redshiftOptions.bucketSize", 64)
        cmds.setAttr("redshiftOptions.bucketOrder", 0)  # Horizontal
        cmds.setAttr("redshiftOptions.denoisingEnabled", 1)
        cmds.setAttr("redshiftOptions.denoiseEngine", 3)  # OptiX
        cmds.setAttr("redshiftOptions.volumeMaxTraceDepth", 2)  # Add this line
        cmds.setAttr("redshiftOptions.transparencyMaxTraceDepth", 2)  # Add this line
        cmds.setAttr("redshiftOptions.numGIBounces", 4)
        print("Quick Redshift render settings applied.")


    def apply_custom_settings(self):
        settings = {
            "defaultResolution.width": int(self.width_input.text()),
            "defaultResolution.height": int(self.height_input.text()),
            "redshiftOptions.reflectionMaxTraceDepth": int(self.reflection_depth_input.text()),
            "redshiftOptions.refractionMaxTraceDepth": int(self.refraction_depth_input.text()),
            "redshiftOptions.combinedMaxTraceDepth": int(self.combined_depth_input.text()),
            "redshiftOptions.volumeMaxTraceDepth": int(self.volume_max_trace_depth_input.text()),
            "redshiftOptions.transparencyMaxTraceDepth": int(self.transparency_max_trace_depth_input.text()),
            "redshiftOptions.numGIBounces": int(self.num_gi_bounces_input.text())
        }

        for attr, value in settings.items():
            cmds.setAttr(attr, value)

        print("Custom Redshift render settings applied.")

    def convert_selected_lambert_to_redshift(self):
        selected_objects = cmds.ls(selection=True, dag=True, long=True, type="mesh")

        if not selected_objects:
            cmds.warning("No mesh objects selected.")
            return

        for obj in selected_objects:
            shading_groups = cmds.listConnections(obj, type='shadingEngine')
            if not shading_groups:
                continue

            for sg in shading_groups:
                materials = cmds.ls(cmds.listConnections(sg), materials=True)
                for mat in materials:
                    if cmds.objectType(mat) == 'lambert' and mat != 'lambert1':
                        color = cmds.getAttr(mat + '.color')[0]
                        rs_material = cmds.shadingNode('RedshiftMaterial', asShader=True, name=mat + "_rs")
                        cmds.setAttr(rs_material + '.diffuse_color', color[0], color[1], color[2], type='double3')
                        cmds.setAttr(rs_material + '.refl_roughness', 1)

                        sg = cmds.listConnections(mat, type='shadingEngine')
                        if sg:
                            cmds.connectAttr(rs_material + '.outColor', sg[0] + '.surfaceShader', force=True)
                        cmds.delete(mat)

                        print(f"Converted {mat} to Redshift material with reflection roughness set to 1.")     
        
def show_ui():
    global ui
    try:
        ui.close()
    except:
        pass

    ui = UIW3DRedshiftHelper()
    ui.show()

show_ui()
