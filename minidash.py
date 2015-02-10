#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
import sys
import time
import json
import urllib2

pygame.init()
dag=0
wait=58
h_off=23
m_off=10
h_on=7
m_on=15
window = pygame.display.set_mode((320,240))
font0 = pygame.font.SysFont("droidsans", 15)
font1 = pygame.font.SysFont("droidsans", 83)
font2 = pygame.font.SysFont("freemono", 32)
font3 = pygame.font.SysFont("droidsans", 16)
font2.set_italic(1)
font2.set_bold(1)
#label0 = font0.render("Temperatuur: "+str(temperature)+"C        Luchtvochtigheid: "+str(humidity)+"%", 1, (255,0,0))
#label3 = font3.render("Luchtvochtigheid:"+str(humidity)+"%", 1, (255,0,0))
rect1 = pygame.Rect(0, 62, 319, 70)
rect2 = pygame.Rect(0, 150, 319, 35)
os.system("/app/tft_init")
os.system("/app/tft_clear")
os.system("/app/tft_pwm 20")
while True:
        try:      
                lt = time.localtime()
                dag_nu=time.strftime("%d", lt)
                uur_nu=time.strftime("%H", lt)
                min_nu=time.strftime("%M", lt)
                if dag != dag_nu:
                   response = urllib2.urlopen('http://pieters.zapto.org:85/geheim/suntimes/today')
                   my_data = json.load(response)
                   sunrise=my_data['response']['sunrise']
                   sunset=my_data['response']['sunset']
                   dag=dag_nu
                if int(uur_nu) == int(h_off) and int(min_nu) == int(m_off):
                   os.system("/app/tft_pwm 0")
                if int(uur_nu) == int(h_on) and int(min_nu) == int(m_on):
                   os.system("/app/tft_pwm 20")
                label1 = font1.render(time.strftime("  %H:%M ", lt), 1, (255,255,0))
                response = urllib2.urlopen('http://pieters.zapto.org:85/geheim/telist')
                my_data = json.load(response)
                temperature=my_data['response'][0]['te']
                humidity=my_data['response'][0]['hu']
                label0 = font0.render("Temperatuur: "+str(temperature)+"C        Luchtvochtigheid: "+str(humidity)+"%", 1, (255,0,0))
                label3 = font3.render("ZonOp: "+str(sunrise)+"                     ZonOnder: "+str(sunset) , 1, (255,0,0))
                window.fill(pygame.Color(0,0,0))
                pygame.draw.rect(window, pygame.Color(60,0,0), rect1)
                pygame.draw.rect(window, pygame.Color(0,200,200), rect2)
#                pygame.draw.line(window, pygame.Color(0,0,255), (0,210), (319,210))
                pygame.draw.line(window, pygame.Color(0,0,255), (0,239), (319,239))
                label2 = font2.render(time.strftime("%a %d.%m.%Y ", lt), 1, (0,0,0))
                window.blit(label1, (0,50))
                window.blit(label2, (0,150))
                window.blit(label0, (0,0))
                window.blit(label3, (10,210))
                window=pygame.transform.flip(window,1,1)
                pygame.image.save(window, "/app/temp.bmp")
                os.system("tft_bmp /app/temp.bmp")
                time.sleep(wait)

        except:
                 sys.exit()

