
def readFastq(filename):
    '''Reading and parsing a fastq file
    return the reads in a list
    returns the quality score for the individual read'''
    sequences = [] # stores a list sequences 
    qualities = [] # stores a list of quality scores
    with open(filename) as fh: # open the file and store it in a file handle
        while True: # loop through the file
            fh.readline() # skip name line
            seq = fh.readline().rstrip() # read base sequence and store it
            fh.readline() # skip placeholder line
            qual = fh.readline().rstrip() # read base quality scores and store them
            if len(seq) == 0: # if the end of the file is reached 
                break # stop looping through the file
            sequences.append(seq) # the elif we are still reading through the file append it to seq
            qualities.append(qual) # continue appending the quality scores past the influence of the loop
    return sequences, qualities # returns multiple values 

seqs, quals = readFastq('files/SRR835775_1.first1000.fastq')
print (seqs[:5]) ; print (quals[:5])