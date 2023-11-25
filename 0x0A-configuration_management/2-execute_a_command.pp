# Using Puppet, create a manifest that kills a process named killmenow.
# Executes a bash command
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}

