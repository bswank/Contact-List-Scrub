# Find & replace multi-line data in newsletter recipeint list for HubSpot from Salesforce (Liberty HealthShare)

import fileinput
import re

scrubbedData = ''

print('\nPerforming magic.')

for line in fileinput.input('list.csv'):
	line = re.sub(r'([^"]$)\s?\R*(.*)', r'\1\2', line)
	scrubbedData += line

saveFile = open("scrubbedList.csv", "w")
saveFile.write(scrubbedData)
saveFile.close()

lines = open('scrubbedList.csv').readlines()
open('scrubbedList.csv', 'w').writelines(lines[:-7]) # Get rid of meta data at end of file

print('\nDone.\n\nFind the scrubbed file, named "scrubbedList.csv," in the same directory from which you ran this script. -Sprockets\n')