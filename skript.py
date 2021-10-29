# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 00:12:46 2021

@author: ahmet
"""
import random

#sadece gerekli fonksiyonlari kütüphaneden cagiriyorum
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeAudioClip, AudioFileClip

u = int(input("kesitler kac saniye olsun: "))
ks = int(input("Kac klip olsun: "))

#ses ve video konumlarini belirt
clip = VideoFileClip("video.mp4")
ses = AudioFileClip("music.mp3")

#ses ve video sürelerini al
cs = int(clip.duration)
ss = int(ses.duration)

# videodan rastgele parcalar al
l1 = random.sample(range(30, cs), ks+1)
l2 = [x+u+random.randint(0,2) for x in l1]
    
y =[]
a = dict()

for i in range(ks+1):
    y.append([l1[i], l2[i]])
y.pop(0)

for j in range(0,ks):
    a[j] = clip.subclip(y[j][0],y[j][1])
        
#parcalari birlestir
clipk1 = concatenate_videoclips([a[k] for k in range(ks)])

#ses ekle ve birlestir
yenises = CompositeAudioClip([ses])
c1s = int(clipk1.duration)
clipk1.audio = yenises

#son kez kirp
clipk1 = clipk1.subclip(0,c1s)

#kaydet ya da onizle
clipk1.ipython_display(width = 360)



