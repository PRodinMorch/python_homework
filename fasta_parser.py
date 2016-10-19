import pytest

# I wanna start by defining the class using only the path as the attribute. Within it i also want to raise exceptions for IOError and TypeError. The IOError works fine,
# But the type error eception wont be raised.

class FastaParser(object):
    def __init__(self, path):
        self.path = path
        self.count()
               
        try:
            self.path = open(path)
        except IOError:
            raise Exception('/file_does_not_exist.fasta')
        except TypeError:
            raise Exception('Filename is missing')

    def count(self):
        fasta = []
        with open(self.path) as infile:
            for line in infile:
                if line.startswith('>'):
                    fasta.append(line)
        self.count = fasta.count('>')

# Here i want to define methods that will parse the fasta file and somehow turn it into a list or dictonary so i can use those properties to obtain len() and count(),
# These dont work which leads me to belive that they have to be defined differently
    def __iter__(self):
        fasta = {}
        with open(self.path, 'r') as infile:
            for line in infile:
                if line.startswith('>'):
                    fasta.append(line)                
        yield fasta

    
    def __len__(self):
        return len(self.path)

    def len(self):
        return self.__len__()


contigs = FastaParser("all_contigs.fasta")
genes = FastaParser("predicted_genes.fasta")


# Here i want to parse the file and put the lines into a dictionary/list. I havent had time to try and put it into place yet, but this is needed in order to solve the later steps in exercise_day5.py
header = ""
seq = ""

for line in file:
    if line.startswith(">")
    header.append(line)
else:
     seq += line




header = ""
seq = ""
dict_seq = {}
for line in file:
    if line.startswith(">"):
        if header!= "" = dict_seq[header] : seq:
        header = the line
    else:
     seq + = the line


