# -*- coding: utf-8 -*-
"""
@author: Alfred
"""
import csv


class CsvPipeline(object):
    """
    Pipeline to csv file
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Get item fields and file path through crawler
        """
        return cls(crawler.settings)

    def __init__(self, settings):
        self.flds = settings.get('field_to_export')
        self.writer = csv.writer(
            open(settings['FILE_PATH'], 'a', encoding='utf-8')
        )

    def process_item(self, item, spider):
        """
        write file
        """
        row = []
        for fld in self.flds:
            try:
                for i in ['\n', '\r', u'\xa0']:
                    item[fld] = item[fld].replace(i, '')
                row.append(item[fld].strip(' '))
            except:
                row.append(item[fld])
        self.writer.writerow(row)
