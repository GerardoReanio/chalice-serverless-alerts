# -*- coding: utf-8 -*-
import os

def get_config_env():
    config = {
        'RATE_MINUTE': os.getenv('RATE_MINUTE'),
        'DISCORD_WEBHOOK_URL': os.getenv('DISCORD_WEBHOOK_URL'),
        'DEGRADATION_THRESHOLD': os.getenv('DEGRADATION_THRESHOLD')
    }
    return config