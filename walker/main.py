#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def execute_command(repo):
    os.chdir(repo)
    command = sys.argv[1:]
    try:
        subprocess.check_call(command)
    except Exception as e:
        print "ERROR in %s: %s" % (repo, e)

def main():
    base = os.getcwdu() + "/"
    repositories = None

    # Get immediate child directories.
    for root, dirs, files in os.walk('.'):
        repositories = dirs
        break

    # Traverse through the directories.
    for repo in sorted(repositories, key=lambda s: s.lower()):
        repo_full_path = base + repo
        execute_command(repo_full_path)
        os.chdir(base)

if __name__ == '__main__':
    main()
