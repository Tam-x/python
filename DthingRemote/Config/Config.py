#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created by Tan.Xing
Created date: 2018/07/19
Last edited: 2018/07/20
'''


VERSION = '1.0.1'

CODE_MQTT_REMOTE = 0x01
CODE_MQTT_MONITOR = 0x02

MQTT_CLIENT = 'client-from-dthing-remote-desktop-tool'

MQTT_REMOTE_BROKER = '182.61.25.208'
MQTT_REMOTE_PORT = '1883'
MQTT_REMOTE_USER = 'admin'
MQTT_REMOTE_PWD = 'pwd'
MQTT_TOPIC_CLIENT_TO_REMOTE = 'dthing/terminal2remote/data'
MQTT_TOPIC_REMOTE_TO_CLIENT = 'dthing/remote2terminal/data'

CMD_STR_NONE = 'none'
CMD_STR_INSTALL = 'install'
CMD_STR_DELE = 'delete'
CMD_STR_RUN = 'run'
CMD_STR_LIST = 'list'
CMD_STR_OTA = 'ota'
CMD_STR_DESTROY = 'destroy'
CMD_STR_LINKS = 'links'

CMD_STR_DIRCTION_UP = 'remote2user'
CMD_STR_DIRCTION_DOWN = 'user2remote'

KEY_CMD = 'cmd'
KEY_CMD_DIRCTION = 'cmd_direction'
KEY_CMD_PARAM = 'cmd_param'
KEY_CMD_STATUS = 'cmd_status'
KEY_BODY = 'body'
KEY_LINK_ID = 'current_tcp_id'
KEY_LINK_SOCKET = 'current_tcp_socket'

STATUS_OK = 'ok'
STATUS_ERROR = 'error'
STATUS_RECVED = 'received'
