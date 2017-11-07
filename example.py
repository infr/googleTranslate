import translate
with open('data.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

# Pass any string in the data variable:
g = translate.googleTranslate(data)
json = g.getJSON()

print(json)