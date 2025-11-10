# -*- mode: python ; coding: utf-8 -*-
import os


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'pytest', 'scipy', 'matplotlib', 'notebook', 'jupyter', 'IPython', 'PyQt5', 'wx', 'PySide2', 'PySide6.QtPdf', 'PySide6.QtQml', 'PySide6.QtQuick', 'PySide6.QtVirtualKeyboard', 'PySide6.QtSvg', 'PySide6.QtOpenGL', 'pandas.tests', 'numpy.tests', 'PySide6.QtWebEngineCore', 'PySide6.QtWebEngineWidgets'],
    noarchive=False,
    optimize=0,
)

# Aggressively remove unused files to reduce size
files_to_remove = [
    'Qt6Pdf.dll',
    'Qt6Qml.dll',
    'Qt6Quick.dll',
    'Qt6VirtualKeyboard.dll',
    'Qt6Svg.dll',
    'Qt6OpenGL.dll',
    'opengl32sw.dll',
    'selenium-manager', # Linux and macOS binaries
]

# Filter binaries (tuple is (name, path, typecode))
a.binaries = [x for x in a.binaries if os.path.basename(x[1]) not in files_to_remove]

# Filter datas (selenium-manager might be here too)
a.datas = [x for x in a.datas if not any(x[0].endswith(rem) for rem in files_to_remove)]


# Remove Qt translations to reduce size
for i in range(len(a.datas) - 1, -1, -1):
    if a.datas[i][1].startswith('PySide6/translations'):
        a.datas.pop(i)

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