# Scrapy settings for fypscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'fypscraper'

SPIDER_MODULES = ['fypscraper.spiders']
NEWSPIDER_MODULE = 'fypscraper.spiders'
ITEM_PIPELINES = {
	'fypscraper.pipelines.FypscraperPipeline': 1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fypscraper (+http://www.yourdomain.com)'

# Setting up django's project full path.
import sys
#sys.path.insert(0, '/home/ssjoleary/PythonProjects/fyp')
sys.path.append('/home/ssjoleary/PythonProjects/fyp')

# Setting up django's settings module name.
# This module is located at /home/rolando/projects/myweb/myweb/settings.py.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'wildlifewebapp.settings'