import sys, os
import csv
import snscrape.modules.twitter as sntwitter


def scrape_twitter(search_str, num_tweets):
    csv_file_path = os.path.join(os.getcwd(), 'scraped_tweets.csv')
    csvFile = open(csv_file_path, 'a', newline='', encoding='utf8')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['id','date','tweet']) 
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('' + search_str + ' since:2021-01-01 until:2021-11-05 -filter:links').get_items()):
        if i == num_tweets:
            break
        csvWriter.writerow([tweet.id, tweet.date, tweet.content])
        
    csvFile.close()


search_str_input = sys.argv[1]
num_tweets_input = sys.argv[2]
scrape_twitter(search_str_input, int(num_tweets_input))
