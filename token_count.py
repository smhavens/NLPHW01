import sys
import argparse
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def read_file(args):
    # print("Reading file")
    word_dict = {}
    # print(args)
    if args.stem:
        nltk.download('punkt')
        stemmer = PorterStemmer()
    if args.word:
        nltk.download('stopwords')
    with open(args.filename, 'r') as myfile:
        for line in myfile:
            if args.lower:
                # print(line)
                line = line.lower()
            # if args.stem:
                # line = word_tokenize(line)
            
            # print("Begin word stuff")
            for word in line.split():
                # print(word)
                if args.number:
                    word = ''.join([i for i in word if i.isalpha()])
                    # print("4U".isalpha())
                if args.word:
                    if word not in stopwords.words('english'):
                        if args.stem:
                            word_tokenize(word)
                            stemmer.stem(word)
                        word_dict.setdefault(word, 0)
                        word_dict[word] += 1
                else:
                    if args.stem:
                            word_tokenize(word)
                            stemmer.stem(word)
                    word_dict.setdefault(word, 0)
                    word_dict[word] += 1
                    
                
            
    # print(word_dict)
    return word_dict
    

def main():
    # if len(sys.argv) < 3:
    #     exit("Please input text file and at least one preprocessing command.")
    
    #### ARGLINE PARSER ####
    parser = argparse.ArgumentParser(
        prog='normalize_text',
        description='This program will take in a txt file and list of desired preproccessing commands and output tokens.',
        epilog='Please give at least one of the following preprocessing procedures: lowercasing (--lower or -l), stemming (--stem or -s), stopword removal (--word or -w), or number and symbol removal (--number or -n)'
    )
    parser.add_argument('filename')
    parser.add_argument('-l', '--lower', action='store_true')
    parser.add_argument('-s', '--stem', action='store_true')
    parser.add_argument('-w', '--word', action='store_true')
    parser.add_argument('-n', '--number', action='store_true')
    
    args = parser.parse_args()
    # if args.filename == '':
    #     exit("Please input text file and at least one preprocessing command.")
    # print(args.filename, args.lower, args.stem, args.word)
    
    #### READ AND THEN SORT FILE ####
    sorted_dict = sorted(read_file(args).items(), key=lambda x:x[1], reverse=True)
    # print(sorted_dict)
    
    
    #### PRINT RESULTS ####
    print_list = []
    for token, count in sorted_dict:
            print(token, count)
            print_list.append(token + " " + str(count))
            
    # Results.txt has the exact copy of the console print
    with open("results.txt", 'w') as results:
        results.writelines([word + "\n" for word in print_list])
        
    # histogram_counts.txt has the numbers only copy of the console print for easy graphing
    count_list = []
    with open("histogram_counts.txt", "w") as excel:
        for token, count in sorted_dict:
            # print(token, count)
            count_list.append(str(count))
        excel.writelines([num + "\n" for num in count_list])
    
    
    
    
    
if __name__ == "__main__":
    main()