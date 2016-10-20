import os, matplotlib.pyplot as plt, numpy as np, scipy.stats as stats, sh
""" Importing the necessary modules"""


class FastaParser(object):
    """ Defining class FastaPareser that takes a filepath"""
    def __init__(self, path):
        """ Initializing with file path and check if file path exists"""
        self.path = path
        self.count_genes()               
        if not os.path.exists(self.path):
            raise IOError("The file does not exist")

# Here we parse the fasta file and split it up into three lists. A temporary list in order to join the lines for each entry in the contigs file,
# a list for the headers in order to count the number of sequences and finally a list of sequences, where the joined contig sequences end up at the end of the loop.
        tmp = []
        header = []
        seq = []
        with open(self.path) as infile:
            for line in infile:
                if line.startswith('>'):
                    header.append("".join(line.strip(">").rstrip("\n")))
                    seq.append(''.join(tmp))
                    tmp = []
                else:
                    tmp.append(line.strip())
            else:
                seq.append(''.join(tmp))
        seq.pop(0)

        dict_seq = {name : seq for name, seq in zip(header, seq)} # Creating a dictonary
# Assigning attributes
        self.length = len(seq)
        self.seq = seq
        self.header = header        
        self.dict_seq = dict_seq



    def count_genes(self):
        """ A methhod to count the number of genes based on the fasta header that starts with > """
        number_genes = 0
        with open(self.path) as infile:
            for line in infile:
                if line.startswith('>'):
                    number_genes += 1
                self.count = number_genes


    def __len__(self):
        """A method to calculate the length of the object"""
        return self.length

    def __getitem__(self, arg):
        """ A method for indexing and extracting an item from either a list for sequences or dictonary for contig/gene name"""
        if type(arg) == int:
            return self.seq[arg]
        elif type(arg) == str:
            return self.dict_seq[arg]



    def extract_length(self, max_length):
        """ Extract the sequences that are shorter a specified length"""
        self.max_length = max_length
        seq_storage = []
        for line in self.seq:
            if len(line) <= max_length:
                seq_storage.append(line)
        return seq_storage

    def length_dist(self, path):
        """ A to calculate the distribution of sequence length from the input fasta file and plot that distribution. The plot is then saved in pdf format in a newly creted directory"""
        directory = os.path.split(path)
        sh.mkdir("-p", directory)

        length_list = []

        for line in self.seq:
            length_list.append(len(line))
        a = np.array(length_list)
        a.sort()
        f = plt.figure()
        a_mean = np.mean(a)
        a_std = np.std(a)
        p = stats.norm.pdf(a, a_mean, a_std)
        plt.xlabel('Sequence length')
        plt.ylabel('Number of sequences')
        plt.plot(a, p)
        plt.show()
        f.savefig(path)


       
                 
