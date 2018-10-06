import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

SSH_LDAP_BINDPW = "ldap"


def test_secret_file(host):
    f = host.file("/etc/ssh/ssh.secret")

    assert f.exists
    assert f.contains(SSH_LDAP_BINDPW)
    assert f.user == "nobody"
    assert f.group == "root"
    assert f.mode == 0640
