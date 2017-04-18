# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
from spd import Spd


def word(response):
    item = {}
    item['ipa'] = response.xpath('//span[@class="ipa"]/text()').extract_first()
    yield item


class Word(Spd):
    """
    springer spider
    """

    def __init__(self):
        custome_settings={
            'DIR_NAME': 'springer',
            'SITE': 'springer',
            'field_to_export': ['ipa'],
            'CALLBACK': 'word',
            'PARSE': {'word': word},
        }
        super(Word, self).__init__(custome_settings)

    @staticmethod
    def get_urls():
        """
        generate the book url to crawl
        """
        url = 'http://dictionary.cambridge.org/dictionary/'\
            'english-chinese-simplified/%s'
        for i in ['dance']:
            return [(url % i, {})]


if __name__ == '__main__':
    WORD = Word()
    WORD.start_crawl()
# create table v (id int auto_increment primary key , word varchar(16), pron varchar(16), type vachar(8), meaning text)
