import sys, os
from conf import MyLogSettings, gol
import logging
from conf.settings import config_path

from conf.config_operate import Config_operate

BASE_DI_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#  sys.path.append(BASE_DI_R)


if __name__ == '__main__':
    # init 日志配置
    MyLogSettings.load_my_logging_cfg()
    curLogger = logging.getLogger(__name__)
    # 输出项目路径
    curLogger.error(BASE_DI_R)
    # 全局变量
    gol._init()
    ## 全局变量 配置文件赋值
    config = Config_operate(config_path)
    gol.setValue("config", config)
    ## 测试配置文件中信息
    socks_proxy_host = gol.getValueFromConfig("proxy", "socks_proxy_host")
    ## 输出日志信息
    curLogger.info(socks_proxy_host)
