import sys, os
from conf import MyLogSettings

import logging

BASE_DI_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#  sys.path.append(BASE_DI_R)


if __name__ == '__main__':
    MyLogSettings.load_my_logging_cfg()
    curLogger = logging.getLogger(__name__)
    # 输出项目路径
    curLogger.error(BASE_DI_R)
