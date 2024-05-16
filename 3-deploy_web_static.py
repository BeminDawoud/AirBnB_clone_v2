#!/usr/bin/python3
"""
creates and distributes an archive to web servers
"""

from fabric.api import *
from datetime import datetime
from os.path import exists
env.hosts = ['18.204.3.147', '3.84.158.72']


def do_pack():
    """
    function to create the archive
    """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_path = f"versions/web_static_{time}.tgz"
        local(f"tar -czvf {archive_path} web_static")
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        put(f"{archive_path}", "/tmp/")
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        remote_path = f"/data/web_static/releases/{folder_name}"
        run(f"sudo mkdir -p {remote_path}")
        run(f"sudo tar -xzf /tmp/{archive_name} -C {remote_path}")
        run(f"sudo mv {remote_path}/web_static/* {remote_path}")
        run(f"sudo rm -rf {remote_path}/web_static")
        run(f"sudo rm /tmp/{archive_name}")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {remote_path} /data/web_static/current")
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    f_path = do_pack()
    if f_path is None:
        return False
    return do_deploy(f_path)
