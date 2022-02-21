# Deep-Learning for Conversational Speech using Semantic Textual Analysis
## Setup
### Recreate and activate conda virtual environment (using Python 3.7):
```
$ conda env create -f conv_sph.yml python=3.7
$ conda activate conv_sph
```

## Usage
### File Processing
#### Youtube Transcript to SRT File Converter
Run the YT_transcript_to_srt.py script with the first argument as the path to the folder containing Youtube video transcripts.
```
$ python YT_transcript_to_srt.py C:/example/cwd/mydir/transcripts
```
The SRT files will be located at C:/example/cwd/mydir/srt
