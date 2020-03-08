import keras
from keras.models import load_model
import cv2
import numpy as np

class Vision:
    def __init__(self):
        self.model=load_model("model.h5")
    def pred(self, img):
        img=cv2.resize(img,(128,128))
        p=self.model.predict(img)
        m=max(p)
        for i in range(len(m)):
            if p[i]==m:
                s=i
        key=['melanoma','nevus','seborrheic_keratosis']
        return key[i]
    def getimg(self,url):
        img=cv2.imread(url,1)
        return img