exec { 'fix_nginx':
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
  command => 'echo ULIMIT=\" -n 4096\" >> /etc/default/nginx',
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
