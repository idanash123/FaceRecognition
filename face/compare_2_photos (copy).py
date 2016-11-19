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
os.system("ls images\ |grep comp | grep .jpeg >aa")
file1 = open("images\aa","rb")
line = file1.readline()
while not line == "" :
    face.append(cv2.imread(line))
    line = file1.readline()
face1 = cv2.imread("comp1.jpeg")
face2 = cv2.imread("comp2.jpeg")
face3 = cv2.imread("comp3.jpeg")
face4 = cv2.imread("comp4.jpeg")
face5 = cv2.imread("comp5.jpeg")
face6 = cv2.imread("comp6.jpeg")
face7 = cv2.imread("comp7.jpeg")
face8 = cv2.imread("comp8.jpeg")
face9 = cv2.imread("comp9.jpeg")
face10 = cv2.imread("comp10.jpeg")
face11 = cv2.imread("comp11.jpeg")



# convert the images to grayscale
face1_gray = cv2.cvtColor(face1, cv2.COLOR_BGR2GRAY)
face2_gray = cv2.cvtColor(face2, cv2.COLOR_BGR2GRAY)
face3_gray = cv2.cvtColor(face3, cv2.COLOR_BGR2GRAY)
face4_gray = cv2.cvtColor(face4, cv2.COLOR_BGR2GRAY)
face5_gray = cv2.cvtColor(face5, cv2.COLOR_BGR2GRAY)
face6_gray = cv2.cvtColor(face6, cv2.COLOR_BGR2GRAY)
face7_gray = cv2.cvtColor(face7, cv2.COLOR_BGR2GRAY)
face8_gray = cv2.cvtColor(face8, cv2.COLOR_BGR2GRAY)
face9_gray = cv2.cvtColor(face9, cv2.COLOR_BGR2GRAY)
face10_gray = cv2.cvtColor(face10, cv2.COLOR_BGR2GRAY)
face11_gray = cv2.cvtColor(face11, cv2.COLOR_BGR2GRAY)


face1_ = cv2.cvtColor(face1, cv2.COLOR_BGR2RGB)
face2_ = cv2.cvtColor(face2, cv2.COLOR_BGR2RGB)
face3_ = cv2.cvtColor(face3, cv2.COLOR_BGR2RGB)
face4_ = cv2.cvtColor(face4, cv2.COLOR_BGR2RGB)
face5_ = cv2.cvtColor(face5, cv2.COLOR_BGR2RGB)
face6_ = cv2.cvtColor(face6, cv2.COLOR_BGR2RGB)
face7_ = cv2.cvtColor(face7, cv2.COLOR_BGR2RGB)
face8_ = cv2.cvtColor(face8, cv2.COLOR_BGR2RGB)
face9_ = cv2.cvtColor(face9, cv2.COLOR_BGR2RGB)
face10_ = cv2.cvtColor(face10, cv2.COLOR_BGR2RGB)
face11_ = cv2.cvtColor(face11, cv2.COLOR_BGR2RGB)

# initialize the figure
fig = plt.figure("Images")
images = ("face1", face1_), ("face2", face2_), ("face3", face3_) ,("face4", face4_) ,("face5", face5_), ("face6", face6_),("face7", face7_),("face8", face8_),("face9", face9_),("face10", face10_),("face11", face11_)   
 
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 11, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
 
# show the figure
plt.show()
 
# compare the images
compare_images(face1, face1, "Is this Idan?")
ocompare_images(face1, face2, "Is this Idan?")
compare_images(face1, face3, "Is this Idan?")
compare_images(face1, face4, "Is this Idan?")
compare_images(face1, face5, "Is this Idan?")
compare_images(face1, face6, "Is this Idan?")
compare_images(face1, face7, "Is this Idan?")
compare_images(face1, face8, "Is this Idan?")
compare_images(face1, face9, "Is this Idan?")
compare_images(face1, face10, "Is this Idan?")
compare_images(face1, face11, "Is this Idan?")

