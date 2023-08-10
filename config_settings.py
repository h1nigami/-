import configparser

class Config:
    def __init__(self, config_file) -> None:
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self.read_config()
    
    def read_config(self):
        self.config.read(self.config_file)
        self.packet_format = self.config['settings']['packet_format']
        
config = Config('config.ini')


