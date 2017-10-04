import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_config(File):
    f = File('/etc/ssh/sshd_config')

    assert f.exists
    assert f.contains('ListenAddress 0.0.0.0')
    assert f.contains('Protocol 2')
    assert f.contains('UsePrivilegeSeparation yes')
    assert f.contains('ServerKeyBits 1024')
    assert f.contains('LogLevel INFO')
    assert f.contains('LoginGraceTime 120')
    assert f.contains('PermitRootLogin without-password')
    assert f.contains('StrictModes yes')
    assert f.contains('PubkeyAuthentication yes')
    assert f.contains('IgnoreRhosts yes')
    assert f.contains('RhostsRSAAuthentication no')
    assert f.contains('HostbasedAuthentication no')
    assert f.contains('PermitEmptyPasswords no')
    assert f.contains('ChallengeResponseAuthentication no')
    assert f.contains('PasswordAuthentication no')
    assert f.contains('X11Forwarding yes')
    assert f.contains('X11DisplayOffset 10')
    assert f.contains('PrintMotd no')
    assert f.contains('PrintLastLog yes')
    assert f.contains('TCPKeepAlive yes')
    assert f.contains('UsePAM yes')
    assert f.contains('UseDNS no')
