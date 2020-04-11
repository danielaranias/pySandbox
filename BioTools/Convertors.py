

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
            #print(lines)

        return  lines

    def isItValidFastaFile(self,listOfLists)-> 'return True or Flase':
        """
        check if there is fasta header ('>') or not
        """
        res = False
        import StringTool
        #strTool = StringTool.StringTool() 
        fastaHeader = '>'
        fastaFormatData = {} #header : seq
        last_header_title =''
        #header_was_found = False
        #seq_data = ''

        for line in listOfLists:
            if line.find(fastaHeader) != -1 :
                #just adding the header
                last_header_title = line
                fastaFormatData[line] = ''
            else:
                #adding the data
                if last_header_title != '':
                    fastaFormatData[last_header_title] += line

        
        if fastaFormatData != {}:
            res = True 

        return res
