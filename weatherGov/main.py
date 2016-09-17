#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weatherGov import Weather

def main():
    res = Weather().run()
    print(res)

if __name__ == '__main__':
    main()
