"""
Maya/QT UI template
Maya 2023
"""

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
import sys
import os

class MayaUITemplate(QtWidgets.QWidget):
    """
    Create a default tool window.
    """
    window = None
    
    def __init__(self, parent=None):
        """
        Initialize class.
        """
        super(MayaUITemplate, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.widgetPath = r'C:\Users\uhata\Documents\Proxy_UI\MakeProxy.ui'
        print(f"Widget Path: {self.widgetPath}")  # Debug print

        if not os.path.exists(self.widgetPath):
            raise FileNotFoundError(f"The specified UI file does not exist: {self.widgetPath}")

        try:
            self.widget = QtUiTools.QUiLoader().load(self.widgetPath)
        except Exception as e:
            print(f"Error loading UI file: {e}")
            raise

        self.widget.setParent(self)
        # set initial window size
        self.resize(200, 100)
        # locate UI widgets
        self.btn_makeproxy = self.widget.findChild(QtWidgets.QPushButton, 'makeproxy_btn')
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'close_btn')
        self.radio_sphere = self.widget.findChild(QtWidgets.QRadioButton, 'radiobtn_sphere')
        self.radio_trap = self.widget.findChild(QtWidgets.QRadioButton, 'radiobtn_trap')
        
        # Debug statements to confirm the widgets are found
        print(f"btn_makeproxy: {self.btn_makeproxy}")
        print(f"btn_close: {self.btn_close}")
        print(f"radio_sphere: {self.radio_sphere}")
        print(f"radio_trap: {self.radio_trap}")

        # assign functionality to buttons
        self.btn_makeproxy.clicked.connect(self.on_makeproxy)
        self.btn_close.clicked.connect(self.close)

    def on_makeproxy(self):
        """
        Handle make proxy button click.
        """
        if self.radio_sphere and self.radio_sphere.isChecked():
            print("Sphere radio button is checked")  # Debug print
            self.sphere_rig()
        elif self.radio_trap and self.radio_trap.isChecked():
            print("Trap radio button is checked")  # Debug print
            self.trap_rig()
        else:
            print("No proxy type selected")  # Debug print
            cmds.warning("Please select a proxy type.")

    def sphere_rig(self):
        """
        Load sphere rig.
        """
        print("Loading sphere rig")  # Debug print
        cmds.file(r"C:\Users\uhata\OneDrive\Documents\maya\projects\proxy_rig\scenes\SphereProxy.mb", reference=True)

    def trap_rig(self):
        """
        Load trap rig.
        """
        print("Loading trap rig")  # Debug print
        cmds.file(r"C:\Users\uhata\OneDrive\Documents\maya\projects\proxy_rig\scenes\TrapProxy.mb", reference=True)

    def resizeEvent(self, event):
        """
        Called on automatically generated resize event.
        """
        self.widget.resize(self.width(), self.height())

    def closeWindow(self):
        """
        Close window.
        """
        print('closing window')
        self.destroy()

def openWindow():
    """
    ID Maya and attach tool window.
    """
    # Maya uses this so it should always return True
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QtWidgets.QApplication.allWindows():
            if 'myToolWindowName' in win.objectName():  # update this name to match name below
                win.destroy()

    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    MayaUITemplate.window = MayaUITemplate(parent=mayaMainWindow)
    MayaUITemplate.window.setObjectName('myToolWindowName')  # code above uses this to ID any existing windows
    MayaUITemplate.window.setWindowTitle('Maya UI Template')
    MayaUITemplate.window.show()

# Execute the script
openWindow()
