pip3 install -r requirements.txt
cp mastodon_bot.service /etc/systemd/system/mastodon_bot.service
systemctl daemon-reload 