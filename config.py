import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("20114039"))
    API_HASH = os.environ.get("87297b8f3cc8fc9bbce591ad30da5896")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int(8172163893) for user_id in VIP_USER]
