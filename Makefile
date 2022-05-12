
install : 
	@pip install psutil 
	@pip install termcolor
	@pip install progress

clean : 
	@rm -f minitel/connexion/sudo.txt 
	@touch minitel/connexion/sudo.txt
	@chmod +rw minitel/connexion/sudo.txt
