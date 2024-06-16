# src/logging_config.py
import logging
import logging.handlers
import time

class LoggerSetup():

    def __init__(self):
        # Pega a instância do logger
        self.logger = logging.getLogger('')
        # Invoca o método que configura o logger
        self.setup_logging()

    def setup_logging(self):
        # Adiciona um formatador para o logger - utilizando a sintaxe de JSON
        LOG_FORMAT = '{"time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": "%(message)s"}'
        # Setando o nível do log para INFO.
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

        # Adiciona o formatador ao logger
        formatter = logging.Formatter(LOG_FORMAT)

        # Adiciona um handler para que os dados armazenados no logger também possam ser exibidos na tela
        console=logging.StreamHandler()
        # Adiciona o formatador para o handler definido
        console.setFormatter(formatter)

        # Adiciona um gerenciador de rotação para o logs. Esse comportamento faz com que o arquivo que está sendo criado para guardar os logs possa ser alterado de acordo com o tamanho do arquivo ou o tempo de criação. Também é possível definir a quantidade de arquivos anteriores de logs serão armazenados.
        log_file = "logs/app.log"
        # Mais informações sobre a classe: https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
        # Neste caso, estamos configurando nosso arquivo de log para ser rotacionado a cada 5 minutos, mantendo 3 arquivos anteriores.
        file = logging.handlers.TimedRotatingFileHandler(filename=log_file, when='m', interval=5, backupCount=3)
        file.setFormatter(formatter)

        # Com os dois handlers criados, adicionamos eles ao logger
        self.logger.addHandler(console)
        self.logger.addHandler(file)




