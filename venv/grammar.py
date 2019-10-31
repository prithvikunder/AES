import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException

configuration = ProWritingAidSDK.Configuration()
configuration.host = 'https://api.prowritingaid.com'
# To get an API code with 500 test credits go to https://prowritingaid.com/en/App/Api
configuration.api_key['licenseCode'] = '9BA0B9E5-4368-4802-A4E8-C9674A20F0E5'


# create an instance of the API class
api_instance = ProWritingAidSDK.TextApi(ProWritingAidSDK.ApiClient('https://api.prowritingaid.com'))

wrong_sent = 'I go to the store and I bought milk'

try:
    api_request = ProWritingAidSDK.TextAnalysisRequest(wrong_sent,
                                                       ["grammar"],
                                                       "General",
                                                       "en")
    api_response = api_instance.post(api_request)
    
except ApiException as e:
    print("Exception when calling TextAnalysisRequest->get: %s\n" % e)
tags = api_response.result.tags
correct_sentence = wrong_sent
# Apply all the tags to the original string to get a corrected string 
# Important to work through the tags backward to that indexes don't change
for tag in reversed(tags):
    replacement = '' if tag.suggestions[0] == '(omit)' else tag.suggestions[0] 
    correct_sentence = correct_sentence[0:tag.start_pos] + replacement + correct_sentence[tag.end_pos+1:]
print('Incorrect Sentence')
print(wrong_sent)
print('Correct Sentence')
print(correct_sentence)
print('Done')