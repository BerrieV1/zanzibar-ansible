Content in file
=========

A role that takes input through a variable and puts it in a file.

Role Variables
--------------

destination_content: the file where the content is going to go.
file_content: the content that goes in the file.

Example Playbook
----------------

- hosts: servers
  vars:
    destination_content: /home/test.txt
    file_content: "This is a test!"
  roles:
    - role: content-in-file

License
-------

BSD

Author Information
------------------

Made by Van Loon Bernd
