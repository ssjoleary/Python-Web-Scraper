# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field #,Item

from speciesguide.models import Species
from sightings.models import Sighting

class SpeciesItem(DjangoItem):
    # define the fields for your item here like:
    # name = Field()

    django_model = Species

class SightingItem(DjangoItem):
	django_model = Sighting