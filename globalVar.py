import re
regxOptionsABCDE = r'[\(\（][ \t]*([ABCDEabcde])[ \t]*[\)\）]'  # 查找题目选项
regxOptionsABCDE_except = r'[\(\（][ \t]*[ABCDEabcde][ \t]*[\)\）]:*(.+)'  # 查找题目选项中的内容
regxAnswer = r'答[ \n]*案\W*(\w*)'
regexIsUrl = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)