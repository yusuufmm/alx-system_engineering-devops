#!/usr/bin/env bash
#using puppet script to create or make changes our ssh configuration file
file_line {'ect/ssh/ssh_config':
		ensure => present,
content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	".
}
