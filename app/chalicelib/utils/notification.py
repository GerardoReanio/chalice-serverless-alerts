from discord_webhook import DiscordWebhook

def notification_discord(discord_webhook_url, rmtavg):
    
    webhook = DiscordWebhook(url=discord_webhook_url, 
                rate_limit_retry=True,
                content='@everyone Se detecta una degradación del servicio MATRIX  - RTMAVG: {}'.format(rmtavg))
    response = webhook.execute()
    print(response)


def notification_slack():
    pass

def notification_email():
    pass