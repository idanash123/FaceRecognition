# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time,os
def mse(imageA, imageB):
	# the 'Mean Squared Errr' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB, title):
     tic = time.time()
	# compute the mean squared error and structural similarity
     # index for the images
     imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
     imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
     imageB_color = cv2.cvtColor(imageB, cv2.COLOR_BGR2RGB)
     m = mse(imageA_gray, imageB_gray)
     s = ssim(imageA_gray, imageB_gray)
	# setup the figure
     fig = plt.figure(title)
     print m
     print s    
     plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
     if s >0.99 and m < 1:
         plt.suptitle("YES")
     elif s > 0.265 and m > 2510:
         plt.suptitle("YES")
     elif s > 0.25 and m > 4000:
         plt.suptitle("YES")        
     else:
        plt.suptitle("NO")
     ax = fig.add_subplot(1, 1, 1)
     plt.imshow(imageB_color, cmap = plt.cm.gray)
     plt.axis("off")
     print time.time()-tic
	# show the images
     plt.show()
    
# load the images -- the original, the original + contrast,
# and the original + photoshop
face = []
face_RGB = []
os.system("ls images/ |grep comp | grep .jpeg >aa")
file1 = open("aa","r")
line = file1.readline()
while not line == "" :
    line = line[:-1]
    print "images/"+line
    face.append(cv2.imread("images/"+line))
    line = file1.readline()
# convert the images to grayscale
for i in range(len(face)):
    face_RGB.append(cv2.cvtColor(face[i], cv2.COLOR_BGR2RGB))
# initialize the figure
fig = plt.figure("Images")
 
# loop over the images

for i in range(len(face)):
    # show the image
	ax = fig.add_subplot(1, len(face), i + 1)
	ax.set_title(str(i))
	plt.imshow(face_RGB[i], cmap = plt.cm.gray)
	plt.axis("off")
 
# show the figure
plt.show()

for i in range(len(face)):
    # compare the images
    compare_images(face[0], face[i], "Is this Idan?")

