# puppet script to create ssh config file
file_line {'Turn off paswd auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    passwordAuthentication no',
}

file_line { 'Declare identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    identifyFile ~/.ssh/school',
}
