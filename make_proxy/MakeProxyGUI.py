"""
This code is originally by isaacoster which I have modified to serve the purpose of this project
"""
import sys
from importlib import reload

# Add the Maya scripts directory to the system path
sys.path.insert(0, r"C:\Users\uhata\OneDrive\Documents\maya\projects\proxy_rig\UI\MayaUITemplate")

# Import and reload the MayaUITemplate module
try:
    import MayaUITemplate
    reload(MayaUITemplate)
    
    # Open the custom UI window
    MayaUITemplate.openWindow()
except ImportError as e:
    print(f"Failed to import MayaUITemplate: {e}")
except SyntaxError as e:
    print(f"Syntax error encountered: {e}")
