Ansible Role SSH
================

This role installs and configures SSH server and client.

Example Play
============

```yaml
- hosts: foo
  vars:
    ssh_enabled: yes
  roles:
    - blunix.role-ssh
```

License
-------

Apache

Author Information
------------------

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
