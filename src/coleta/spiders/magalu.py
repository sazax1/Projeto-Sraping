import scrapy


class MagaluSpider(scrapy.Spider):
    name = "magalu"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/selecao/ofertasdodia/?page=1"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('div.sc-dcjTxL.xDJfk') 

        for product in products:

            yield {
                'brand' : product.css('h2.sc-fvwjDU.fbccdO::text').get(),
                'old_price' : product.css('p.sc-kpDqfm.efxPhd.sc-gEkIjz.jmNQlo::text').get(),
                'new_price' : product.css('p.sc-kpDqfm.eCPtRw.sc-bOhtcR.dOwMgM::text').get()
            }
        
        if self.page_count < self.max_pages:
            self.page_count += 1
            next_page = f"https://www.magazineluiza.com.br/selecao/ofertasdodia/?page={self.page_count}"
            yield scrapy.Request(next_page, callback=self.parse)

    
        pass
