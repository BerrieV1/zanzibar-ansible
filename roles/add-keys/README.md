Add keys
=========

A role that can add repository keys using 'apt' package manager.

Role Variables
--------------

keys: one or more URL's that contain the keys.

Example Playbook
----------------

- hosts: servers
  vars:
    keys:
      - https://example.com/keys
      - https://test.com/signing-key
  roles:
    - role: add-keys

License
-------

BSD

Author Information
------------------

Made by Van Loon Bernd
