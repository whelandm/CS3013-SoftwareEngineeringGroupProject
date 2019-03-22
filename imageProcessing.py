#imports - just open cv atm
import cv2
import glob # reading images from local folder

#remove the red and blue value from each pixel
def remove_RB(image):
    rows,columns,channels = image.shape
    for x in range(rows):
        for y in range(columns):
            image[x, y, 0] = 0 # remove red value
            image[x, y, 2] = 0 # remove blue value
    return image

#islates hand and creates mask (current sweet spot 130-150 blue value)
def isolate_hand(image):
    rows,columns,channels = image.shape
    count = 0
    for x in range(rows):
        for y in range(columns):
            # check if blue is greater than 125, changed to black
            if(image[x, y, 2] <= 150):
                image[x, y, 0] = 0
                image[x, y, 1] = 0
                image[x, y, 2] = 0
            else:
                count += 1 #count of hand pixels
    return image, count

#counts pixels where gel present, current sweetspot green channel > 5
def count_coverage(image):
    rows,columns,channels = image.shape
    count = 0
    for x in range(rows):
        for y in range(columns):
            if (image[x, y, 1] > 5):
                count += 1
    return count

#TESTING
path = glob.glob('handwash/*.jpg') #import images from folder stored in path
image_list = []
for file in path:
    image = cv2.imread(file) #read image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convert to RGB
    image_list.append(image) #adds image to list
test = image_list[4]
mask, count = isolate_hand(test)
result = remove_RB(mask)
coverage = count_coverage(result)
percent = coverage/count
print(percent)
