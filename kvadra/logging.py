# coding=utf-8
import os

imf_log = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
) + '/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'my_conf': {
            'format': '%(asctime)s %(levelname)s  %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
            # 'filters': ['special']
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': imf_log + 'filelog.log',
            'formatter': 'my_conf'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'kvadra': {
            'handlers': ['console', 'logfile', 'mail_admins'],
            'level': 'INFO',
            # 'filters': ['special']
        },
        # 'mon.management.commands.monitoring': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_dsi': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_query': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_partitions': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_cleaner': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.lost_delay': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_preference': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_warmstandby': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_restartdsi': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.bot_telegramm': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_repagent_statistic': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'mon.management.commands.mon_repinstance': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        #
        # 'mon.management.commands.bothandler': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'utils.workdb': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'utils.worklogrs': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'ERROR',
        #     'propagate': True,
        # },
        # 'utils.worklogrs_noparamiko': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'INFO',
        #     'propagate': True,
        # },
        # 'mon.views': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'graph.views': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'logrs.views': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'delay.views': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'warm.views': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'incident.workalert': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'utils.client_pubsub': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'utils.logsegment': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'utils.repagent_dsi_params': {
        #     'handlers': ['logfile', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'django_auth_ldap': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        #     'propagate': True,
        # },
    }
}

