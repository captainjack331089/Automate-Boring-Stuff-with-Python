import re

sample = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
new_s = agentNamesRegex.sub(r'\1**', sample)

print(agentNamesRegex.search(sample).group(2))
print(sample)
print(new_s)