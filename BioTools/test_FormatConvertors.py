
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

def test_building_fasta_from_non_valid_fasta_seq():
    listOfLists = ['ashcfcgf','jghh']
    fasta_dict = fasta_to_bam.FastaBuilderFromLists(listOfLists)
    assert fasta_dict == {}

def test_building_fasta_from_valid_fasta_seq():
    listOfLists = ['ashcfcgf','> first header','jghh','> second header','ASADS','SDSD']
    fasta_dict = fasta_to_bam.FastaBuilderFromLists(listOfLists)
    assert fasta_dict == {'> first header':'jghh','> second header':'ASADSSDSD'}


def test_building_fasta_from_valid_fasta_file():
    
    fasta_file = FastaFolderPath + '/validFasta.fna'
    fasta_dict = fasta_to_bam.  FastaBuilderFromFile(fasta_file)
    assert fasta_dict != {}
