## Generate Similar Sentences with PEGASUS
This script generates semantically similar *formal* sentences from conversational sentences using the PEGASUS model. 
<br/>
### Usage
1. Run the gen_sim_sentences_pegasus.py script with the following arguments:
   - Path to the CSV file containing conversational sentences
   - No. of similar sentences to be generated per conversational sentence
```
$ python gen_sim_sentences_pegasus.py C:/example/cwd/mydir/sentences.csv
```
The new file with the generated sentences will be located at C:/example/cwd/mydir/similar_sentences_pegasus.csv   
<br/>
[For script testing purposes]:
Test run can be done on the 'test_sentences' folder
<br/>
<br/>
## Youtube Transcript to SRT Converter
This script generates semantically similar sentences from conversational sentences using the iNLTK model. 
<br/>
### Usage
1. Run the gen_sim_sentences_inltk.py script with the following arguments:
   - Path to the CSV file containing conversational sentences
   - No. of similar sentences to be generated per conversational sentence
```
$ python gen_sim_sentences_inltk.py C:/example/cwd/mydir/sentences.csv
```
The new file with the generated sentences will be located at C:/example/cwd/mydir/similar_sentences_inltk.csv  
<br/>
[For script testing purposes]:
Test run can be done on the 'test_sentences' folder
