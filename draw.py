"""
200201 jc start
環境:mmn_test1(selfPC)

"""

import csv
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


# 開啟 CSV 檔案
with open('D://draw_test//after_clean.txt', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  
  #類別定義 
  uc = 0 #UseComputer
  up= 0 #UsePhone
  d = 0 #discuss
  r = 0 #read
  t =0 #think
  lo=0 #LookOther
  ho=0 #HelpOther
  le=0 #leave
  nd=0 #not define

  
  # 以迴圈輸出指定欄位
  for row in rows:
    
    if row[2] != "" :
      if row[2]==" discuss" :
          d=d+1
      elif row[2]==" read" :
          r=r+1
      elif row[2]==" UseComputer" :  
          uc=uc+1
      elif row[2]==" UsePhone" :  
          up=up+1 
      elif row[2]==" think" :  
          t=t+1
      elif row[2]==" LookOther" :  
          lo=lo+1
      elif row[2]==" HelpOther" :  
          ho=ho+1 
      elif row[2]==" leave" :  
          le=le+1
      else :
          nd=nd+1
    
 
x = ["discuss","HelpOther","leave","LookOther","read","think","UseComputer","UsePhone","not define"]
y = [d,ho,le,lo,r,t,uc,up,nd]
plt.barh(x, y)    #畫長條圖
plt.show()        #出現畫面