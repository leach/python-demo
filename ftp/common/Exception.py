#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CmdException(Exception):
    """
    异常
    """
    def __init__(self,message):
        Exception.__init__(self, message)
        self.message=message
