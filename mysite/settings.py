import os

# 项目根目录的路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 安全密钥，用于加密数据
SECRET_KEY = 'django-insecure-!y^g#z3j$q7x9+v)c@r2&f4b(t6w0m8a5n1p3l7k9d4s2f0g5h'

# 调试模式，开发环境设为True
DEBUG = True

# 允许访问的主机
ALLOWED_HOSTS = []

# 安装的应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 中间件配置
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根URL配置
ROOT_URLCONF = 'mysite.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI应用路径
WSGI_APPLICATION = 'mysite.wsgi.application'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 密码验证器
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

# 语言设置
LANGUAGE_CODE = 'zh-hans'

# 时区设置
TIME_ZONE = 'Asia/Shanghai'

# 是否使用国际时间
USE_I18N = True

# 是否使用本地化时间
USE_TZ = True

# 静态文件路径
STATIC_URL = '/static/'