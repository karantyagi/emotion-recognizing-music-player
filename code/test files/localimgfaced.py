

########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, cv2
import numpy as np

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
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,emotion',
}

# pathToFileInDisk = r'C:\Users\girls.jpg'
pathToFileInDisk = r'C:\Users\Karan Tyagi\Desktop\add to github\0 - hackbeanspot\code\girls.jpg'
with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()

try:
    # Execute the REST API call and get the response.
    response = requests.request('POST', uri_base + '/face/v1.0/detect', json=None, data=data, headers=headers, params=params)

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

'''if response is not None:
    # Load the original image, fetched from the URL
    data8uint = np.fromstring( data, np.uint8 ) # Convert string to an unsigned int array
    img = cv2.cvtColor( cv2.imdecode( data8uint, cv2.IMREAD_COLOR ), cv2.COLOR_BGR2RGB )
    cv2.imshow('preview',img)
    cv2.waitKey()'''

####################################
