## Split YouTube Audio on Sentence-Level
This script splits Youtube audio by sentence, such that it can be used in ASR systems to examine the accuracy of speech recognition on utterances.
<br/>
<br/>
--- Input: Folder containing folders of YouTube video transcripts and wav files (can be obtained using Zhi Hao's Youtube crawling script [crawler_youtube.tar])
<br/>
--- Output: Folder containing wav files by sentence
### Usage
1. Run the split_audio_sentence_level.py script with the following argument:
   - Path to the folder containing folders of Youtube video transcripts and wav files (ensure both folders are named 'transcripts' and 'wav' as originally)
```
$ python split_audio_sentence_level.py C:/example/cwd/mydir
```
The split wav files will be located at C:/example/cwd/mydir/wav_by_sentence
<br/>
<br/>
[For script testing purposes]:
Test run can be done on the provided 'transcripts' and 'wav' folders
