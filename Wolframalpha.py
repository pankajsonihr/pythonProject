import wolframalpha

import API

appId = API.wolf_appId
wolframClient = wolframalpha.Client(appId)
def listOrDict(var):
    if isinstance(var,list):
        return var[0]['plaintext']
    else:
        return var['plaintext']
def search_wolfram(query = ''):
    response = wolframClient.query(query)
    if response['@success'] == 'false':
        return 'something went wrong with calculation system'
    #query resolved then we will send following
    else:
        result = ""
        pod0 = response['pod'][0]
        pod1 = response['pod'][1]
        #pod: list of results. this also contains subpods
        if(('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') =='true') or ('definition' in pod1['@title'].lower()):

            result =listOrDict(pod1['subpod'])
            return result.split('(')[0]
        else:
            question = listOrDict(pod0['subpod'])
            #removing the bracket from the output
            # return question back to commit this same search from another locations
            return question.split('(')[0]
