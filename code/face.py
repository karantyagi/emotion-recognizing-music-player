

########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'a964c99ef5a944d99e2d50e1fea958d0'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,emotion',
}

# Body. The URL of a JPEG image to analyze.
body = {'url': 'https://i.pinimg.com/736x/cf/70/ce/cf70ce32f1981d64ed82875772e33dfa--group-senior-pictures-senior-picture-poses.jpg'}
# body = {'url': 'opencv_frame_1.jpg'}



try:
    # Execute the REST API call and get the response.
    response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)

    print ('Response:')
    parsed = json.loads(response.text)
    # print (json.dumps(parsed, sort_keys=True, indent=2))
    fno = 1;
    for face in parsed:
        print(' Face {} :\t'.format(fno),face['faceAttributes']['emotion'])
        fno+=1
    # print(type(parsed[0]))
    #print(len(parsed))

except Exception as e:
    print('Error:')
    print(e)

####################################
