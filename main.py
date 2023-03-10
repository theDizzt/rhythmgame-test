#0. Modules
import pygame, math, time, os, random, sys

#Initialized Module :D
pygame.init()

#Resolution
w = 1600
h = int(w*(9/16))

#Ingame screen
screen = pygame.display.set_mode((w, h))

#Clock
clock = pygame.time.Clock()

#Bools
main = True
ingame = True

#Key detector
keys = [0, 0, 0, 0]
keyset = [0, 0, 0, 0]

#Frames
maxframe = 60
fps = 0

#Time
gst = time.time()
Time = time.time() - gst

#Rate
rate = "PERFECT"

#Font
Cpath = os.path.dirname(__file__)
Fpath = os.path.join("font")

ingame_font_rate = pygame.font.Font(os.path.join(Fpath, "score.ttf"), int(w/23))
rate_text = ingame_font_rate.render(str(rate), False, (255, 255, 255))

#Note
ty =  0
tst = Time

t1 = []
t2 = []
t3 = []
t4 = []

def sum_note(n):
    ty =  0
    tst = Time + 2

    if n == 1:
        ty =  0
        tst = Time + 2
        t1.append([ty, tst])

    if n == 2:
        ty =  0
        tst = Time + 2
        t2.append([ty, tst])

    if n == 3:
        ty =  0
        tst = Time + 2
        t3.append([ty, tst])

    if n == 4:
        ty =  0
        tst = Time + 2
        t4.append([ty, tst])

speed = 1
notesumt = 0

#temp
a = 0
aa = 0

#Effect Variables
spin = 0

combo = 0
combo_effect = 0
combo_effect2 = 0

combo_time = Time + 1

last_combo = 0
miss_anim = 0

#Score
total_notes = 339
rate_ratio = 0
max_combo = 0
extra_score = 0
pres_notes = 0

score = 0
accuracy = 0

#Rating
rate_data = [0, 0, 0, 0]
rate_stack = [0, 0, 0, 0]

def rating(n):
    global combo, miss_anim, last_combo, combo_effect, combo_effect2, combo_time, rate, rate_ratio, max_combo, extra_score, score, pres_notes, accuracy

    judge_ms = [16/2, 39/2, 69/2, 96/2, 127/2, 164/2]

    if abs((h/12)*9 - rate_data[n - 1] <= judge_ms[5] * speed * (h/900) and abs((h/12) * 9 - rate_data[n - 1] > judge_ms[4] * speed * (h/900))):
        last_combo = combo
        miss_anim = 1
        combo = 0
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate = "FRAGILE"
    
    if abs((h/12)*9 - rate_data[n - 1] <= judge_ms[4] * speed * (h/900) and abs((h/12) * 9 - rate_data[n - 1] > judge_ms[3] * speed * (h/900))):
        last_combo = combo
        miss_anim = 1
        combo = 0
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate_ratio += 0.01
        rate = "SCARCITY"

    if abs((h/12)*9 - rate_data[n - 1] <= judge_ms[3] * speed * (h/900) and abs((h/12) * 9 - rate_data[n - 1] > judge_ms[2] * speed * (h/900))):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate_ratio += 0.3
        rate_stack[3] += 1
        rate = "COMMON"
        if max_combo < combo:
            max_combo += 1
    
    if abs((h/12)*9 - rate_data[n - 1] <= judge_ms[2] * speed * (h/900) and abs((h/12) * 9 - rate_data[n - 1] > judge_ms[1] * speed * (h/900))):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate_ratio += 0.7
        rate_stack[2] += 1
        rate = "PRESERVED"
        if max_combo < combo:
            max_combo += 1

    if abs((h/12)*9 - rate_data[n - 1] <= judge_ms[1] * speed * (h/900) and abs((h/12) * 9 - rate_data[n - 1] > judge_ms[0] * speed * (h/900))):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate_ratio += 1
        rate_stack[1] += 1
        rate = "INTEGRITY"
        if max_combo < combo:
            max_combo += 1
    
    if abs((h/12)*9 - rate_data[n - 1] <= judge_ms[0] * speed * (h/900)):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate_ratio += 1
        extra_score += 1
        rate_stack[0] += 1
        rate = "INTEGRITY+"
        if max_combo < combo:
            max_combo += 1

    pres_notes += 1
    score = int(900000 * (rate_ratio/total_notes) + 100000 * (max_combo/total_notes)) + extra_score
    accuracy = rate_ratio/pres_notes*100

#Run
while main:
    while ingame:

        if len(t1) > 0:
            rate_data[0] = t1[0][0]

        if len(t2) > 0:
            rate_data[1] = t2[0][0]

        if len(t3) > 0:
            rate_data[2] = t3[0][0]

        if len(t4) > 0:
            rate_data[3] = t4[0][0]

        if Time > 0.2 * notesumt:
            notesumt += 1

            #temp
            if not(aa >= total_notes):
                a = random.randint(1, 4)
                sum_note(a)
                aa += 1

        Time = time.time() - gst

        fps = clock.get_fps()

        #Ingame Text
        ingame_font_combo = pygame.font.Font(os.path.join(Fpath, "combo.otf"), int((w/24)*combo_effect2))
        combo_text = ingame_font_combo.render(str(combo), False, (255, 255, 255))

        rate_text = ingame_font_rate.render(str(rate), False, (255, 255, 255))
        rate_text = pygame.transform.scale(rate_text, (int(w/110*len(rate)*combo_effect2), int((w/42*combo_effect*combo_effect2))))

        ingame_font_miss = pygame.font.Font(os.path.join(Fpath, "combo.otf"), int((w/24)*miss_anim))
        miss_text = ingame_font_miss.render(str(last_combo), False, (255, 0, 0))

        ingame_font_combo_title = pygame.font.Font(os.path.join(Fpath, "judge.ttf"), int((w/96)*combo_effect2))
        combo_title = ingame_font_combo_title.render("COMBO", False, (255, 255, 255))

        ingame_font_score = pygame.font.Font(os.path.join(Fpath, "score.ttf"), int((w/48)*combo_effect2))
        score_text = ingame_font_score.render(str(score).zfill(7), False, (255, 255, 255))

        ingame_font_acc = pygame.font.Font(os.path.join(Fpath, "score.ttf"), int((w/48)))
        acc_text = ingame_font_acc.render("{:.2f}%".format(accuracy), False, (255, 255, 255))

        #ingame_font_counter = pygame.font.Font(os.path.join(Fpath, "test.otf"), int(w/96))
        #counter_text = ingame_font_counter.render("MAX COMBO: {}, Perfect+: {}, Perfect: {}, Great: {}, Good: {}".format(max_combo, rate_stack[0], rate_stack[1], rate_stack[2], rate_stack[3]), False, (255, 255, 255))

        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            pygame.display.update()
            
            #Keyboard Input
            if event.type == pygame.KEYDOWN:
                #Line 1
                if event.key == pygame.K_d:
                    keyset[0] = 1
                    if len(t1) > 0:
                        if t1[0][0] > h/3:
                            del t1[0]
                    rating(1)
                
                #Line 2
                if event.key == pygame.K_f:
                    keyset[1] = 1
                    if len(t2) > 0:
                        if t2[0][0] > h/3:
                            del t2[0]
                    rating(2)
                
                #Line 3
                if event.key == pygame.K_j:
                    keyset[2] = 1
                    if len(t3) > 0:
                        if t3[0][0] > h/3:
                            del t3[0]
                    rating(3)
                
                #Line 4
                if event.key == pygame.K_k:
                    keyset[3] = 1
                    if len(t4) > 0:
                        if t4[0][0] > h/3:
                            del t4[0]
                    rating(4)
            
            if event.type == pygame.KEYUP:
                #Line 1
                if event.key == pygame.K_d:
                    keyset[0] = 0
                
                #Line 2
                if event.key == pygame.K_f:
                    keyset[1] = 0
                
                #Line 3
                if event.key == pygame.K_j:
                    keyset[2] = 0
                
                #Line 4
                if event.key == pygame.K_k:
                    keyset[3] = 0
        
        screen.fill((0, 0, 0))

        #Moving Accelerator
        keys[0] += (keyset[0] - keys[0])/(3*(maxframe/fps))
        keys[1] += (keyset[1] - keys[1])/(3*(maxframe/fps))
        keys[2] += (keyset[2] - keys[2])/(3*(maxframe/fps))
        keys[3] += (keyset[3] - keys[3])/(3*(maxframe/fps))

        #Text Effect
        if Time > combo_time:
            combo_effect += (0 - combo_effect) / (7*(maxframe / fps))

        if Time < combo_time:
            combo_effect += (1 - combo_effect) / (7*(maxframe / fps))
        
        combo_effect2 += (2 - combo_effect2) / (7*(maxframe / fps))

        miss_anim += (4 - miss_anim)/(14*(maxframe/fps))

        #Gear BG
        #pygame.draw.rect(screen, (0, 0, 0), (w/2 - w/8, -int(w/100), w/4, h + int(w/50)))

        #Gear Decoration
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/8 + w/32 - (w/32)*keys[0], (h/12)*9 - (h/30)*keys[0]*i, w/16*keys[0], (h/35)/i))
        
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 - w/16 + w/32 - (w/32)*keys[1], (h/12)*9 - (h/30)*keys[1]*i, w/16*keys[1], (h/35)/i))
        
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/32 - (w/32)*keys[2], (h/12)*9 - (h/30)*keys[2]*i, w/16*keys[2], (h/35)/i))
        
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200/7)*i), 200 - ((200/7)*i), 200 - ((200/7)*i)), (w/2 + w/16 + w/32 - (w/32)*keys[3], (h/12)*9 - (h/30)*keys[3]*i, w/16*keys[3], (h/35)/i))

        #Gear Line
        #pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/8, -int(w/100), w/4, h + int(w / 100)))

        #Generate Note
        for tile_data in t1:
            #????????? ?????? "(?????? ?????? - ?????? ????????????) * 350" ??? ????????? ??????. ?????? ?????? ??? ?????? ?????? ??????????????? 2??? ????????? ????????? ??????.
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*1000*speed*(h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/8, tile_data[0] - h/100, w/16, h/50))
            #?????? ?????? ??????
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                pres_notes += 1
                accuracy = rate_ratio/pres_notes*100
                rate = "MISS"
                t1.remove(tile_data)
        
        for tile_data in t2:
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*1000*speed*(h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                pres_notes += 1
                accuracy = rate_ratio/pres_notes*100
                rate = "MISS"
                t2.remove(tile_data)

        for tile_data in t3:
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*1000*speed*(h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w/2, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                pres_notes += 1
                accuracy = rate_ratio/pres_notes*100
                rate = "MISS"
                t3.remove(tile_data)

        for tile_data in t4:
            tile_data[0] = (h/12)*9 + (Time - tile_data[1])*1000*speed*(h/900)
            pygame.draw.rect(screen, (255, 255, 255), (w/2 + w/16, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                last_combo = combo
                miss_anim = 1
                combo = 0
                combo_effect = 0.2
                combo_time = Time + 1
                combo_effect2 = 1.3
                pres_notes += 1
                accuracy = rate_ratio/pres_notes*100
                rate = "MISS"
                t4.remove(tile_data)

        #Judgement Line
        pygame.draw.rect(screen, (0, 0, 0), (w/2 - w/8, (h/12)*9, w/4, h/2))
        pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/8, (h/12)*9, w/4, h/2), int(h/100))

        #Key
        pygame.draw.rect(screen, (0, 0, 0), (w/2 - w/8, (h/12)*9, w/4, h/2))
        pygame.draw.rect(screen, (255, 255, 255), (w/2 - w/8, (h/12)*9, w/4, h/2), int(h/100))

        pygame.draw.rect(screen, (255 - 100 * keys[0],255 - 100 * keys[0], 255 - 100 * keys[0]), (w / 2 - w / 9, (h / 24) * 19 + (h / 48) * keys[0], w / 27, h / 8), int(h / 150))
        pygame.draw.rect(screen, (255 - 100 * keys[3],255 - 100 * keys[3], 255 - 100 * keys[3]), (w / 2 + w / 13.5, (h / 24) * 19 + (h / 48) * keys[3], w / 27, h / 8), int(h / 150))

        pygame.draw.circle(screen, (150, 150, 150), (w / 2, (h / 24) * 21), (w / 20), int(h / 200))
        pygame.draw.line(screen, (150, 150, 150), (w / 2 - math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 - math.cos(spin) * 25 * (w / 1600)), (w / 2 + math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 + math.cos(spin) * 25 * (w / 1600)), int(w / 400))
        spin += (speed / 20 * (maxframe / fps))

        pygame.draw.rect(screen, (255 - 100 * keys[1], 255 - 100 * keys[1], 255 - 100 * keys[1]), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8))
        pygame.draw.rect(screen, (0,0, 0), (w / 2 - w / 18, (h / 48) * 43 + (h / 48) * (keys[1] * 1.2), w / 27, h / 64), int(h / 150))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8), int(h / 150))

        pygame.draw.rect(screen, (255 - 100 * keys[2], 255 - 100 * keys[2], 255 - 100 * keys[2]), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8))
        pygame.draw.rect(screen, (0,0, 0), (w / 2 + w / 58, (h / 48) * 43 + (h / 48) * (keys[2] * 1.2), w / 27, h / 64), int(h / 150))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8), int(h / 150))

        #Judgement Text Render
        miss_text.set_alpha(255 - (255/4)*miss_anim)
        
        screen.blit(combo_title, (w/2 - combo_title.get_width()/2, (h/30)*4 - combo_title.get_height()/2))
        screen.blit(combo_text, (w/2 - combo_text.get_width()/2, (h/18)*4 - combo_text.get_height()/2))
        screen.blit(rate_text, (w/2 - rate_text.get_width()/2, (h/12)*8 - rate_text.get_height()/2))
        screen.blit(miss_text, (w/2 - miss_text.get_width()/2, (h/18)*4 - miss_text.get_height()/2))
        screen.blit(score_text, (4*w/5 - score_text.get_width()/2, (h/25)*4 - score_text.get_height()/2))
        screen.blit(acc_text, (w/2 - acc_text.get_width()/2, (h/8)*4 - acc_text.get_height()/2))
        #screen.blit(counter_text, (w/5 - counter_text.get_width()/2, (h/30)*4 - counter_text.get_height()/2))

        #Update Display
        pygame.display.flip()

        #Limitate Frames
        clock.tick(maxframe)
