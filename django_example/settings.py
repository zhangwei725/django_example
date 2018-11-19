import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '%t4yz+t*$yfqn)#zl6t6(xnk*ur7yy3_vhlwl4=5k939f4uls*'

DEBUG = True

ALLOWED_HOSTS = []
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXT_APPS = ['dj_pagination', ]

CUSTOMER_APPS = [
    'main',
    'pagination',
    'reverse_ex',
]

INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOMER_APPS

MIDDLEWARE = [
    'dj_pagination.middleware.PaginationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_example.wsgi.application'

MYSQL_OPTIONS = {
    # 使用严格模式TRADITIONAL插入数据
    'sql_mode': 'TRADITIONAL',
    'charset': 'utf8',
    # 'init_command': """
    # SET default_storage_engine=INNODB;
    # SET character_set_connection=utf8,collation_connection=utf8_unicode_ci;
    # SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
    # """
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_example',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '112.74.32.121',
        'PORT': '3306',
        'OPTIONS': MYSQL_OPTIONS,
        # 设置数据库交互方式为事务
        'ATOMIC_REQUESTS': True,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

# 静态文件配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/pagination/static'),
)

# ==========logging日志配置==========

import logging
import django.utils.log
import logging.handlers

BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
ALL_LOG = os.path.join(BASE_LOG_DIR, "all.log")
ERROR_LOG = os.path.join(BASE_LOG_DIR, "error.log")
SCRIPT_LOG = os.path.join(BASE_LOG_DIR, "script.log")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 标准的日志格式
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%('
                      'levelname)s]- %(message)s'},
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },

    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ALL_LOG,  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ERROR_LOG,
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': SCRIPT_LOG,
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },

    },
    'loggers': {
        # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },

        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# ======== 分页配置=========
PAGINATION_DEFAULT_PAGINATION = 10
PAGINATION_PREVIOUS_LINK_DECORATOR = ''
PAGINATION_NEXT_LINK_DECORATOR = ''
PAGINATION_DEFAULT_WINDOW = 5
