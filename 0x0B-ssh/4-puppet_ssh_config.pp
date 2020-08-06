#!/usr/bin/env bash
# puppet config
# puppet set up
file_line { 'NoPassword':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line { 'Identify':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
