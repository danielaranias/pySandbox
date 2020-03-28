

class StringTool:
    def findAllStrPos(self,mainStr, strToFind):
        """Returns all positions within mainStr
        that the strToFind is found"""

        all_subStr_positions_list = []
        not_found_ch = 'www'.find('e')

        print('The entered string is:',mainStr)
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
                