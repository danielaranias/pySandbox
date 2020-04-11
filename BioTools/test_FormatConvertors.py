
import unittest

from Convertors import FastaToBam

fasta_to_bam = FastaToBam()
FastaFolderPath = '/Users/danielaranias/Documents/Private/Code Sandbox/Py tests/BioTools/Files Formats'

def test_reading_empty_Fasta_file():
    
    fasta_file = FastaFolderPath + '/emptyFasta.fna'
    lines = fasta_to_bam.read_fasta_file(fasta_file)
    assert lines == []


def test_reading_non_empty_Fasta_file():
    
    fasta_file = FastaFolderPath + '/nonEmptyFasta.fna'
    lines = fasta_to_bam.read_fasta_file(fasta_file)
    assert lines != []

def test_non_valid_fasta_format():
    listOfLists = ['ashcfcgf','jghh']
    res = fasta_to_bam.isItValidFastaFile(listOfLists)
    assert res == False

def test_valid_fasta_format():
    listOfLists = ['ashcfcgf','> first header','jghh','> second header','ASADS','SDSD']
    res = fasta_to_bam.isItValidFastaFile(listOfLists)
    assert res == True
