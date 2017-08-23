#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("PhpStorm-172.3544.41/jre64")
    pisitools.insinto("/opt/phpstorm", "PhpStorm-172.3544.41/*")
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
