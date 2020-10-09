#!/usr/bin/env bash
# fix nginx
exec { 'fix_nginx':
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
  command => "sed -i '5c ULIMIT=\"-n 4096\"' /etc/default/nginx"
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
