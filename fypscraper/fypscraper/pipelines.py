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
        encodeSpecname = item.get('specname', [''])[0].encode('ascii',errors='ignore')

        encodeSpecclass = item.get('specclass', [''])[0].encode('ascii',errors='ignore')
        encodeSpecorder = item.get('specclass', [''])[1].encode('ascii',errors='ignore')
        encodeSpecsuborder = item.get('specclass', [''])[2].encode('ascii',errors='ignore')
        encodeSpecfamily = item.get('specclass', [''])[3].encode('ascii',errors='ignore')
        encodeSpecgenus = item.get('specclass', [''])[4].encode('ascii',errors='ignore')
        encodeSpecspecies = item.get('specclass', [''])[5].encode('ascii',errors='ignore')
        encodeSpeccommonname = item.get('specclass', [''])[6].encode('ascii',errors='ignore')

        item['specname'] = encodeSpecname
        item['specclass'] = encodeSpecclass
        item['specorder'] = encodeSpecorder
        item['specsuborder'] = encodeSpecsuborder
        item['specfamily'] = encodeSpecfamily
        item['specgenus'] = encodeSpecgenus
        item['specspecies'] = encodeSpecspecies
        item['speccommonname'] = encodeSpeccommonname

        item.save()
        return item