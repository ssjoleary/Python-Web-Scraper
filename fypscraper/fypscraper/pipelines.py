#from sqlalchemy.orm import sessionmaker
#from models import Species, db_connect

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class FypscraperPipeline(object):
	""" 
    Speciesguide pipeline for storing scraped items in the database
    """
        def process_item(self, item, spider):
           item.save()
           return item