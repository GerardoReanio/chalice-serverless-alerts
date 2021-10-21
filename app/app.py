from chalice import Chalice, Rate

import logging

from chalicelib.utils.config import get_config_env
from chalicelib.utils.logs import get_response_time_merchantAvg
from chalicelib.utils.notification import notification_discord

app = Chalice(app_name='chalice-serverless-alerts')
app.log.setLevel(logging.DEBUG)

rate_minute = get_config_env().get('RATE_MINUTE')
discord_webhook_url = get_config_env().get('DISCORD_WEBHOOK_URL')
degradation_threshold = float(get_config_env().get('DEGRADATION_THRESHOLD'))

# Automatically runs every "rate_minute" minutes
@app.schedule(Rate(int(rate_minute), unit=Rate.MINUTES))
def get_rtmavg_task(event):
    rmtavg, tna  = get_response_time_merchantAvg(int(rate_minute))

    if rmtavg > degradation_threshold:
        notification_discord(discord_webhook_url, rmtavg)

    print('get_response_time_merchantAvg({}):{}|TotalNotificationsAnalized:{}'.format(rate_minute, rmtavg, tna ))
    
@app.route('/')
def index():
    
    rmtavg , tna = get_response_time_merchantAvg(int(rate_minute))
    print('get_response_time_merchantAvg({}):{}|TotalNotificationsAnalized:{}'.format(rate_minute, rmtavg, tna ))

    return {'Status': 'Ok', 
            'RMTAVG': rmtavg, 
            'Total Notifications Analized': tna,
            'Rate minute schedule' : rate_minute,
            'Degradation threshold': degradation_threshold }
