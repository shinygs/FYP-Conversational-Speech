## Youtube Transcript to SRT Converter
This script converts Youtube video transcripts to SRT format, such that it can be used in subtitle editors (e.g. SubtitleEdit) to test subtitle synchronization with Youtube audio.
<br/>
<br/>
--- Input: Folder containing YouTube video transcripts (can be obtained using Zhi Hao's Youtube crawling script [crawler_youtube.tar])
<br/>
--- Output: Folder containing SRT files of YouTube videos
### Usage
1. Run the YT_transcript_to_srt.py script with the following argument:
   - Path to the folder containing Youtube video transcripts
```
$ python YT_transcript_to_srt.py C:/example/cwd/mydir/transcripts
```
The SRT files will be located at C:/example/cwd/mydir/srt   
<br/>
[For script testing purposes]:
Test run can be done on the 'test_transcripts' folder
