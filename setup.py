from setuptools import setup

APP = ['timer.py']
DATA_FILES = ['tink2.wav']
OPTIONS = {
    'iconfile': 'appstore.icns'
}

setup(
    app=APP,
    name='Timer-Stopwatch',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
