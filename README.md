# SpecialFinder
A crawler helps me find the specials from a variety of sites those I am interested in.  
**Note: Incomplete. Still in development**

### Techincal stack:
[Scrapy](http://scrapy.org/)

### Development:

```bash
$ pip install -r requirements.txt
```

### Run crawlers:

```bash
$ cd crawlers
Run a specific crawler
$ scrapy crawl {{ crawler name }} -s {{ settings }}
For example:
$ scrapy crawl coles -s CLOSESPIDER_PAGECOUNT=5 
```

### Deployment:

```bash
$ cd crawlers && shub deploy
```
