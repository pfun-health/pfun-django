import os

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'USERNAME': 'some-user',
        'PASSWORD': 'some-password',
        'DEFAULT_TIMEOUT': 360,
        'DEFAULT_RESULT_TTL': 800,
        'REDIS_CLIENT_KWARGS': {    # Eventual additional Redis connection arguments
            # 'ssl_cert_reqs': None,
        },
    },
    'with-sentinel': {
        'SENTINELS': [('localhost', 26736), ('localhost', 26737)],
        'MASTER_NAME': 'redismaster',
        'DB': 0,
        # Redis username/password
        'USERNAME': 'redis-user',
        'PASSWORD': 'secret',
        'SOCKET_TIMEOUT': 0.3,
        'CONNECTION_KWARGS': {  # Eventual additional Redis connection arguments
            'ssl': True
        },
        'SENTINEL_KWARGS': {    # Eventual Sentinel connection arguments
            # If Sentinel also has auth, username/password can be passed here
            'username': 'sentinel-user',
            'password': 'secret',
        },
    },
    'high': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'), # If you're on Heroku
        'DEFAULT_TIMEOUT': 500,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    }
}

# RQ_EXCEPTION_HANDLERS = ['path.to.my.handler'] # If you need custom exception handlers
