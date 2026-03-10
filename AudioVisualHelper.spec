# -*- mode: python ; coding: utf-8 -*-

# code in this section has elements taken from kivywhisper under MIT license, see licenses.md for license
from PyInstaller.utils.hooks import copy_metadata

datas = []
datas += copy_metadata('openai-whisper', recursive=True)

import sys, pathlib
dataspath = pathlib.Path(sys.executable) 

basevenv = pathlib.PurePath(*pathlib.Path(sys.executable).parts[:-2])
filterspath = pathlib.PurePath(basevenv, "Lib", "site-packages", "whisper", "assets", "mel_filters.npz")
filterspath2 = pathlib.PurePath(basevenv, "Lib", "site-packages", "whisper", "assets", "multilingual.tiktoken")
datas += [(filterspath, 'whisper\\assets'), (filterspath2, 'whisper\\assets'),('./icon/icon.ico', 'icon'), ('licenses.md', '.')]
# end used code section section

a = Analysis(
    ['src\\app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    exclude_binaries=True,
    name='AudioVisual Helper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AudioVisual Helper',
)
