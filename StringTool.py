

class StringTool:
    def findAllStrPos(self,mainStr, strToFind):
        """Returns all positions within mainStr
        that the strToFind is found"""

        all_subStr_positions_list = []
        not_found_ch = 'www'.find('e')

        print('The entered string is:',mainStr)
        #converting the main str to lower case string
        #in order to work with no case sensative"
        mainStr = mainStr.lower()
        strToFind = strToFind.lower()
        next_pos = 0


        #run on the main str, finding the next position that strToFind is found
        for x in range (next_pos,len(mainStr)):

            found_abs_pos = mainStr[next_pos:].find(strToFind)
            #since we found the absolute position we should add it to the last position we found
            next_pos += found_abs_pos

            if found_abs_pos == not_found_ch:
                return all_subStr_positions_list
            else:
                #adding the position to the list
                all_subStr_positions_list.append(next_pos)
                #we need to pass the word that we founs
                next_pos += len(strToFind)
                