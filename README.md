# Ansible Role SSH

This role installs and configures SSH server and client.

# Example Play

```yaml
- hosts: foo
  roles:
    - blunix.role-ssh
  vars:
    ssh_enabled: yes

    # Setup asking ldap
    ssh_use_ldap: yes

    # sshd_config
    ssh_sshd_config_port: 22
    ssh_sshd_config_protocol_version: 2
    ssh_sshd_config_host_keys:
      - /etc/ssh/ssh_host_rsa_key
      - /etc/ssh/ssh_host_ecdsa_key
      - /etc/ssh/ssh_host_ed25519_key
    ssh_sshd_config_use_privilege_separation: 'yes'
    ssh_sshd_config_syslog_facility: AUTH
    ssh_sshd_config_login_grace_time: 120
    ssh_sshd_config_ignore_rhosts: 'yes'
    ssh_sshd_config_host_based_authentication: 'no'
    ssh_sshd_config_challenge_response_authentication: 'no'
    ssh_sshd_config_use_pam: 'yes'
    ssh_sshd_config_use_dns: 'no'
    ssh_sshd_config_authorized_keys_command: /etc/ssh/authorized_keys_command
    ssh_sshd_config_authorized_keys_command_user: nobody

    # Secured settings below
    ssh_sshd_config_log_level: INFO
    ssh_sshd_config_permit_root_login: prohibit-password
    ssh_sshd_config_strict_mode: 'yes'
    ssh_sshd_config_allow_agent_forwarding: 'no'
    ssh_sshd_gateway_ports: 'no'
    ssh_sshd_x11_forwarding: 'no'
    ssh_sshd_config_permit_tunnel: 'no'

    # Explicitly state users and groups who have permission to login.
    ssh_sshd_config_allow_users: 'root'
    ssh_sshd_config_allow_groups: 'root'

    # Cipher Settings
    # shamelessly copied from https://wiki.mozilla.org/Security/Guidelines/OpenSSH#Modern_.28OpenSSH_6.7.2B.29
    # see also: bettercrypto.org
    ssh_sshd_config_kex_algorithms: 'curve25519-sha256@libssh.org,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256'
    ssh_sshd_config_ciphers: 'chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr'
    ssh_sshd_config_macs: 'hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com'
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
