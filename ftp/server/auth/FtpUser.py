#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FtpUser:

    def __init__(self, username, homedir, currdir, maxsize, usedsize):
        self.username = username
        self.homedir = homedir
        self.currdir = currdir
        self.maxsize = maxsize
        self.usedsize = usedsize
