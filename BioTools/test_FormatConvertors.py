
import unittest

from Convertors import Fasta
from Convertors import Fastq

fasta = Fasta()
fastq = Fastq()
FastaFolderPath = '/Users/danielaranias/Documents/Private/Code Sandbox/Py tests/BioTools/Files Formats'

def test_reading_empty_Fasta_file():
    
    fasta_file = FastaFolderPath + '/emptyFasta.fna'
    lines = fasta.read_file_data(fasta_file)
    assert lines == []


def test_reading_non_empty_Fasta_file():
    
    fasta_file = FastaFolderPath + '/nonEmptyFasta.fna'
    lines = fasta.read_file_data(fasta_file)
    assert lines != []

def test_building_seq_dict_from_non_valid_fasta_seq():
    listOfLists = ['ashcfcgf','jghh']
    fasta_dict = fasta.FromListsToSeqDict(listOfLists)
    assert fasta_dict == {}

def test_building_seq_dict_from_valid_fasta_seq():
    listOfLists = ['ashcfcgf','> first header','jghh','> second header','ASADS','SDSD']
    fasta_dict = fasta.FromListsToSeqDict(listOfLists)
    assert fasta_dict == {'> first header':'jghh','> second header':'ASADSSDSD'}


def test_building_seq_dict_from_valid_fasta_File():
    
    fasta_file = FastaFolderPath + '/validFasta.fna'
    fasta_dict = fasta.FromFileToSeqDict(fasta_file)
    assert fasta_dict != {}

def test_building_seq_dict_from_valid_fastq_File():
    fastq_file = FastaFolderPath + '/validFastq.fna'
    fastq_dict = fastq.FromFileToSeqDict(fastq_file)
    assert fastq_dict != {}