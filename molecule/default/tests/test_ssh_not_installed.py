import os

import testinfra.utils.ansible_runner

# Test if any ssh packages are installed

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_not_installed(host):
    full_package_list = host.run('dpkg --get-selections').stdout
    ssh_package_list = []
    for package_line in full_package_list.split('\n'):
        eline = package_line.encode('utf-8')
        if 'ssh' in eline:
            ssh_package_list.append(eline)
    assert ssh_package_list == []
