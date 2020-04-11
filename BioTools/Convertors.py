

class FastaToBam():
    """
    converting FASTA format to BAM format
    """

    def __init__(self):
        """ Constructor """
        pass

    def read_fasta_file(self,fileNamePath:'the path to the fasta file'='')->'return the list of lines':
        lines = []

        with open(fileNamePath, 'r') as file_handle:
            lines = file_handle.readlines()        

        return  lines

    
    def FastaBuilderFromFile(self,fileNamePath)-> 'return the multi fasta dict':
        """
        check if there is fasta header ('>') or not
        """
        import StringTool

        fastaHeader = '>'
        fastaFormatData = {} #header : seq
        last_header_title =''

        listOfLists = self.read_fasta_file(fileNamePath)

        for line in listOfLists:
            if line.find(fastaHeader) != -1 :
                #just adding the header
                last_header_title = line
                fastaFormatData[line] = ''
            else:
                #adding the data
                if last_header_title != '':
                    fastaFormatData[last_header_title] += line

        return fastaFormatData

    def FastaBuilderFromLists(self,listOfLists)-> 'return the fast multi dict':
        """
        check if there is fasta header ('>') or not
        """
        import StringTool

        fastaHeader = '>'
        fastaFormatData = {} #header : seq
        last_header_title =''

        for line in listOfLists:
            if line.find(fastaHeader) != -1 :
                #just adding the header
                last_header_title = line
                fastaFormatData[line] = ''
            else:
                #adding the data
                if last_header_title != '':
                    fastaFormatData[last_header_title] += line

        return fastaFormatData
