import re
def hackerrankInString(s):
    return 'YES' if re.search(r".*"+".*".join(list("hackerrank")) + ".*",s) else 'NO'
    