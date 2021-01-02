#  coding: utf-8 

from cx_Freeze import setup, Executable


includes=[
    'blocks',
    'fire',
    'monster',
    'pyganim',
    'slime'
]
include_files = ['animation',
                 'image',
                 'music',
                 'sounds',
                 'C:/Users/Степан\AppData/Local/Programs/Python/Python39/python39.dll'
]
excludes = [ 'email', 'html', 'http'

]
options = {
    'build_exe':{
    'include_msvcr': True,
    'excludes':excludes,
    'includes':includes,
    'include_files':include_files,
    }
}

setup(
    name='game_py',
    version='0.0.1',
    description='Slime',
    options=options,
    executables=[Executable('game.py',targetName='Slime-s_castle')]
)
