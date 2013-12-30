from scrapy.item import Item, Field

class LivingSocialDeal(Item):
    """
    Livingsocial containery (dictionary-like object) for scraped data 
    """

    title = Field()
    description = Field()
    category = Field()
    location = Field()
    original_price = Field()
    price = Field()