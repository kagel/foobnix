#!/bin/bash
if [ "$(whoami)" != "root" ]; then
	echo "Sorry, you are not root. try 'sudo uninstall.sh'"
	exit 1
fi

sudo make uninstall
