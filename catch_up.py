from pygame import *



window = display.set_mode((700,500)) # 500 px yükseklik ve 700 pxlik boyutlara sahip boş pencere
display.set_caption("Kovalamaca") #pencere başlığı
background = transform.scale(image.load("background.png"), (700,500))
#arkaplan görselinin aktarılması ve ekrannın boyutlandırılması 

x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100)) # karakter 1 in ekranına yerleştrilmesi
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))# karakter 2 in ekranına yerleştrilmesi
speed = 10

run = True 
clock = time.Clock()# bir tane clock nesnesi oluşturduk oyun döngümüz saniyede ka. defa tekrarlıyacak
FPS = 60 #döngü tekrar hızı için oluşturuldu

while run:
    window.blit(background,(0,0)) # ekrana arkaplanı yerleştiriyoruz
    window.blit(sprite1, (x1, y1)) # ekrana karakter 1 i yerleştiriyoruz
    window.blit(sprite2,(x2,y2)) # ekrana karakter ikiyi yerleştiriyoruz

    for e in event.get(): #burda event.get listesi içerisndeki tüm öğeler tek tek kontrol edilir
        if e.type == QUIT: # eğer bu listedeki değerlerden bir tanesi quite eşitse yani x e başlamışssa
            run = False #oyunu sonlandırdık

    keys_pressed = key.get_pressed() #key pressed değişkenine tuşlara basılma olaylarını atadık

    #karakter 1 
    if keys_pressed [K_LEFT] and x1 > 5: #eğer sol ok tuşuna basılırsa ve x1 konumu 5 ten büyükse
        x1 -= speed #sola git
    if keys_pressed [K_RIGHT] and x1 < 595: #eğer sağ ok tuşuna basılırsa ve x1 konumu 5 ten büyükse
        x1 += speed #sAĞA git
    if keys_pressed [K_UP] and y1 > 5: #eğer yukarı tuşuna basılırsa ve x1 konumu 5 ten büyükse
        y1 -= speed #yukarıgit
    if keys_pressed [K_DOWN] and y1 < 395: #eğer aşşağı tuşuna basılırsa ve x1 konumu 5 ten büyükse
        y1 += speed #aşşağı git

    if keys_pressed [K_a] and x2 > 5: #eğer A ok tuşuna basılırsa ve x1 konumu 5 ten büyükse
        x2 -= speed #sola git
    if keys_pressed [K_d] and x2 < 595: #eğer D tuşuna basılırsa ve x1 konumu 5 ten büyükse
        x2 += speed #sAĞA git
    if keys_pressed [K_w] and y2 > 5: #eğer W tuşuna basılırsa ve x1 konumu 5 ten büyükse
        y2 -= speed #yukarıgit
    if keys_pressed [K_s] and y2 < 395: #eğer S tuşuna basılırsa ve x1 konumu 5 ten büyükse
        y2 += speed #aşşağı git


    display.update()
    clock.tick(FPS)

#oyun penceresi oluştur

#sahne arka planını ayarla

#2 sprite oluştur ve onları sahneye yerleştir

#"Pencereyi kapat" düğmesine tıklayın" olayını ele alın