# Deep-Learning for Conversational Speech using Semantic Textual Analysis
## Setup
### Recreate and activate conda virtual environment (using Python 3.7):
```
$ conda env create -f conv_sph.yml python=3.7
$ conda activate conv_sph
```

## Usage
### File Processing
#### Youtube Transcript to SRT Converter
Run the YT_transcript_to_srt.py script with the following arguments:
1. Path to the folder containing Youtube video transcripts
```
$ python YT_transcript_to_srt.py C:/example/cwd/mydir/transcripts
```
The SRT files will be located at C:/example/cwd/mydir/srt   
<br/>

#### Split YouTube Audio on Sentence-Level
Run the split_audio_sentence_level.py script with the following arguments:
1. Path to the folder containing folders of Youtube video transcripts and wav files
```
$ python split_audio_sentence_level.py C:/example/cwd/mydir
```
The split wav files will be located at C:/example/cwd/mydir/wav_by_sentence
<br/><br/>

### Social Media Scraping
#### Reddit Scraper
Run the reddit_scraper.py script with the following arguments:
1. String to be searched in Reddit
2. No. of Reddit posts to be scraped
3. Flag for comments of posts to be scraped ('comments_true' if you want comments, else 'comments_false')
```
$ python reddit_scraper.py katong 40 comments_false
```
The scraped data will be located at C:/example/cwd/mydir/Scraped_reddit_data.json
<br/>

#### Twitter Scraper
Run the twitter_scraper.py script with the following arguments:
1. String to be searched in Twitter
2. No. of tweets to be scraped
```
$ python twitter_scraper.py bendemeer 15
```
The scraped data will be located at C:/example/cwd/mydir/scraped_tweets.csv
<br/>
