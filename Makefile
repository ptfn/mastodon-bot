.PHONY: install
install:
	pip3 install -r requirements.txt
	cp mastodon_bot.service /etc/systemd/system/mastodon_bot.service
	systemctl daemon-reload

.PHONY: restart
restart:
	systemctl stop mastodon_bot.service
	systemctl start mastodon_bot.service