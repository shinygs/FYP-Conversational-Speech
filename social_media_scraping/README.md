## Reddit Scraper
This script scrapes Reddit posts and their related information without requiring existing Reddit account credentials
<br/>

### Usage
Run the reddit_scraper.py script with the following arguments:
1. String to be searched in Reddit
2. No. of Reddit posts to be scraped
3. Flag for comments of posts to be scraped ('comments_true' if you want comments, else 'comments_false')
```
$ python reddit_scraper.py katong 40 comments_false
```
The scraped data will be located at C:/example/cwd/mydir/Scraped_reddit_data.json
<br/>
<br/>

## Twitter Scraper
This script scrapes tweets and their related information without requiring existing Twitter developer account credentials
<br/>

### Usage
Run the twitter_scraper.py script with the following arguments:
1. String to be searched in Twitter
2. No. of tweets to be scraped
```
$ python twitter_scraper.py katong 40
```
The scraped data will be located at C:/example/cwd/mydir/scraped_tweets.csv
<br/>
