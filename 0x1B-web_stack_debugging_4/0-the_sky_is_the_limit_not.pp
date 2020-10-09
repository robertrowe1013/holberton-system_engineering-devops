# fix nginx
file {'/etc/default/nginx':
  ensure  => present,
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 4096"',
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart',
  path     => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
