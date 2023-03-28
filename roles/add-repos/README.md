Add repo
=========

A role that can add repositories to the system using 'apt' package manager.

Role Variables
--------------

repos: one or more URL's that point to the repos.

Example Playbook
----------------

- hosts: servers
  vars:
    keys:
      - https://example.com/repo stable main
      - https://test.com/test bullseye main
  roles:
    - role: add-repos

License
-------

BSD

Author Information
------------------

Made by Van Loon Bernd
