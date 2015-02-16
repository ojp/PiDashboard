#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
import sys
import time
import json
import urllib2
import urllib
import datetime

pygame.init()
dag=0
wait=58
h_off=16
m_off=46
h_on=16
m_on=50
ws=1
window = pygame.display.set_mode((320,240))
font0 = pygame.font.SysFont("droidsans", 15)
font1 = pygame.font.SysFont("droidsans", 60)
font2 = pygame.font.SysFont("freemono", 22)
font3 = pygame.font.SysFont("droidsans", 16)
#font2.set_italic(1)
font2.set_bold(1)
rect1 = pygame.Rect(0, 62, 150, 50)
rect2 = pygame.Rect(0, 113, 150, 27)
rect3 = pygame.Rect(0,141,150,27)
os.system("/app/tft_init")
os.system("/app/tft_clear")
os.system("/app/tft_pwm 40")
while True:
        try:
                try:
                 lt = time.localtime()
                 dag_nu=time.strftime("%d", lt)
                 uur_nu=time.strftime("%H", lt)
                 min_nu=time.strftime("%M", lt)
                except Exception,e: print str(e)
                if dag != dag_nu:
                   week=datetime.datetime.now().isocalendar()[1]
                   response = urllib2.urlopen('http://pieters.zapto.org:85/geheim/suntimes/today')
                   my_data = json.load(response)
                   sunrise=my_data['response']['sunrise']
                   sunset=my_data['response']['sunset']
                   dag=dag_nu
                if int(uur_nu) == int(h_off) and int(min_nu) == int(m_off):
                   os.system("/app/tft_pwm 0")
                if int(uur_nu) == int(h_on) and int(min_nu) == int(m_on):
                   os.system("/app/tft_pwm 20")
                label1 = font1.render(time.strftime("%H:%M", lt), 1, (255,255,0))
                response = urllib2.urlopen('http://pieters.zapto.org:85/geheim/telist')
                my_data = json.load(response)
                temperature=my_data['response'][0]['te']
                humidity=my_data['response'][0]['hu']
                label0 = font0.render("Temperatuur: "+str(temperature)+"C", 1, (255,0,0))
                label4 = font0.render("Luchtvochtigheid: "+str(humidity)+"%", 1, (255,0,0))
                label3 = font3.render("ZonOp: "+str(sunrise) , 1, (255,0,0))
                label5 = font3.render("ZonOnder: "+str(sunset) , 1, (255,0,0))
                label6 = font3.render("Week "+str(week),1,(255,0,0))
                window.fill(pygame.Color(0,0,0))
                pygame.draw.rect(window, pygame.Color(60,0,0), rect1)
                pygame.draw.rect(window, pygame.Color(0,200,200), rect2)
                pygame.draw.rect(window, pygame.Color(60,0,0), rect3)
#                pygame.draw.line(window, pygame.Color(0,0,255), (0,210), (319,210))
                pygame.draw.line(window, pygame.Color(0,0,255), (0,239), (319,239))
                label2 = font2.render(time.strftime("%d.%m.%Y", lt), 1, (0,0,0))
                window.blit(label1, (0,50))
                window.blit(label2, (0,115))
                window.blit(label0, (0,0))
                window.blit(label4, (0,25))
                window.blit(label5, (0,185))
                window.blit(label3, (0,210))
                window.blit(label6, (0,145))
#                window=pygame.transform.flip(window,1,1)
                if int(ws)==0:
                  urllib.urlretrieve ("http://www.knmi.nl/waarschuwingen_en_verwachtingen/images/waarschuwing_land.png", "/app/waarschuwing_land.png")
                  image = pygame.image.load("/app/waarschuwing_land.png")
                  ws=1
                else:
                  urllib.urlretrieve ("http://www.knmi.nl/waarschuwingen_en_verwachtingen/images/short_term_vandaag_dag.png", "/app/short_term_vandaag_dag.png")
                  image = pygame.image.load("/app/short_term_vandaag_dag.png")
                  ws=0
                weerinfo=pygame.transform.rotozoom(image,0,0.8)
                window.blit(weerinfo, (150,0))
                pygame.image.save(window, "/app/temp.bmp")
                os.system("/app/tft_bmp /app/temp.bmp")
                time.sleep(wait)

        except:
                 sys.exit()
# except Exception,e: print str(e)
