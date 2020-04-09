
def Test_StrinTool():

    def __init__(self):
        import StringTool
        import Decorators

        tool = StringTool.StringTool()

    def test_empty_str():
        pos_list = tool.findAllStrPos('', 'boy')
        assert pos_list == []

    def test_no_subStr_found():
        pos_list = tool.findAllStrPos('the boy is here', 'girl')
        assert pos_list == []

    def test_one_subStr_found():
        pos_list = tool.findAllStrPos('the boy is here', 'boy')
        assert pos_list == [4]

    def test_one_subStr_case_sensative_1_found():
        pos_list = tool.findAllStrPos('the Boy is here', 'boy')
        assert pos_list == []

    def test_one_subStr_case_sensative_true_1_found():
        pos_list = tool.findAllStrPos('the Boy is here', 'boy',True)
        assert pos_list == [4]

    def test_one_subStr_case_sensative_2_found():
        pos_list = tool.findAllStrPos('the boy is here', 'Boy')
        assert pos_list == []

    def test_one_subStr_case_sensative_true_2_found():
        pos_list = tool.findAllStrPos('the boy is here', 'Boy',True)
        assert pos_list == [4]

    def test_two_subStr_found():
        pos_list = tool.findAllStrPos('the boy is here, boy', 'boy')
        assert pos_list == [4,17]

    def test_tokenize_none():
        pos_list = tool.tokenizedSeq('')
        assert pos_list == {}

    def test_tokenize_one():
        pos_list = tool.tokenizedSeq('a')
        assert (pos_list['a'] == 1 and pos_list.__len__()== 1)


    def test_tokenize_many_ch():
        pos_list = tool.tokenizedSeq('aba!p Yya')
        assert (pos_list['a'] == 3 and 
                pos_list['b'] == 1 and
                pos_list['!'] == 1 and
                pos_list['p'] == 1 and
                pos_list['Y'] == 1 and
                pos_list['y'] == 1 and
                pos_list[' '] ==1 and
                pos_list.__len__()== 7
                )


    def test_seq_no_DNA_less_than_defualt():
        res = tool.isSeqDNA('ACTGCCu')
        assert res == False

    def test_seq_is_DNA():
        res = tool.isSeqDNA('ACTGCCu',80)
        assert res == True

    def test_seq_not_DNA():
        res = tool.isSeqDNA('ACyytnposnhu')
        assert res == False
        




