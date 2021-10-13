.PHONY: install
install:
	pip3 install -r requirements.txt
	cp mastodon_bot.service /etc/systemd/system/mastodon_bot.service
	systemctl daemon-reload

.PHONY: restart
restart:
	systemctl restart mastodon_bot.service

.PHONY: status
status:
	systemctl status mastodon_bot.service

.PHONY: stop
stop:
	systemctl stop mastodon_bot.service

.PHONY: start
start:
        systemctl start mastodon_bot.service