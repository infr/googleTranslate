# googleTranslate
Python translation package

## Usage
```
import translate
data = "Tämä on suomeksi"
g = translate.googleTranslate(data)
json = g.getJSON()
print(json)
