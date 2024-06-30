"""
Maya/QT UI template
Maya 2023
"""

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial
import os
import sys

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
        self.widgetPath = r'C:\Users\uhata\OneDrive\Documents\maya\scripts\UIScripts\TemplateDesigner\TransformRig.ui'
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
        self.transformrig_btn = self.widget.findChild(QtWidgets.QPushButton, 'TransformRig_btn')
        # assign functionality to buttons
        self.transformrig_btn.clicked.connect(self.transformrig)
        #self.btn_close.clicked.connect(self.close)
    
    """
    Your code goes here
    """
        
    def transformrig(self):
      
        child_object_list = ['zelda_V001_008:Bip001_GLOBAL', 'link_V001_004:Bip001_GLOBAL' , 'ganon_V001_002    _file011:Bip001_GLOBAL']
        selected_objects = cmds.ls(selection=True)
        if selected_objects:
            parent_object = selected_objects[0]      
            # Query the world space transformation matrix of the parent object
            parent_transform = cmds.xform(parent_object, query=True, matrix=True, worldSpace=True)
            for child_obj in child_object_list:
                # Apply the same transformation matrix to zelda_V001_008:Bip001_GLOBAL
                cmds.xform(child_obj, matrix=parent_transform, worldSpace=True)       
        



    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
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
    
openWindow()
