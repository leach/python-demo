#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Querier:
    pass

    def __init__(self, db_file):
        self.db_file = db_file

    def print(self):
        f = open(self.db_file, 'r')
        for line in f:
            print(line.strip())

        f.close()


