# -*- mode: python ; coding: utf-8 -*-
import os

# Modules to exclude from the build to reduce size.
EXCLUDES = [
    'tkinter', 'pytest', 'scipy', 'matplotlib', 'notebook', 'jupyter', 'IPython', 
    'PyQt5', 'wx', 'PySide2', 
    'PySide6.QtPdf', 'PySide6.QtQml', 'PySide6.QtQuick', 'PySide6.QtVirtualKeyboard', 
    'PySide6.QtSvg', 'PySide6.QtOpenGL', 'PySide6.QtWebEngineCore', 'PySide6.QtWebEngineWidgets',
    'PySide6.translations', # Exclude all translation files
    'pandas.tests', 'numpy.tests'
]

# Specific DLLs and files to remove from the collected binaries and datas.
FILES_TO_REMOVE = [
    # Unused Qt6 DLLs
    'Qt6Pdf.dll',
    'Qt6Qml.dll',
    'Qt6Quick.dll',
    'Qt6VirtualKeyboard.dll',
    'Qt6Svg.dll',
    'Qt6OpenGL.dll',
    'opengl32sw.dll',

    # Unused Qt6 plugins
    # Image formats (keeping only jpeg, and svg for icons)
    'qgif.dll',
    'qicns.dll',
    'qico.dll',
    'qpdf.dll',
    'qtga.dll',
    'qtiff.dll',
    'qwbmp.dll',
    'qwebp.dll',
    # Styles
    'qmodernwindowsstyle.dll',
    # Input contexts
    'qtvirtualkeyboardplugin.dll',
    'qtuiotouchplugin.dll',
    # Platforms (qwindows.dll is essential)
    'qdirect2d.dll',
    'qminimal.dll',
    'qoffscreen.dll',
    
    # Other
    'selenium-manager', # Helper for chromedriver, not needed in final bundle
]


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    noarchive=False,
    optimize=0,
)

# Filter binaries based on the files_to_remove list
# PyInstaller collects tuples of (destination_name, source_path, typecode)
a.binaries = [x for x in a.binaries if os.path.basename(x[1]) not in FILES_TO_REMOVE]

# Filter data files as well
a.datas = [x for x in a.datas if os.path.basename(x[0]) not in FILES_TO_REMOVE]


pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mysafetyreport',
    debug=False,
    bootloader_ignore_signals=False,
    onefile=True,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)