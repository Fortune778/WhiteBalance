# White patch reference 
# How about picking a patch of image that is supposed to be white
# and using it as reference to rescale each channel in the image

import cv2 
px, py = 0, 0


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(f'x = {x}, y = {y}')
        global px,py
        px, py = x, y
        

 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)

def Convert2WhiteBalance(clone):
    # For human1.jpg px, py, 10, 10 
    h_start, w_start, h_width, w_width = py, px, 10, 10 
    image = clone
    image_patch = image[h_start:h_start+h_width, 
                        w_start:w_start+w_width]

    # Get maximum pixel values from each channel (BGR), normalize the original image
    # with these max pixel vlaues - assuming the max pixel is white. 
    image_normalized = image / image_patch.max(axis=(0, 1))
    # print(image_normalized.max())
    # Some values will be above 1, so we need to clip the values to between 0 and 1
    image_balanced = image_normalized.clip(0,1)

    cv2.rectangle(clone, (w_start, h_start), (w_start+w_width, h_start+h_width), (0,0,255), 2)
    cv2.imshow("Image GW Balanced", image_balanced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(img):

# reading the image
    clone = img.copy() 

# display a clickable image.
# click where it is supposed to be white. 
    cv2.imshow('image', img)
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    Convert2WhiteBalance(clone)
    






if __name__ == '__main__':
    # Change the picture which you want
    img = cv2.imread("human1.jpg")
    main(img)