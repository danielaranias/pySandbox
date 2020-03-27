import StringTool

def test_no_subStr_found():
    tool = StringTool.StringTool()
    pos_list = tool.findAllStrPos('the boy is here', 'girl')
    assert pos_list == []

def test_one_subStr_found():
    tool = StringTool.StringTool()
    pos_list = tool.findAllStrPos('the boy is here', 'boy')
    assert pos_list == [4]

def test_one_subStr_case_sensative_1_found():
    tool = StringTool.StringTool()
    pos_list = tool.findAllStrPos('the Boy is here', 'boy')
    assert pos_list == [4]

def test_one_subStr_case_sensative_2_found():
    tool = StringTool.StringTool()
    pos_list = tool.findAllStrPos('the boy is here', 'Boy')
    assert pos_list == [4]

def test_two_subStr_found():
    tool = StringTool.StringTool()
    pos_list = tool.findAllStrPos('the boy is here, boy', 'boy')
    assert pos_list == [4,17]

