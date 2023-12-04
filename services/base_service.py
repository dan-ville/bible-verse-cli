import configparser
from pathlib import Path

class BaseService:
    def __init__(self, config_file_name):
        self.config_file = Path.home() / config_file_name
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get_config(self, service, key):
        if not self.config.has_section(service):
            if not self.config.has_section('DEFAULT'):
                self.config['DEFAULT'] = {}
            self.config[service] = self.config['DEFAULT']

        if key not in self.config[service]:
            value = input(f"Enter your {service} {key}: ")
            self.config[service][key] = value
            with open(self.config_file, 'w') as f:
                self.config.write(f)
        else:
            value = self.config[service][key]

        return value
