#!/usr/bin/python3

import subprocess

def making_universal_git_in_python():
	git_cmd=input("Hello Tas, what git command do you want to use today?\n")
	#Then I just stole: 
	#https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
	#:D
	process = subprocess.Popen(git_cmd.split(), stdout=subprocess.PIPE)

making_universal_git_in_python()
