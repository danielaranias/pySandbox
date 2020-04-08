

class StringTool:
    def findAllStrPos(self,mainStr:'the input string to work on', strToFind:'the string to find within the mainStr',IsCaseSesative = False) -> 'list of the found positions':
        """Returns all the strToFind positions within mainStr"""

        all_subStr_positions_list = []
        not_found_ch = 'www'.find('e')

        print('The entered string is:',mainStr)
        if IsCaseSesative == True:
            #converting the main str to lower case string using casefold for more aggressive lower action
            #in order to work with no case sensative"
            mainStr = mainStr.casefold()
            strToFind = strToFind.casefold()

        found_abs_pos = not_found_ch
        next_pos = 0

        #find the first posution of the dub str
        found_abs_pos = mainStr[next_pos:].find(strToFind)
        #run on the main str, untill nothing has found
        while found_abs_pos != not_found_ch:
            #since we found the absolute position we should add it to the last position we found
            next_pos += found_abs_pos
            #adding the position to the list
            all_subStr_positions_list.append(next_pos)
            #we need to pass over the word that we found
            next_pos += len(strToFind)
            #find the first posution of the dub str
            found_abs_pos = mainStr[next_pos:].find(strToFind)

        return all_subStr_positions_list


    def tokenizedSeq(self,seqList:'the list to tokenize each charecture')->'the tokenized Dict':
        tokenized_dict = {}

        #running on all charectures in the sequence and building a Dict
        for ch in seqList:
            if tokenized_dict.get(ch) == None:
                tokenized_dict[ch] = 1
            else:
                #adding one more to the counting number
                tokenized_dict[ch]+=1 
            
        return tokenized_dict

    def GetPrecentageOfCharecturesInSeq(self, charectureList:'the charecture List to look on the seq',seqList:'the sequence to check on')->'return the precentage':
        """Getting the precentage of a charecture list out of a sequence"""

        precentage = 0.0
        tokenized_dict = self.tokenizedSeq(seqList)
        total_other_ch_seq = 0
        total_charectureList_base = 0

        for ch in tokenized_dict:
            if ch in charectureList:
                total_charectureList_base += tokenized_dict[ch]
            else:
                total_other_ch_seq += tokenized_dict[ch] 

        if tokenized_dict.__len__() > 0:
            precentage = (total_charectureList_base/(total_charectureList_base + total_other_ch_seq))*100
        else:
            precentage = 0

        return precentage           


    def isSeqDNA(self,seqList:'the sequence to check on',DnaThreshold:'the precentage that above that it is a DNA'=90)->'return True if the majoruty of the Seq are DNA based':
        """ A practical getter to verify if a sequnce is a DNA or not according to a given threashold"""

        res = False
        precentage = 0.0
        dna_based = ['A','C','T','G']
        
        precentage = self.GetPrecentageOfCharecturesInSeq(dna_based,seqList)
        if precentage >= DnaThreshold:
            res = True
        else:
            res = False


        return res           

    