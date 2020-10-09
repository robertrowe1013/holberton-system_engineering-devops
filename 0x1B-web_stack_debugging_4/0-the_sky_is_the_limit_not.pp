#!/usr/bin/env bash
# fixinx nginx
exec { 'fix_nginx':
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
  command => "sed -i '5c ULIMIT=\"-n 4096\"'"
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
