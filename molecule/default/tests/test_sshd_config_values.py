import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_config(host):
    assert host.file('/etc/ssh/sshd_config.d/ansible.conf').exists
    assert host.file('/etc/ssh/sshd_config.d/ansible.conf').contains('HostbasedAuthentication no')
