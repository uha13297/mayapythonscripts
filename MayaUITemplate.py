"""
Maya/QT UI template
Maya 2023
"""

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial # optional, for passing args during signal function calls
import sys

class MayaUITemplate(QtWidgets.QWidget):
    """
    Create a default tool window.
    """
    window = None
    
    def __init__(self, parent = None):
        """
        Initialize class.
        """
        super(MayaUITemplate, self).__init__(parent = parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.widgetPath = r'C:\Users\uhata\OneDrive\Documents\maya\projects\AnimTransfer\scripts\PoseTransfer.ui'
        self.widget = QtUiTools.QUiLoader().load(self.widgetPath)
        self.widget.setParent(self)
        # set initial window size
        self.resize(200, 100)      
        # locate UI widgets
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_Close')
        self.btn_TransferPose = self.widget.findChild(QtWidgets.QPushButton, 'btn_TransferPose')
        # assign functionality to buttons
        self.btn_close.clicked.connect(self.close)
        self.btn_TransferPose.clicked.connect(self.TransferPose)
    

    def TransferPose(self):
        def transfer_selected(*args):
            """Transfer pose from first selected rig to the rest of the selection."""
            namespaces = get_selected_namespaces()
            selection = cmds.ls(selection=True)

            if len(selection) < 2:
                cmds.warning("Please select source and target rigs!")
                return

            if len(namespaces) < 2:
                cmds.warning("Please select more than 1 rig with different namespaces!")
                return

            source_namespace = namespaces[0]
            target_namespaces = namespaces[1:]

            pose_dict = get_pose_dict(source_namespace)

            if not pose_dict:
                cmds.warning("No animatable attributes found in the source rig!")
                return

            for target in target_namespaces:
                apply_pose(pose_dict, target)



        def get_selected_namespaces():
            """Get list of namespaces for selected rigs."""
            selection = cmds.ls(selection=True)
            if len(selection) == 0:
                return []

            namespace_list = []
            for ctrl in selection:
                namespace = ctrl.split(":")[0]
                if namespace not in namespace_list:
                    namespace_list.append(namespace)
            return namespace_list

        def get_attrs_from_node(ctrl_node):
            """Get attribute names from node."""
            attributes = cmds.listAnimatable(ctrl_node)
            if not attributes:
                return []

            attr_names = []
            for full_attr in attributes:
                attr_name = full_attr.split(".")[-1]
                attr_names.append(attr_name)

            return attr_names

        def get_pose_dict(namespace):
            """Get the pose dictionary without namespaces."""
            selection = cmds.ls(selection=True)
            if not selection:
                return {}

            pose_dict = {}
            for ctrl in selection:
                if ctrl.startswith(namespace):
                    animatable_attrs = get_attrs_from_node(ctrl)
                    if not animatable_attrs:
                        continue

                    for attr in animatable_attrs:
                        attr_value = cmds.getAttr("{}.{}".format(ctrl, attr))
                        ctrl_name = ctrl.split(":")[-1]
                        full_attr = "{}.{}".format(ctrl_name, attr)
                        pose_dict[full_attr] = attr_value

            print("Pose dictionary:", pose_dict)  # Debugging output
            return pose_dict

        def apply_pose(pose_dict, namespace):
            """Apply provided pose to provided namespace."""
            for attr_name in pose_dict.keys():
                # need to add namespace
                attr_value = pose_dict[attr_name]
                ctrl_name = '{}:{}'.format(namespace, attr_name)

                node, attr_short_name = ctrl_name.split('.')
                # attribute checks
                if not cmds.objExists(node) or not cmds.attributeQuery(attr_short_name, node=node,
                                                                       exists=True) or not cmds.getAttr(ctrl_name,
                                                                                                        settable=True):
                    continue
                # set attribute
                cmds.setAttr(ctrl_name, attr_value)

        transfer_selected()


    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.widget.resize(self.width(), self.height())
        
    def closeWindow(self):
        """
        Close window.
        """
        print ('closing window')
        self.destroy()
    
def openWindow():
    """
    ID Maya and attach tool window.
    """
    # Maya uses this so it should always return True
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in (QtWidgets.QApplication.allWindows()):
            if 'myToolWindowName' in win.objectName(): # update this name to match name below
                win.destroy()

    #QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    MayaUITemplate.window = MayaUITemplate(parent = mayaMainWindow)
    MayaUITemplate.window.setObjectName('myToolWindowName') # code above uses this to ID any existing windows
    MayaUITemplate.window.setWindowTitle('Maya UI Template')
    MayaUITemplate.window.show()
    
openWindow()