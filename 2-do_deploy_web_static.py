#!/usr/bin/python3
"""
distributes an archive to your web servers
"""
from fabric.api import *
from os.path import exists


env.hosts = ['18.204.3.147', '3.84.158.72']
def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if(exists(archive_path) is False):
        return False
    try:
        put(f"{archive_path}", "/tmp/")
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        remote_path = f"/data/web_static/releases/{folder_name}"
        sudo(f"mkdir -p {remote_path}")
        sudo(f"tar -xzf /tmp/{archive_name} -C {remote_path}")
        sudo(f"mv {remote_path}/web_static/* {remote_path}")
        sudo(f"rm -rf {remote_path}/web_static")
        sudo(f"rm /tmp/{archive_name}")
        sudo(f"rm -rf /data/web_static/current")
        sudo(f"ln -s /data/web_static/current {remote_path}")

    except:
        return False
