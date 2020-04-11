
import StringTool
from Decorators  import PrintFuncDuritionTime

@PrintFuncDuritionTime
def sum(a,b):
    print ('the sum is {0}'.format(a+b))



    
def main():
    print('STARTING')  

    from BioTools.Convertors import FastaToBam
    
    fasta_to_bam = FastaToBam()
    FastaFolderPath = '/Users/danielaranias/Documents/Private/Code Sandbox/Py tests/BioTools/Files Formats'
    fasta_file = FastaFolderPath + '/validFasta.fna'
    fasta_dict = fasta_to_bam.  FastaBuilderFromFile(fasta_file)
    
    for header in fasta_dict:
        print('Here is a FASTA header: {0}'.format(header))
        print('Related Seq:\n{0}'.format(fasta_dict[header]))


    
    fastq_file = FastaFolderPath + '/validFastq.fna'
    fastq_dict = fasta_to_bam.FastqBuilderFromFile(fastq_file)
    
    for header in fastq_dict:
        print('Here is a FASTQ header: {0}'.format(header))
        print('Related Seq:\n{0}'.format(fastq_dict[header]))




    
if __name__ == "__main__":
    main()