===============================
walker
===============================

.. image:: https://badge.fury.io/py/walker.png
    :target: http://badge.fury.io/py/walker

.. image:: https://travis-ci.org/darylyu/walker.png?branch=master
        :target: https://travis-ci.org/darylyu/walker

.. image:: https://pypip.in/d/walker/badge.png
        :target: https://pypi.python.org/pypi/walker


Walker executes the same command on multiple directories.

* Free software: BSD license
* Documentation: https://walker.readthedocs.org.

Usage
--------

Walker only gets the immediate children of the current directory.

Here is an example of it showing showing the status of different
git repositories: ::

    $ walker git status
    
    walker: in /home/dyu/src/couchdb-lucene
    # On branch master
    nothing to commit (working directory clean)
    
    walker: in /home/dyu/src/dotfiles
    # On branch master
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   gitignore_global
    #
    no changes added to commit (use "git add" and/or "git commit -a")
    
    walker: in /home/dyu/src/es
    fatal: Not a git repository (or any of the parent directories): .git

Here is another example of it showing disk usage: ::

    $ walker du -cksh

    walker: in /home/dyu/src/cookiecutter
    2.1M    .
    2.1M    total

    walker: in /home/dyu/src/couchdb-lucene
    145M    .
    145M    total

    walker: in /home/dyu/src/dotfiles
    588K    .
    588K    total

    walker: in /home/dyu/src/es
    245M    .
    245M    total
