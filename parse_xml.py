#! /usr/bin/env python3
# coding: utf-8

import time
import requests
from xml.etree import ElementTree
import re
import sqlite3

ns = {'gml': "http://www.opengis.net/gml/3.2"}

class parse_xml:
    def __init__(self, xml_path, sqlite_path):
        tree = ElementTree.parse(xml_path)
        self.root = tree.getroot()

    def get_range(self):
        lower_corner_text = self.root.find('.//gml:lowerCorner', ns).text.strip()
        upper_corner_text = self.root.find('.//gml:upperCorner', ns).text.strip()
        lower_corner = [float(l) for l in lower_corner_text.split(' ')]
        upper_corner = [float(l) for l in upper_corner_text.split(' ')]
        return [[lower_corner[0], upper_corner[0]],
                [lower_corner[1], upper_corner[1]]]

    def get_grid_num(self):
        low_text = self.root.find('.//gml:low', ns).text.strip()
        high_text = self.root.find('.//gml:high', ns).text.strip()
        low = [float(l) for l in low_text.split(' ')]
        high = [float(l) for l in high_text.split(' ')]
        return [(int(h) - int(l) + 1) for (l, h) in zip(low, high)]

    def get_height(self):
        height_list_text = self.root.find('.//gml:tupleList', ns).text.strip()
        data_num = 0
        for height_elem in height_list_text.split('\n'):
            if height_elem == '':
                continue
            lat_index = int(data_num / self.grid_num[0])
            lon_index = data_num % self.grid_num[0]
            
            data_num += 1


            
    def run(self):
        pass

    def write_db(self, sqlite_path):
        db = sqlite3.connect(sqlite_path)
