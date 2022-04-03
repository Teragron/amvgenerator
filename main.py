import random
import PySimpleGUI as sg
import os.path
from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join
import glob
import itertools
import timeit
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeAudioClip, AudioFileClip



def func(message):
    print(message)
    
    
    
layout1 = [     
    
     [sg.Text('1) Choosing number and duration of miniclips part', size=(45, 1),background_color= "#92A8D1", font=("Bookerly", 12, "bold"))],
     [sg.Text('¯'  * 350, size=(65, 1),  background_color='#92A8D1')],
    
    [sg.Text("Duration of miniclips", size=(17, 1),background_color= "#92A8D1" ,font=("Bookerly", 10, "bold")),
            sg.Input(do_not_clear=True, key = "-INPI1-",size=(40, 2)),  sg.Button("Confirm", key = "-MINIDUR-",size=(30, 1))
          ],
         [
             sg.Text("Number of  miniclips", size=(17, 1),background_color= "#92A8D1" ,font=("Bookerly", 10, "bold")),
            sg.Input(do_not_clear=True, key = "-INPI2-",size=(40, 2)),  sg.Button("Confirm", key = "-MININUM-",size=(30, 1))
          ],

    
    
     [sg.Text('2) Video choosing part', size=(25, 1),background_color= "#92A8D1", font=("Bookerly", 12, "bold"))],
        [sg.Text('¯'  * 300, size=(65, 1),  background_color='#92A8D1')],
    
    [sg.Text('Path of first video', size=(17, 1),background_color= "#92A8D1" ,font=("Bookerly", 10, "bold")),
     
             sg.In(size=(40, 2), enable_events=True, key="-VIDEO1-"), 
            sg.FileBrowse("Choose first video",size=(30, 1), file_types=(("Video files", "*.mp4"),))],
    
        [sg.Text('Path of second video', size=(17, 1),background_color= "#92A8D1" ,font=("Bookerly", 10, "bold")), sg.In(size=(40, 2), enable_events=True, key="-VIDEO2-"), 
            sg.FileBrowse("Choose second video",size=(30, 1), file_types=(("Video files", "*.mp4"),))],
    
    
        [sg.Text('Path of third video', size=(17, 1),background_color= "#92A8D1" ,font=("Bookerly", 10, "bold")), sg.In(size=(40, 2), enable_events=True, key="-VIDEO3-"), 
            sg.FileBrowse( "Choose third video",size=(30, 1), file_types=(("Video files", "*.mp4"),))],
    
    
     [sg.Text('3) Concatenating part', size=(45, 1),background_color= "#92A8D1", font=("Bookerly", 12, "bold"))],
    [sg.Text('¯'  * 350, size=(65, 1),  background_color='#92A8D1')],
    
    [sg.Button("Concatenate video clips", key = "-CONCAT-",size=(67, 1))],
    
     [sg.Text('4) Audio choosing part', size=(45, 1),background_color= "#92A8D1", font=("Bookerly", 12, "bold"))],
    [sg.Text('¯'  * 350, size=(65, 1),  background_color='#92A8D1')],
            
    [sg.Text("Path of soundtrack", size=(17, 1),background_color= "#92A8D1" ,font=("Bookerly", 10, "bold")), sg.In(size=(40, 2), enable_events=True, key="-AUDIO-"), 
            sg.FileBrowse("Choose soundtrack",size=(30, 1), file_types=(("Audio Files", "*.mp3"),)), 
            ] ,
    
    [sg.Checkbox("Add random time effect (base time + 0-2 sec.)", default=False, key= "-RANDTIME-")],
    
    
        [sg.Text('5) Save path choosing part', size=(45, 1),background_color= "#92A8D1", font=("Bookerly", 12, "bold"))],
    [sg.Text('¯'  * 350, size=(65, 1),  background_color='#92A8D1')],
            [sg.Text("Edit will be saved here", size=(18, 1),background_color= "#92A8D1" ,font=("Bookerly", 10, "bold")),
            sg.In(size=(40, 2), enable_events=True, key="-SAVEFOLDER-"), 
             sg.FolderBrowse("Choose save folder",size=(30, 1))]
          ,

    
     [sg.Text('6) Generating part', size=(45, 1),background_color= "#92A8D1", font=("Bookerly", 12, "bold"))],
    [sg.Text('¯'  * 350, size=(65, 1),  background_color='#92A8D1')],
            [
            sg.Button("Generate", key = "-GENBUT-",size=(67, 1))
          ]




]







window = sg.Window('AMV Generator', layout= layout1, margins=(100, 50), background_color= "#92A8D1")

while True:             
    try:  
        event, values = window.Read()
        if event in (None, 'Exit'):
            break

        elif event == '-MINIDUR-':
            minidur = 0
            minidur = int(values['-INPI1-'])

            if 1<minidur <999:
                sg.Popup("Size has been saved")


        elif event == '-MININUM-':
            mininum = 0
            mininum = int(values['-INPI2-'])

            if 1<mininum<99:
               # func("mininum: {}".format(mininum))
                sg.Popup("Size has been saved")


        elif event == '-VIDEO1-':
            videovalue1 = values['-VIDEO1-']
            video_obj1 = VideoFileClip("{}".format(videovalue1))
            cs1 = int(VideoFileClip("{}".format(videovalue1)).duration)
            #func(type(cs1))
            #func(cs1)

        elif event == '-VIDEO2-':
            videovalue2 = values['-VIDEO2-']
            video_obj2 = VideoFileClip("{}".format(videovalue2))
            cs2 = int(VideoFileClip("{}".format(videovalue2)).duration)
          #  func(type(cs2))
          #  func(cs2)

        elif event == '-VIDEO3-':
            videovalue3 = values['-VIDEO3-']
            video_obj3 = VideoFileClip("{}".format(videovalue3))
            cs3 = int(VideoFileClip("{}".format(videovalue3)).duration)
          #  func(type(cs3))
           # func(cs3)

        elif event == '-AUDIO-':
            audiovalue = values['-AUDIO-']
            audio_obj = AudioFileClip("{}".format(audiovalue))
            ss = int(AudioFileClip("{}".format(audiovalue)).duration)
           # func(type(ss))
            #func(ss)

        elif event == "-SAVEFOLDER-":
            savevalue = values['-SAVEFOLDER-']

        elif event == '-CONCAT-':

            if "video_obj1" in locals() and "video_obj2" in locals() and "video_obj3" in locals():
                video_obj1 = video_obj1.set_fps(30)
                video_obj2 = video_obj2.set_fps(30)
                video_obj3 = video_obj3.set_fps(30)

                clips = [video_obj1, video_obj2, video_obj3]
                clip = concatenate_videoclips(clips, method="compose")
                sg.Popup("Videos are concatenated (1-2-3)")
                cs = cs1+cs2+cs3
                del video_obj1, video_obj2, video_obj3

            elif "video_obj1" in locals() and not ("video_obj2" in locals()) and not ("video_obj3" in locals()) :

                clip = video_obj1
                cs = cs1
                del video_obj1

            elif "video_obj2" in locals() and not ("video_obj1" in locals()) and not ("video_obj3" in locals()) :
                clip = video_obj2
                cs = cs2
                del video_obj2

            elif "video_obj3" in locals() and not ("video_obj1" in locals()) and not ("video_obj2" in locals()) :
                clip = video_obj3
                cs = cs3
                del video_obj3

            elif "video_obj1" in locals() and "video_obj2" in locals() and not ("video_obj3" in locals()):
                video_obj1 = video_obj1.set_fps(30)
                video_obj2 = video_obj2.set_fps(30)
                clips = [video_obj1, video_obj2]
                clip = concatenate_videoclips(clips, method="compose")
                sg.Popup("Videos are concatenated (1-2)")
                cs = cs1+cs2
                del video_obj1,video_obj2

            elif "video_obj1" in locals() and "video_obj3" in locals() and not ("video_obj2" in locals()):
                video_obj1 = video_obj1.set_fps(30)
                video_obj3 = video_obj3.set_fps(30)
                clips = [video_obj1, video_obj3]
                clip = concatenate_videoclips(clips, method="compose")
                sg.Popup("Videos are concatenated (1-3)")
                cs = cs1+cs3
                del video_obj1,video_obj3

            elif "video_obj2" in locals() and "video_obj3" in locals() and not ("video_obj1" in locals()):
                video_obj2 = video_obj2.set_fps(30)
                video_obj3 = video_obj3.set_fps(30)
                clips = [video_obj2, video_obj3]
                clip = concatenate_videoclips(clips, method="compose")
                sg.Popup("Videos are concatenated (2-3)")
                cs = cs2+cs3
                del video_obj2,video_obj3




        elif event == '-GENBUT-':
            
            sg.Popup("Estimated render time will be: {} seconds. (Do not panic if it seems stuck after clicking OK)".format(mininum*minidur+mininum+minidur))

            if minidur!=0 and int(mininum)!=0:



                start = timeit.default_timer()


                l1 = random.sample(range(0, cs), int(mininum)+1)  #30du

                if values["-RANDTIME-"]:
                    l2 = [x+int(minidur)+random.randint(0,2) for x in l1]
                else:
                    l2 = [x+int(minidur) for x in l1]

                y =[]
                a = dict()

                for i in range(int(mininum)+1):
                    y.append([l1[i], l2[i]])
                y.pop(0)

                for j in range(0,int(mininum)):
                    a[j] = clip.subclip(y[j][0],y[j][1])

                clipk1 = concatenate_videoclips([a[k] for k in range(int(mininum))])

                #ses ekle ve birlestir
                yenises = CompositeAudioClip([audio_obj])
                c1s = int(clipk1.duration)
                clipk1.audio = yenises

                #son kez kirp
                clipk1 = clipk1.subclip(0,c1s)

                #kaydet ya da onizle
               # clipk1.ipython_display(width = 360)
                clipk1.write_videofile("{}/output.mp4".format(savevalue),fps = 30)

                stop = timeit.default_timer()

                print('Time: ', stop - start)  

            else:
                sg.Popup("Not enough input to generate AMV")
            
    except:
        func("---")
