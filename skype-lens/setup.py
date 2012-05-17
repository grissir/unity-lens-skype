#!/usr/bin/env python
#
from distutils.core import setup
from DistUtilsExtra.command import *

setup(name="unity-lens-skype",
      version="0.1",
      author="Christian Rupp",
      author_email="christian@r-k-r.de",
      url="",
      license="GNU General Public License (GPL)",
      data_files=[
    ('lib/unity-lens-skype', ['src/unity-lens-skype']),
    ('share/dbus-1/services', ['unity-lens-skype.service']),
    ('share/unity/lenses/skype', ['skype.lens']),
    ('share/unity/lenses/skype', ['data/skype-wrapper.svg']),
    ], cmdclass={"build":  build_extra.build_extra, })

