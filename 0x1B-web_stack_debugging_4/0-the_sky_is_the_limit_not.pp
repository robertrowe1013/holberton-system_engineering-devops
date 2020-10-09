# fix nginx
exec { 'fix_nginx':
  command => "sed -i '5c ULIMIT=\"-n 4096\"' /etc/default/nginx",
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/']
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
