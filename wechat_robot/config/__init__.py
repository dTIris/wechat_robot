# -*- coding:utf-8 -*-

TOKEN = "o44odc6A3wjetIv8DlVh3cMiu0hF"
APPID = "wx1f0043387c3de18d"
APP_SECRET = "7aee91fa5b6dd8b033ff24e873cfa426"
ENCODING_AES_KEY = "CW8WweiAvQcGnYtkjF9sERXybvhTcyPQnPJONuHyMQS"
ENCRYPT_MODE = "normal"

DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": 'localhost',
                "port": 3306,
                "user": 'myread',
                "password": 'Read@123456',
                "database": 'wx_public_accounts',
                "maxsize": 3
            }
        }
    },
    "apps": {
        "wechat": {
            "models": ["wechat_robot.models"],
            "default_connection": "default"
        }
    }
}

REDIS_SETTINGS = {
    "default": {
        "host": "localhost",
        "port": 6379,
        "db": 0,
        "password": "my@redis123",
        "minsize": 1,
        "maxsize": 3,
        "timeout": 33
    },
    "other": {
        "host": "localhost",
        "port": 6379,
        "db": 1,
        "password": "my@redis123",
        "minsize": 1,
        "maxsize": 3,
        "timeout": 3
    }
}