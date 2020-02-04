# import the client library
from grammarbot import GrammarBotClient

# Creating the client
# ===================
client = GrammarBotClient()

# or, signup for an API Key to get higher usage limits here: https://www.grammarbot.io/
client = GrammarBotClient(api_key='KS9C5N3Y') # GrammarBotClient(api_key=my_api_key_here)

# you can even set the base URI to a different server
# client = GrammarBotClient(base_uri='http://backup.grammarbot.io:80')

# Analyzing the text
# ==================

# There is only one method to perform the analysis, viz. GrammarBotClient.check
# method.

text = 'For example in paragraph two it about @CAPS1 where he and how he that he "Passionate Cuban music.'

# check the text, returns GrammarBotApiResponse object
res = client.check(text)
print(res.matches)
match = res.matches
match0 = match[0]
print(match0.replacements)