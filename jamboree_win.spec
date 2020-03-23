# -*- mode: python ; coding: utf-8 -*-
import sys
import os
import freetype
import glfw

block_cipher = None

data_files = [
    (os.path.dirname(freetype.__file__), os.path.join('freetype')),
    (os.path.dirname(glfw.__file__), os.path.join('glfw')),
    ('res/*.png', 'res/'), ('res/*.ttf', 'res/'),
]

a = Analysis(['jamboree.py'],
             pathex=['C:\\Users\\adf\\Documents\\python\\pyinstaller-test'],
             binaries=[],
             datas=data_files,
             hiddenimports=['pkg_resources.py2_warn', 'freetype', 'glcontext'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='jamboree',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='jamboree')
