import scrapy


class EspnNBASpider(scrapy.spiders.Spider):
    name = "espn"
    start_urls = [
        'http://www.espn.com/espn/rss/nba/news',
        'http://www.espn.com/espn/rss/nfl/news',
        'http://www.espn.com/espn/rss/news',
        'http://www.espn.com/espn/rss/mlb/news',
        'http://www.espn.com/espn/rss/nhl/news',
        'http://www.espn.com/espn/rss/rpm/news',
        'http://soccernet.espn.com/rss/news',
        'http://www.espn.com/espn/rss/espnu/news',
        'http://www.espn.com/espn/rss/ncb/news',
        'http://www.espn.com/espn/rss/ncf/news',
        'http://www.espn.com/espn/rss/action/news',
        'http://www.espn.com/espn/rss/poker/master',
        'http://www.espn.com/broadband/ivp/rss',
        'http://search.espn.com/rss/bill-simmons/',
        'http://www.grantland.com/feed',
        'http://www.espn.com/espn/rss/recruiting/osu/news',
        'http://www.espn.com/espn/rss/recruiting/georgia/news',
        'http://www.espn.com/espn/rss/recruiting/oregon/news',
        'http://www.espn.com/espn/rss/recruiting/florida/news',
        'http://www.espn.com/espn/rss/recruiting/tamu/news',
        'http://www.espn.com/espn/rss/recruiting/lsu/news',
        'http://www.espn.com/espn/rss/recruiting/texas/news',
        'http://www.espn.com/espn/rss/recruiting/washington/news',
        'http://www.espn.com/espn/rss/recruiting/psu/news',
        'http://www.espn.com/espn/rss/recruiting/fsu/news',
        'http://www.espn.com/espn/rss/recruiting/oklahoma/news',
        'http://www.espn.com/espn/rss/recruiting/alabama/news',
        'http://www.espn.com/espn/rss/recruiting/usc/news',
        'https://www.espn.com/espn/rss/index',
    ]

    def parse(self, response):
        url = response.url
        for news in response.css('rss channel item'):
            yield {
                'source': url,
                'title': news.css('title::text').get(),
                'description': news.css('description::text').get(),
                'pubDate': news.css('pubDate::text').get(),
                'linkedContent':scrapy.Request(news.css("link::text").get(), callback=self.parse_content)
            }

    def parse_content(self, response):
        # response.xpath('//div//ul//li//p//a').getall() # this will get the link in the main page
        yield response.css('p::text').getall() # this will provied full content


