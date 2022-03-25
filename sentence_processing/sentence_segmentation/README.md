## Sentence Segmentation
This script segments YouTube video transcripts into proper sentences.
<br/>

### Usage
Run the sentence_segementation.py script with the following argument:
1. Folder containing YouTube video transcripts (can be obtained using Zhi Hao's Youtube crawling script [crawler_youtube.tar])
```
$ python sentence_segmentation.py C:/example/cwd/mydir/transcripts
```
The new files will be located at C:/example/cwd/mydir/segmented_text
<br/>
<br/>

## Sentence Segmentation with Timestamps
This script segments YouTube video transcripts into proper sentences with timestamps.
<br/>

### Usage
1. Get the YouTube video transcript with word-level timestamps from YouTube-dl using the YouTube video ID
```
$ youtube-dl --write-auto-sub --skip-download "https://www.youtube.com/watch?v=6TfJeJwBKdw
```
Rename the generated file to 'input.vtt' and ensure it is located in the vtt_clean folder. 
<br/>
<br/>
2. Run Prof Chng's VTT cleaning script to remove repeating lines and improper formatting in the 'input.vtt' file (Ensure correct input and output file paths in the script):
```
$ python convertYouTubeVTT_textNormalize.py 
```
A 'output.vtt' file will be located in the vtt_clean folder
<br/>
<br/>
3. Run the sentence_segmentation_with_times.py script on the 'output.vtt' file:
```
$ python sentence_segmentation_with_times.py C:/example/cwd/mydir/vtt_clean/output.vtt
```
The new file with the segmented sentences and timestamps will be located at C:/example/cwd/mydir/vtt_clean/segmented_text_with_times.txt
<br/>
<br/>
[For script testing purposes]:
Test run can be done on the included 'input.txt' file in the vtt_clean folder
