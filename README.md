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
The file I chose to use for testing and the histogram was The Adventures of Sherlock Holmes, which can be found [here](https://sherlock-holm.es/ascii/). I thought this was an interesting file just because it is an entire book and the largest file I could find on Sherlock Holmes, meaning more data to quantify.

### Methodology
When developing my software, I focused on both usability and modularity. I wanted this to be easy to figure out, which is I spent time to set up the [argparse library](https://docs.python.org/3/library/argparse.html) so I could offer better instructions. For modularity, I worked to develop each command seperately, as they shouldn't rely on each other and would allow me to test each individually for bugs. This also helped for usability since I could learn what each individual part was reliant on and have the program download it for the user. When preparing to create the histogram, I wanted to make it simple to just take the data from the program and send it to excel or any other software, so even though it wasn't required, I had the program create two extra txt files, one to save the results of the console print (results.txt) and one that would contain only the counts so I or anyone else could easily plug them into excel (histogram_counts.txt).

#### Options
- Lowercasing
  This changes all capital letters into lowercase and allows the program to count them as the same (so cat is no longer a seperate token from Cat).
- Stemming
  Stemming attempt to reach the 'stem' of the word so that words like "swimming" and "swims" both become "swim". This improves the counts of words with different variations but the same meaning.
- Remove Stopwords
  Removing stopwords such as "the", "and", "a" allows the program to focus on the counts of more important words. For The Adventures of Sherlock Holmes, with stopwords removed, "said" is the most common word and indicates how dialoge heavy the text is.
- Remove numbers and symbols
  This was my addition to the options, as I thought that often times numbers in text can be easily replaced (2 doors vs 3 vs 50) and symbols will often just be to show quotes or '&' or apostrophes. I thought having a tool to remove everything outside of raw letters would be a useful option just to understand words being used. The other main reason is I wanted an option that can coexist with the others, and many other ideas would step on their toes or require another option to always be used in concurrence.

### Sample Output (All done with sherlock.txt will all options used)
#### First 10 words
```
said 486
upon 464
holmes 461
one 369
would 327
man 288
could 286
mr 274
little 269
see 229
```

#### Last 10 words
```
fitness 1
formatted 1
ascii 1
html 1
variants 1
httpsherlockholmes 1
electronic 1
additional 1
collections 1
version 1
```

#### Generated Histogram
![image](https://github.com/smhavens/NLPHW01/assets/55886989/7e37c408-0749-4668-9809-49833ccd1421)

### Discussion
#### Findings
Of the most common words, there are some that can be expected such as "said" in a novel along with "could" and "would". "holmes" also was to be expected as the titular character thought some did catch my attention: particulary "see", "one", "man" and "mister". "see" I can reason as I used a detective novel which naturally will have many observations on the crime scene, the suspects, and other such things. The other four, however, I think help date the story as "one" as a pronoun isn't used often anymore but from my reading of the text is used considerably. Similarly, the fact that "mr" is used so often shows a formality that many recent texts don't adhear to, and "man" can hint at there being few women characters in the text.
Looking at the least common words, I noticed that some were merely from txt file details on the document, such as "httpsherlockholmes", "electronic", "ascii" and "html". I also noticed that there were more tokens with only 1 appearance than there were of any other count. This shows how while these words on their own are rare, texts will often use many rare words in conjuntion with many of the few common words. This goes along well with Zipf's law, as we see with War and Peace that there are only select words with high counts but a high frequency of words with lower counts. I removed stop words for my diagram but looking at the top 5 counts with stopwords:
```
the 5621
and 3002
i 2995
to 2685
of 2658
```
and they significantly outweigh even the most common non-stop word (said). Removing stopwords impacts the number of tokens far more than the number of words, as the largest part of the histogram without stopwords (around 8 thousand words with 1 to 4 occurances) is trumped by only a handful of stopwords in their total count.

#### What I've Learned
First, this assignment gave me excellent practice in documentation, as seen by this readme. I was able to note down what steps I need and really think about what libraries I was actively using and if their inclusion (and then required documentation on how to use) was worth it compared to doing it some other way. I got practice using the nltk library, which will be exceptionally useful for later projects considering how much it alleviates the process of stemming or lowercasing text. These were things I more or less expected to learn, but one thing that did catch me a bit off guard was what the token counts taught me about the text itself. I mentioned previously with the most common non-stopwords in The Adventures of Sherlock Holmes having dated words or a much larger amount of masculine terms (mr or man) and analyzing this could be important for understanding the text in broad strokes.
