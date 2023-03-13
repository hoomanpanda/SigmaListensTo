# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['slt.py'],
             pathex=['slt.py'],
             binaries=[],
             datas=[('SigmaListens.mp4', '.')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='slt',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          upx_include=[],
          console=True )

app = BUNDLE(exe,
             name='Sigma Listens To',
             icon=None,
             bundle_identifier=None,
             info_plist=None,
             debug=False,
             standalone=True,
             )

