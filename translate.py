'''
Usage
import translate
with open('data.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

t = translate.googleTranslate(data)
t.printTranslation()
json = t.getJSON()

Normal API: https://translation.googleapis.com/language/translate/v2?q=sourceText&target=en&format=text&source=fi&key={YOUR_API_KEY}
Free API: https://translate.googleapis.com/translate_a/single?client=gtx&sl="+ sourceLang + "&tl=" + targetLang + "&dt=t&q=" + encodeURI(sourceText);
'''
import http.client, urllib.request, urllib.parse, urllib.error, base64, json
class googleTranslate():
    def __init__(self, text=""):
        self.use_free = True
        self.params = ""
        self.data = ""
        self.setParams(text)
        self.getTranslation()
        
    def setParams(self, text):
        if not self.use_free:
            # Get api key from here
            # https://console.cloud.google.com/apis/library/translate.googleapis.com/?project=api-project-394734819633
            self.api_key = 'ADD_YOUR_KEY'
            self.uri_base = 'translation.googleapis.com'
            self.params = urllib.parse.urlencode({
                'target': 'en',
                'format': 'text',
                'source': 'fi',
                'q': text,
                'key': self.api_key,
            })
            self.request = "/language/translate/v2?%s" % self.params
        else:
            self.uri_base = 'translate.googleapis.com'
            self.params = urllib.parse.urlencode({
                'client':'gtx',
                'tl': 'en',
                'format': 'text',
                'sl': 'fi',
                'dt': 't',
                'q': text,
            })
            self.request = "/translate_a/single?%s" % self.params

    def getTranslation(self):
        try:
            conn = http.client.HTTPSConnection(self.uri_base)
            conn.request("POST", self.request)
            response = conn.getresponse()
            self.data = response.read()
            conn.close()

        except Exception as e:
            print('Error:')
            print(e)
            
    def printTranslation(self):
        parsed = json.loads(self.data)
        print (json.dumps(parsed, sort_keys=True, indent=2))

    def getJSON(self):
        return json.loads(self.data)
