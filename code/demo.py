
########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, cv2
import numpy as np
import cv2
import os
import keyboard

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
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'smile,emotion',
}


def find_emotions(path):
    # pathToFileInDisk = r'C:\Users\girls.jpg'
    pathToFileInDisk = r'C:\Users\Karan Tyagi\Desktop\add to github\0 - hackbeanspot\code\{}'.format(path)
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()


    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=None, data=data, headers=headers, params=params)
        # print ('Response:')
        parsed = json.loads(response.text)
        # print (json.dumps(parsed, sort_keys=True, indent=2))
        frame_num = 1;

        for face in parsed:
            #print(' Frame {} :\t'.format(frame_num),face['faceAttributes']['emotion'])
            #print(' Smile {} :\t'.format(fno),face['faceAttributes']['smile'])
            sum = (face['faceAttributes']['emotion']['happiness'] + face['faceAttributes']['emotion']['sadness']
            + face['faceAttributes']['emotion']['neutral'] + face['faceAttributes']['emotion']['fear'] +
            face['faceAttributes']['emotion']['disgust'] + face['faceAttributes']['emotion']['contempt'] +
            face['faceAttributes']['emotion']['anger'])
            print('\t{}'.format(face['faceAttributes']['emotion']['happiness']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['surprise']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['neutral']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['sadness']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['disgust']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['anger']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['contempt']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['fear']).ljust(18)+'{}'.format(sum))
            frame_num+=1
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


cv2.namedWindow("preview")
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

img_counter = 1

print('\n\tHappiness'.ljust(18)+'Surprise'.ljust(18)+'Neutral'.ljust(18)+'Sadness'.ljust(18)+'Disgust'.ljust(18)+'Anger'.ljust(18)+'Contempt'.ljust(18)+'Fear'.ljust(18))
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    img_name = "img_frame{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)

    # print("Created img_frame{}.jpg".format(img_counter))

    # print(type(frame))

    # start processing the image emotions
    if keyboard.is_pressed('p'):
        find_emotions(img_name)
        key = cv2.waitKey() # milliseconds
    else:
        key = cv2.waitKey() # milliseconds
    # take less frames
    # end processing this frame

    # deleting the image after processing it
    # print("Deleted img_frame{}.jpg".format(img_counter))

    # this can be put in a try catch box
    ## if file exists, delete it ##
    if os.path.isfile(img_name):
        os.remove(img_name)
    else: ## Show an error ##
        print("Error: %s file not found" % myfile)
    img_counter+=1

    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()





####################################
