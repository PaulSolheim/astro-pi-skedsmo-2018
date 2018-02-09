import numpy as np
import cv2

# ---------------------------------------------------------
# Brute-Force Matching with ORB Descriptors
# ---------------------------------------------------------

class ORBMatcher:
    
    def __init__(self):
        # Initiate ORB detector
        self.orb = cv2.ORB_create()

    def match(self, trainFilename, queryFilename):

        try:
            img2 = cv2.imread(trainFilename,0)      # trainImage
            img1 = cv2.imread(queryFilename,0)      # queryImage

            # resize the queryImage
            r = 640.0 / img1.shape[1]
            dim = (640, int(img1.shape[0] * r))
             
            # perform the actual resizing of the image
            img1_resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

            # find the keypoints and descriptors with ORB
            kp1, des1 = self.orb.detectAndCompute(img1_resized,None)
            kp2, des2 = self.orb.detectAndCompute(img2,None)

            # create BFMatcher object
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

            # Match descriptors.
            matches = bf.match(des1,des2)

            # Sort them in the order of their distance.
            matches = sorted(matches, key = lambda x:x.distance)

            # Draw first x matches.
            img3 = cv2.drawMatches(img1_resized,kp1,img2,kp2,matches[:50],None, flags=2)

            # resize the image to save storage space
            r = 1024.0 / img3.shape[1]
            dim = (1024, int(img3.shape[0] * r))
             
            # perform the actual resizing of the image
            img3_resized = cv2.resize(img3, dim, interpolation = cv2.INTER_AREA)

            matchFilename = queryFilename.replace("img","match")
            
            # Save image showing the matching of features
            cv2.imwrite(matchFilename, img3_resized)
            
        ### catch the exceptions
        except Exception as ex:
            print("Error in orbmatcher match")
            print(ex)