# coding=utf-8

from pytdx.parser.base import BaseParser
from pytdx.helper import get_datetime, get_volume, get_price
from collections import OrderedDict
import struct


class ExSetupCmd1(BaseParser):

    def setup(self):
        '''self.send_pkg = bytearray.fromhex("01 01 48 65 00 01 52 00 52 00 54 24 1f 32 c6 e5"
                                            "d5 3d fb 41 1f 32 c6 e5 d5 3d fb 41 1f 32 c6 e5"
                                            "d5 3d fb 41 1f 32 c6 e5 d5 3d fb 41 1f 32 c6 e5"
                                            "d5 3d fb 41 1f 32 c6 e5 d5 3d fb 41 1f 32 c6 e5"
                                            "d5 3d fb 41 1f 32 c6 e5 d5 3d fb 41 cc e1 6d ff"
                                            "d5 ba 3f b8 cb c5 7a 05 4f 77 48 ea")'''
        self.send_pkg = bytearray.fromhex('01 01 48 65 00 01 52 00 52 00 54 24 e5 bb 1c 2f af'
                                          'e5 25 94 1f 32 c6 e5 d5 3d fb 41 5b 73 4c c9 cd bf'
                                          '0a c9 5a 06 d9 2a 37 3c be 39 8d ea 43 d8 06 5f 19'
                                          '4a 40 f4 fd 3b 0e f3 78 24 1f 32 c6 e5 d5 3d fb 41'
                                          '1f 32 c6 e5 d5 3d fb 41 24 28 83 02 ea 5f c6 3d f4'
                                          '43 51 2c 51 84 77 20')

    def parseResponse(self, body_buf):
        pass
