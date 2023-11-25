# Using Puppet to install flask from pip3.
# Task 1
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
