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
## Generate Similar Sentences with iNLTK
This script generates semantically similar sentences from conversational sentences using the iNLTK model. 
<br/>
### Setup
#### Recreate and activate conda virtual environment (using Python 3.7):
```
$ conda env create -f gen_sim_sent_inltk.yml python=3.7
$ conda activate gen_sim_sent_inltk
```
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
