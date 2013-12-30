from scrapy.item import Item, Field

class LivingSocialDeal(Item):
    """
    Livingsocial containery (dictionary-like object) for scraped data 
    """

    title = Field()
    description = Field()
    location = Field()
    price = Field()