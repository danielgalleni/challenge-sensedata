# coding=utf-8
class Config(object):
    """
    Configurações comuns
    """

    # Aqui devem ser inseridas configurações comuns em todos os ambientes,
    # seja producao ou desenvolvimento
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Configuracão de desenvolvimento
    """

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Configuração de produção
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Configuração de teste
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}