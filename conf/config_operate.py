# coding = utf-8

from configparser import ConfigParser



class Config_operate(ConfigParser):

    def __init__(self, config_path):
        self.config = self.__init_config_operate(config_path)

    # 静态方法
    def __init_config_operate(self, config_path):
        config = ConfigParser()
        config.read(config_path, encoding='utf-8')
        return config

    def get_value_from_section_key(self, section, key):
        # config = Config_operate.init_config_operate()
        value = self.config.get(section, key)
        # config.clear()
        return value
