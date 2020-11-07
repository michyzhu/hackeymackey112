from getStatistics import *
import random

def generateQuoteAndSource(query):
    sourcesSet = getURLs(query) 
    sourceQuoteDict = lookThroughSources(sourcesSet)
    source1, quotes = random.choice(list(sourceQuoteDict.items()))
    randSourceEntry = random.choice(list(quotes))
    print("separate")
    print(source1, randSourceEntry)
    return (source1, randSourceEntry)


zipcode = 1
name = 2
state = 3
issue = 4
personemail = 5
senator = 6

#i need
statusAbout = 7
stance = 8
source1, content1 = generateQuoteAndSource("abortion")
source2, content2 = generateQuoteAndSource("abortion")



emailText = f'''Dear Congress Person {senator}:
My name is {name} and I reside at [Insert Your Address] in [Insert Your City], South Carolina.  I am {statusAbout}.  
I am writing you about {issue}, and asking that you stand {stance} it. 
This issue is important to me because:
According to {source1}, \" {content1}\"
And according to {source2}, \" {content2}\"
I appreciate your help and ask that you please send me a response letting me know if you are able to pass a Bill that would improve lives of American citizens like me.
Thank you for your time and considering my request.
Sincerely,
{name}
'''
