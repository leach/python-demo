#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

d = datetime.datetime.now()
print(d)
print(d.timestamp())
print(d.today())
print(d.year)
print(d + datetime.timedelta(minutes=100))
print(d + datetime.timedelta(days=100))