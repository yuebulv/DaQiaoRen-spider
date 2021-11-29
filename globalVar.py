import re
regxOptions_group = r"(?<!^)(?=(（|\()[ABCDEabcde](）|\)))"  # 如果str中含有（A***（B***时，分成[（A***,（B***]
regxOptionsABCDE = r'[\(\（][ \t]*([ABCDEabcde])[ \t]*[\)\）]'  # 查找题目选项,例（A)*** 中提取出A
regxOptionsABCDE_except = r'[\(\（][ \t]*[ABCDEabcde][ \t]*[\)\）]:*(.+)'  # 查找题目选项中的内容,例（A)*** 中提取出***
regxAnswer = r'答[ \n]*案\W*(\w*)'
regexIsUrl = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # 判断网址格式是否正确