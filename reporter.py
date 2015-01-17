import numpy as np
import cv2
import operator

def report(cross_rect, rows, cols, w, h) :

  blackQuotas = np.zeros((rows, cols))

  width = w
  height = h
  
  # sq = square
  
  sq_w = width/cols
  sq_h = height/rows
  
  sq_a = sq_w * sq_h

  # horizontal adjustment
  # could be 0 or 1
  ha = 0

  blackQuotaFreqs = {}

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
          blackQuota = sq_a - whiteQuota
          blackQuotas.itemset((i,j), blackQuota)

          blackQuotaFreq = int(blackQuotas[i][j])
          if str(blackQuotaFreq) in blackQuotaFreqs :
              blackQuotaFreqs[str(blackQuotaFreq)] += 1
          else :
              blackQuotaFreqs[str(blackQuotaFreq)] = 1
  
  sortedFreqs = sorted(blackQuotaFreqs.items(), key=operator.itemgetter(1), reverse=True)

  moreFrequent = sortedFreqs.pop(0)
  secondMoreFrequent = sortedFreqs.pop(0)

  realValues = []

  for key,freq in sortedFreqs:
      realValues.append(int(key))

  sortedValues = sorted(realValues)

  minVal = sortedValues[0]
  maxVal = sortedValues[-1]
  values = [minVal, maxVal]

  return values
