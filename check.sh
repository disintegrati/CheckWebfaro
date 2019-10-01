if nmap -p 22901 1.tcp.eu.ngrok.io | grep open; then
	printf "Tutto ok"
else
	/usr/bin/python messaggio.py
	sudo killall node
fi
exit 1
