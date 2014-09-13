#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def execute_command(target):
    os.chdir(target)
    command = sys.argv[1:]
    try:
        subprocess.check_call(command)
    except Exception as e:
        print "ERROR in %s: %s" % (target, e)

def main():
    base = os.getcwdu() + "/"
    targets = None

    # Get immediate child directories.
    for root, dirs, files in os.walk('.'):
        targets = dirs
        break  # dirty hack so we only get the first level

    # Traverse through the directories.
    for target in sorted(targets, key=lambda s: s.lower()):
        target_full_path = base + target
        print "\nwalker: in %s" % target_full_path
        execute_command(target_full_path)
        os.chdir(base)

if __name__ == '__main__':
    main()
