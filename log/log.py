import logging

class LOG:
    def __init__(self, filename:str ='server.log', level=logging.DEBUG) -> None:
        # self.log = logging.basicConfig(filename=filename, level=level)
        # self.logs = {}
        self.log = None


    def Write(self, data: str) -> None:
        # Write data to log
        self.log.info(data)

    def Run(self, Destination: str):
        self.log = logging.getLogger("Destination")
        self.log.setLevel(logging.DEBUG)

    def registerHandlers(self):
        pass

    def write(self, message):
        self.log.info(message)
