#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("PhpStorm-181.4203.565/jre64")
    pisitools.insinto("/opt/phpstorm", "PhpStorm-181.4203.565/*")
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
