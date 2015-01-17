import numpy as np
import cv2

def generate(cross_rect, rows, cols, w, h, values, taskName) :

  # min and max values for Squares with Numbers
  minVal = values[0]
  maxVal = values[1]

  # you need to uncomment these lines if your image is rotated
  #new_pts = np.float32([[0,0], [0,129],[129,129],[129,0]])
  #old_pts = max_approx.reshape(4,2).astype('float32')
  #M = cv2.getPerspectiveTransform(old_pts,new_pts)
  #cross_rect = cv2.warpPerspective(thresh2,M,(130,130))
  
  cross = np.zeros((rows, cols))
  numberCross = np.zeros((rows, cols))

  width = w
  height = h
  
  # sq = square
  
  sq_w = width/cols
  sq_h = height/rows
  
  sq_a = sq_w * sq_h

  k = 1

  # horizontal adjustment
  # could be 0 or 1
  ha = 0

  # select each box, if number of white pixels is more than 50, it is white box
  for i in xrange(rows):
      for j in xrange(cols):
          # box is defined by intersection of projections
          # cartesian plot
          # x increases from up to down
          # y increases form left to right
          # image[y1:y2, x1:x2]
          # rectangle: upper-left (x1,y1), low-right (x2,y2)
          #box = cross_rect[i*10:(i+1)*10, j*10:(j+1)*10]
          box = cross_rect[i*sq_h:(i+1)*sq_h, ha+j*sq_w:ha+(j+1)*sq_w]
  
          whiteQuota = 0
          blackQuota = 0
  
          whiteQuota = cv2.countNonZero(box)
          if whiteQuota > (sq_a/2) :
              cross.itemset((i,j), 1)
          blackQuota = sq_a - whiteQuota
          
          ##if ((i > -1) and (i < 1)) :
          ##    print( "[%d, %d] -> w: %d , b: %d" % (i, j, whiteQuota, blackQuota ) )
          ## identify squares with numbers
          if ( (blackQuota >= minVal) and (blackQuota <= maxVal) ):
              numberCross.itemset((i,j), k)
              k = k + 1
              print("[ %d, %d ]," % ((j+1), (i+1)) )
          ##    print("%d -> [%d, %d], b: %d" % (k, (j+1), (i+1), blackQuota ) )
  
  np.savetxt('./data/' + taskName + '/' + taskName + '-square-map.txt', cross, fmt='%1d', delimiter=', ')
  np.savetxt('./data/' + taskName + '/' + taskName + '-number-map.txt', numberCross, fmt='%2d', delimiter=', ')
