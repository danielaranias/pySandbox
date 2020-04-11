

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

   
    def FastqBuilderFromFile(self,fileNamePath)-> 'return the multi fasta dict':
        """
        check if there is fasta header ('>') or not
        """
        import StringTool

        fastqHeader = '@'
        fastqData = {} #header : seq
        last_header_title =''
        fastq_states = ['SEQ_ID','SEQ','SEQ_ID_VERFICATION','SEQ_ENCODE']
        current_fastq_state = 0 #initial state

        listOfLists = self.read_fasta_file(fileNamePath)
        data = ['','','']

        for line in listOfLists:
            #finding the header
            if current_fastq_state == 0 and line.find(fastqHeader) != -1 :
                #just adding the header
                last_header_title = line
                fastqData[line] = data
                #increament the state
                #pos = (current_fastq_state +1)%fastq_states.__len__()
                current_fastq_state = (current_fastq_state +1)%fastq_states.__len__()

            # raw data    
            elif current_fastq_state == 1:
                data[0] = line
                fastqData[last_header_title] = data
                #increament the state
                current_fastq_state = (current_fastq_state +1)%fastq_states.__len__()

            #SEQ_ID verification
            elif current_fastq_state == 2:
                data[1]=line
                #increament the state
                current_fastq_state = (current_fastq_state +1)%fastq_states.__len__()

            #SEQ ENCODE 
            elif current_fastq_state == 3:
                data[2]=line
                #increament the state
                current_fastq_state = (current_fastq_state +1)%fastq_states.__len__()
                data = ['','','']

        return fastqData
