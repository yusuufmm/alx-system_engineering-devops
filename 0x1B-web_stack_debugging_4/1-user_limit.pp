# This Puppet manifest changes the OS configuration to replace the username "holberton" with "foo" in the /etc/security/limits.conf file
# holberton user and open a file without getting any error message.
exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
