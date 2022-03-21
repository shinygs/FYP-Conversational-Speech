----- Split YouTube Audio on Sentence-Level -----
*** This script splits Youtube audio by sentence, such that it can be used in ASR systems to examine the accuracy of speech recognition on utterances.
*** Input: folder containing folders of Youtube video transcripts and wav files (can be obtained using Zhi Hao's Youtube crawling script [crawler_youtube])
*** Output: folder containing wav files by sentence


1. Run the split_audio_sentence_level.py script with the following argument:
   - Path to the folder containing folders of Youtube video transcripts and wav files (ensure both folders are named 'transcripts' and 'wav' as originally)

	python split_audio_sentence_level.py C:/example/cwd/mydir


2. The split wav files will be located at C:/example/cwd/mydir/wav_by_sentence


[For script testing purposes]:
Test run can be done on the given 'transcripts' and 'wav' folders

	
	
