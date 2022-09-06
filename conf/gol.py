# -*- coding: utf-8 -*-
import logging

golLog = logging.getLogger(__name__)


def _init():  # 初始化
    global _global_dict
    _global_dict = {}


def setValue(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def getValue(key):
    '''
        获得一个全局变量,不存在则返回默认值
    '''
    try:
        return _global_dict[key]
    except KeyError as e:
        err = "key:{} not found!{}".format(key, e)
        golLog.exception(err)
        raise Exception(err)


def getValueFromConfig(section, key):
    if len(_global_dict) == 0 or _global_dict['config'] is None:
        raise Exception("获取全局config配置文件为空")
    config = _global_dict['config']
    return config.get_value_from_section_key(section, key)
