# Programmed by Dogan Yigit Yenigun (toUpperCase78)
"""
Happy New Year 2024 with Squares, Tree & Gifts!
Implemented with OpenCV - EN Version
"""
import numpy as np
import cv2

FONT = cv2.FONT_HERSHEY_TRIPLEX
AA = cv2.LINE_AA
COLORS = [(0,0,255),(0,128,255),(0,255,255),(0,255,0),(255,255,0),(255,100,0),(255,0,0),(128,0,192)]
COLORS_DARK = [(0,0,128),(0,64,128),(0,128,128),(0,128,0),(128,128,0),(128,50,0),(128,0,0),(64,0,96)]
COLORS_SQ = [(0,0,255),(0,255,0),(0,160,220),(255,0,0)]
COLORS_DARK_SQ = [(0,0,128),(0,128,0),(0,80,110),(128,0,0)]

image = np.zeros((795,795,3))
image = image.astype(np.uint8)

c = 0
for i in range(12):
    cv2.rectangle(image, (15+(i*60),15), (55+(i*60),55), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (20+(i*60),20), (50+(i*60),50), COLORS_SQ[c%4], -1)
    c += 1
for i in range(12):
    cv2.rectangle(image, (735,15+(i*60)), (775,55+(i*60)), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (740,20+(i*60)), (770,50+(i*60)), COLORS_SQ[c%4], -1)
    c += 1
for i in range(12):
    cv2.rectangle(image, (735-(i*60),735), (775-(i*60),775), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (740-(i*60),740), (770-(i*60),770), COLORS_SQ[c%4], -1)
    c += 1
for i in range(12):
    cv2.rectangle(image, (15,735-(i*60)), (55,775-(i*60)), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (20,740-(i*60)), (50,770-(i*60)), COLORS_SQ[c%4], -1)
    c += 1

cv2.putText(image, "HAPPY NEW YEAR!", (95,135), FONT, 2, (0,255,255), 3, AA)
cv2.putText(image, "2", (90,305), FONT, 4.2, (0,255,255), 6, AA)
cv2.putText(image, "0", (90,410), FONT, 4.2, (0,255,255), 6, AA)
cv2.putText(image, "2", (90,515), FONT, 4.2, (0,255,255), 6, AA)
cv2.putText(image, "4", (90,620), FONT, 4.2, (0,255,255), 6, AA)

cv2.putText(image, "2", (620,305), FONT, 4.2, (0,255,255), 6, AA)
cv2.putText(image, "0", (620,410), FONT, 4.2, (0,255,255), 6, AA)
cv2.putText(image, "2", (620,515), FONT, 4.2, (0,255,255), 6, AA)
cv2.putText(image, "4", (620,620), FONT, 4.2, (0,255,255), 6, AA)

root_out = np.array([[300,690],[500,690],[500,678],[460,640],[450,510],[350,510],[340,640],[300,678]], np.int32)
cv2.fillPoly(image, [root_out], (0,41,68), lineType=AA)
root_in = np.array([[305,685],[495,685],[495,683],[455,645],[445,505],[355,505],[345,645],[305,683]], np.int32)
cv2.fillPoly(image, [root_in], (0,62,102), lineType=AA)

grass1 = np.array([[210,630],[400,590],[590,630],[590,624],[400,465],[210,624]], np.int32)
cv2.fillPoly(image, [grass1], (0,80,0), lineType=AA)
grass2 = np.array([[240,550],[400,510],[560,550],[560,544],[400,380],[240,544]], np.int32)
cv2.fillPoly(image, [grass2], (0,90,0), lineType=AA)
grass3 = np.array([[270,480],[400,430],[530,480],[530,474],[400,295],[270,474]], np.int32)
cv2.fillPoly(image, [grass3], (0,100,0), lineType=AA)
grass4 = np.array([[300,410],[400,350],[500,410],[500,404],[400,220],[300,404]], np.int32)
cv2.fillPoly(image, [grass4], (0,110,0), lineType=AA)
grass5 = np.array([[320,340],[400,270],[480,340],[480,334],[400,190],[320,334]], np.int32)
cv2.fillPoly(image, [grass5], (0,120,0), lineType=AA)

star1 = np.array([[348,184],[386,184],[400,150],[414,184],[452,184],[422,206],[440,245],[400,220],[360,245],[378,206]], np.int32)
cv2.fillPoly(image, [star1], (0,150,150), lineType=AA)
star2 = np.array([[360,189],[391,189],[400,160],[409,189],[440,189],[417,206],[434,239],[400,215],[366,239],[383,206]], np.int32)
cv2.fillPoly(image, [star2], (0,200,200), lineType=AA)
star3 = np.array([[372,194],[396,194],[400,170],[404,194],[428,194],[412,206],[428,233],[400,210],[372,233],[388,206]], np.int32)
cv2.fillPoly(image, [star3], (0,255,255), lineType=AA)

cv2.circle(image, (360,295), 12, COLORS_DARK[5], -1, AA)
cv2.circle(image, (360,295), 9, COLORS[5], -1, AA)
cv2.circle(image, (440,295), 12, COLORS_DARK[4], -1, AA)
cv2.circle(image, (440,295), 9, COLORS[4], -1, AA)
cv2.circle(image, (400,260), 12, COLORS_DARK[0], -1, AA)
cv2.circle(image, (400,260), 9, COLORS[0], -1, AA)

cv2.circle(image, (324,380), 12, COLORS_DARK[2], -1, AA)
cv2.circle(image, (324,380), 9, COLORS[2], -1, AA)
cv2.circle(image, (400,344), 12, COLORS_DARK[1], -1, AA)
cv2.circle(image, (400,344), 9, COLORS[1], -1, AA)
cv2.circle(image, (476,380), 12, COLORS_DARK[6], -1, AA)
cv2.circle(image, (476,380), 9, COLORS[6], -1, AA)

cv2.circle(image, (290,465), 12, COLORS_DARK[3], -1, AA)
cv2.circle(image, (290,465), 9, COLORS[3], -1, AA)
cv2.circle(image, (345,440), 12, COLORS_DARK[4], -1, AA)
cv2.circle(image, (345,440), 9, COLORS[4], -1, AA)
cv2.circle(image, (400,420), 12, COLORS_DARK[7], -1, AA)
cv2.circle(image, (400,420), 9, COLORS[7], -1, AA)
cv2.circle(image, (455,440), 12, COLORS_DARK[0], -1, AA)
cv2.circle(image, (455,440), 9, COLORS[0], -1, AA)
cv2.circle(image, (510,465), 12, COLORS_DARK[2], -1, AA)
cv2.circle(image, (510,465), 9, COLORS[2], -1, AA)

cv2.circle(image, (264,540), 12, COLORS_DARK[7], -1, AA)
cv2.circle(image, (264,540), 9, COLORS[7], -1, AA)
cv2.circle(image, (330,520), 12, COLORS_DARK[1], -1, AA)
cv2.circle(image, (330,520), 9, COLORS[1], -1, AA)
cv2.circle(image, (400,500), 12, COLORS_DARK[3], -1, AA)
cv2.circle(image, (400,500), 9, COLORS[3], -1, AA)
cv2.circle(image, (470,520), 12, COLORS_DARK[5], -1, AA)
cv2.circle(image, (470,520), 9, COLORS[5], -1, AA)
cv2.circle(image, (536,540), 12, COLORS_DARK[0], -1, AA)
cv2.circle(image, (536,540), 9, COLORS[0], -1, AA)

cv2.circle(image, (236,620), 12, COLORS_DARK[5], -1, AA)
cv2.circle(image, (236,620), 9, COLORS[5], -1, AA)
cv2.circle(image, (290,605), 12, COLORS_DARK[6], -1, AA)
cv2.circle(image, (290,605), 9, COLORS[6], -1, AA)
cv2.circle(image, (345,592), 12, COLORS_DARK[2], -1, AA)
cv2.circle(image, (345,592), 9, COLORS[2], -1, AA)
cv2.circle(image, (400,580), 12, COLORS_DARK[4], -1, AA)
cv2.circle(image, (400,580), 9, COLORS[4], -1, AA)
cv2.circle(image, (455,592), 12, COLORS_DARK[1], -1, AA)
cv2.circle(image, (455,592), 9, COLORS[1], -1, AA)
cv2.circle(image, (510,605), 12, COLORS_DARK[7], -1, AA)
cv2.circle(image, (510,605), 9, COLORS[7], -1, AA)
cv2.circle(image, (564,620), 12, COLORS_DARK[3], -1, AA)
cv2.circle(image, (564,620), 9, COLORS[3], -1, AA)

cv2.rectangle(image, (180,630), (270,700), (0,50,150), -1, AA)
cv2.line(image, (225,630), (225,700), (255,255,105), 5, AA)
ribbon1a = np.array([[225,628], [208,618], [197,615], [190,619], [198,624]], np.int32)
cv2.fillPoly(image, [ribbon1a], (255,255,105), lineType=AA)
ribbon1b = np.array([[225,628], [242,618], [253,615], [260,619], [252,624]], np.int32)
cv2.fillPoly(image, [ribbon1b], (255,255,105), lineType=AA)

cv2.rectangle(image, (250,650), (320,710), (150,0,0), -1, AA)
cv2.line(image, (285,650), (285,710), (0,255,255), 5, AA)
ribbon2a = np.array([[285,648], [268,638], [257,635], [250,639], [258,644]], np.int32)
cv2.fillPoly(image, [ribbon2a], (0,255,255), lineType=AA)
ribbon2b = np.array([[285,648], [302,638], [313,635], [320,639], [312,644]], np.int32)
cv2.fillPoly(image, [ribbon2b], (0,255,255), lineType=AA)

cv2.rectangle(image, (540,620), (620,700), (0,150,255), -1, AA)
cv2.line(image, (580,620), (580,700), (0,160,0), 5, AA)
ribbon3a = np.array([[580,618], [563,608], [552,605], [545,609], [553,614]], np.int32)
cv2.fillPoly(image, [ribbon3a], (0,160,0), lineType=AA)
ribbon3b = np.array([[580,618], [597,608], [608,605], [615,609], [607,614]], np.int32)
cv2.fillPoly(image, [ribbon3b], (0,160,0), lineType=AA)

cv2.rectangle(image, (450,660), (550,715), (150,255,0), -1, AA)
cv2.line(image, (500,660), (500,715), (0,0,150), 5, AA)
ribbon4a = np.array([[500,658], [483,648], [472,645], [465,649], [473,654]], np.int32)
cv2.fillPoly(image, [ribbon4a], (0,0,150), lineType=AA)
ribbon4b = np.array([[500,658], [517,648], [528,645], [535,649], [528,654]], np.int32)
cv2.fillPoly(image, [ribbon4b], (0,0,150), lineType=AA)

cv2.imshow("HAPPY NEW YEAR 2024", image)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    print("Saving image...")
    cv2.imwrite("newyear_2024_en.png", image)

cv2.destroyAllWindows()
