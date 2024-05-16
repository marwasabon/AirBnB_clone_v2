#!/usr/bin/python3
""" These methods aid in deploying the web_static directory
to the remote servers
"""
from fabric.api import *
import os
from datetime import datetime

env.hosts = ['54.237.44.169', '34.204.95.33']


def do_pack():
    """ Funciton to pack the web_static directory into a tar.gz
    for deployment to remote servers.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_static_{}.tgz".format(date)
    archive = local("tar -cvzf {} web_static".format(archived_path))

    if archive.succeeded:
        return archived_path
    else:
        return None


def do_deploy(archive_path):
    """ Function to deploy a compressed file
    then unpack and move the content to its destination

    Returns:
        Boolean : True on sucess well Fale
    """
    try:
        open(archive_path)
    except IOError:
        return False
    split_path = archive_path.split('/')
    cln_name = split_path[1][0:split_path[1].rfind('.')]
    dest = '/data/web_static'
    put(archive_path, "/tmp/")
    with cd("/tmp/"):
        run('tar xpf {}'.format(split_path[1]))
        run('mv web_static {}/releases/{}'.format(dest, cln_name))
        run('rm -rf {}'.format(split_path[1]))

    with cd(dest):
        run('rm {}/current'.format(dest))
        run('ln -s {d}/releases/{t} {d}/current'
            .format(d=dest, t=cln_name))
    print('New version deployed!')
    return True


def deploy():
    """ Function to pack and deploy
    """
    path = do_pack()
    print(path)
    if path:
        dp = do_deploy(path)
        return dp
    return False
