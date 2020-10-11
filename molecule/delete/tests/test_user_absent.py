import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_config(host):
    assert not host.file('/etc/passwd').contains('backuppc')
    assert not host.file('/etc/group').contains('backuppc')
