# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class SubtitlePipeline(object):
    def process_item(self, item, spider):
        url = item['url']
        file_name = 'result/'+item['filename']+'.donwload'
        with open(file_name, 'wb') as f:
            f.write(item['body'])
        os.rename(file_name,'result/'+item['filename'])
        return item
