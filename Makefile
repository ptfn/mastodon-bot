.PHONY: install
install:
	pip3 install -r requirements.txt
	cp mastodon_bot.service /etc/systemd/system/mastodon_bot.service
	systemctl daemon-reload

.PHONY: restart
restart:
	systemctl stop mastodon_bot.service
	systemctl start mastodon_bot.service

.PHONY: status
status:
	systemctl status mastodon_bot.service

.PHONY: stop
stop:
<<<<<<< HEAD
	systemctl stop mastodon_bot.service
=======
	systemctl stop mastodon_bot.service
>>>>>>> ff7042f3edf66a38afca981d4cf149221074e083
