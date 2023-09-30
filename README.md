# Text Normalization Tool

## Download Files
To run, download token_count.py in the repository and optionally sherlock.txt or h.txt for text files to run with the program. Your Tokenization file should now include the following:
- token_count.py
- sherlock.txt [OPTIONAL]
- h.txt [OPTIONAL]

## Tokenization Tool

To run the program, use the command 
```
python3 token_count.py [txt file name] [options]
```

The options to run the program include:
- lowercase all letters (-l or --lower)
- stemming (-s or --stem)
- remove stopwords (-w or --word)
- remove all numbers and symbols (-n or --number)
- help (-h or --help)

For example, to run all options the command would look like
```
python3 token_count.py sherlock.txt -l -s -w -n
```

The tokenization tool's program already includes all needed downloads and should run as is.

## Histogram Results
After running token_count.py on sherlock.txt (The adventures of sherlock holmes), I was able to plot this histogram in excel:
![image](https://github.com/smhavens/NLPHW01/assets/55886989/7e37c408-0749-4668-9809-49833ccd1421)

## Report
### Data
The file I chose to use for testing and the histogram was The Adventures of Sherlock Holmes, which can be found [here](https://sherlock-holm.es/ascii/)

### Methodology

### Sample Output

### Discussion
