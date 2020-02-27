#splits the input by comma or period

regex_pattern = r",|\."	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

