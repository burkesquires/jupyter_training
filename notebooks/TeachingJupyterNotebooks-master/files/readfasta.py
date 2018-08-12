def readgenome (filename):
    '''This function takes the filename in the directory'''
    genome = '' # stores the result 
    with open(filename,'r') as filehandle: # i'm telling the comp to read any file and store in a filehandle
        for line in filehandle: # going through all the characters in the filehandle
            genome += line.rstrip() # removing all the new line characters in the string
    return genome # spit out the result of the function
    
# specify path to file
filename = 'files/chr-1.fasta'
fasta = readgenome(filename)[10143: 11143]
