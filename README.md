# Ansible Role SSH

This role installs and configures SSH server and client.

# Example Play

```yaml
- hosts: foo
  roles:
    - blunix.role-ssh
  vars:
    ssh_enabled: yes
    ssh_sshd_config:
      AllowTcpForwarding: 'no'
      ClientAliveCountMax: 0
      ClientAliveInterval: 0
      HostbasedAuthentication: 'no'
      HostKey:
        #- /etc/ssh/ssh_host_dsa_key
        #- /etc/ssh/ssh_host_ecdsa_key
        - /etc/ssh/ssh_host_ed25519_key
        #- /etc/ssh/ssh_host_rsa_key
      IgnoreRhosts: 'yes'
      KeyRegenerationInterval: 3600
      LoginGraceTime: 60s
      LogLevel: INFO
      PasswordAuthentication: 'no'
      PermitEmptyPasswords: 'no'
      PermitRootLogin: 'prohibit-password'
      Port: 22
      PrintLastLog: 'yes'
      PrintMotd: 'no'
      Protocol: 2
      PubkeyAuthentication: 'yes'
      RhostsRSAAuthentication: 'no'
      RSAAuthentication: 'yes'
      ServerKeyBits: 1024
      StrictModes: 'yes'
      'Subsystem sftp': /usr/lib/openssh/sftp-server
      SyslogFacility: AUTH
      TCPKeepAlive: 'yes'
      UseDNS: 'no'
      UsePAM: 'no'
      GatewayPorts: 'no'
      PermitTunnel: 'no'
      UsePrivilegeSeparation: 'sandbox'
      X11DisplayOffset: 10
      X11Forwarding: 'no'
      AllowAgentForwarding: 'no'
      AllowUsers: 'root'
      AllowGroups: 'root'
      # Cipher settings from https://wiki.mozilla.org/Security/Guidelines/OpenSSH#Modern_.28OpenSSH_6.7.2B.29
      KexAlgorithms: 'curve25519-sha256@libssh.org,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256'
      Ciphers: 'chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr'
      MACs: 'hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com'
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
