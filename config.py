class DevelopmentConfig():
    DEBUG = True
    MYSQL_GOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'api_flask'

config = {
    'development': DevelopmentConfig
}
