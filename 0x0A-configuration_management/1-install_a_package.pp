# Using Puppet to install flask from pip3.
# Ensure pip3 is installed
    package { 'python3-pip'
    ensure => 'installed',
}
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],

}
