import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        for product in response.xpath("//div[@id='product-lists']/div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row']"):
            if product.xpath("./div[@class='product-img-outer']"):
                yield {
                    'url': product.xpath("./div[@class='product-img-outer']/a/@href").get(),
                    'image_url': product.xpath("./div[@class='product-img-outer']/a/img[1]/@src").get(),
                    'name': product.xpath("./div[@class='p-title-block']/div[2]/div/div/div/a/text()").get().rstrip().lstrip(),
                    'price': product.xpath("./div[@class='p-title-block']/div[2]/div/div[2]/div/div/span/text()").get()
                }

            next_page = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
            if next_page:
                yield scrapy.Request(url='https://www.glassesshop.com/bestsellers?page=2', callback=self.parse)