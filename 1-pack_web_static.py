#!/usr/bin/python3
""" This is python script that will run
and pack the directory into the tar file
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """The function do_pack must return the archive path
    if the archive has been correctly generated.
    Otherwise, it should return None
    """
    if not os.path.exists(os.path.dirname("./web_static")):
        return None

    if not os.path.exists(os.path.dirname("versions")):
        try:
            local("mkdir -p versions")
        except Exception as e:
            print(e)
            return None
    file_name = "web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    local("echo {}".format(file_name))
    local("tar cpfz {} ./web_static".format(file_name))
    local("mv {f} versions/{f}".format(f=file_name))
    return "versions/{}".format(file_name)
