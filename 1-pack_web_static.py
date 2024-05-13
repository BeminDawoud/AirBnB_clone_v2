#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    function to create the archive
    """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_path = f"versions/web_static{time}.tgz"
        local(f"tar -czvf {archive_path} web_static")
        return archive_path
    except:
        return None
