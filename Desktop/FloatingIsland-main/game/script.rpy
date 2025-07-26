#personaje
define z = Character("[name]", color="#8ca969") #zana
image z default = im.Scale("zana.png", 1400, 1100)
image z happy = im.Scale("zana happy.png", 1400, 1100)
image z think = im.Scale("zana ganditoare.png", 1400, 1100)
image z scared = im.Scale("zana scared.png", 1400, 1100)
define s = Character("soarec", color="#805D49") #soarec
image s happy = im.Scale("soarec happy.png", 1400, 1100)
image s default = im.Scale("soarec.png", 1400, 1100)
image s diss = im.Scale("soarec dissapointed.png", 1400, 1100)
define f = Character("furnica", color="#5454") #furnica
define b = Character("broaste", color="#57882D") #broaste
default aura = 0
default char_ypos=0.1

#backgrounds
image island = im.Scale("island.png", 1920, 1080)
image field = im.Scale("Field.png", 1920, 1080)
image field_bridge = im.Scale("Field + bridge.png", 1920, 1080)
image island_wind = im.Scale("island_wind.png", 1920, 1080)
image poiana_aura = im.Scale("poiana_aura.png", 1920, 1080)
image black_image = im.Scale("black_image.png", 1920, 1080)
image marginea_padurii = im.Scale("marginea_padurii.png", 1920, 1080)
image poiana_pod = im.Scale("poiana_pod.png", 1920, 1080)
image poiana_cadere = im.Scale("poiana_cadere.png", 1920, 1080)
#locatii
transform center:
    ypos 0.1
    xpos 0.15

# de adaugat undeva pe aici cod ce seteaza aura bar
screen stats_screen():
    frame:
        xalign 0.05
        yalign 0.0
        vbox:
            text "AURA: [aura]"

#Chapter 1: Prolog
label start:
    scene island
    "Pe o insulă îndepărtată, în ceruri, unde lumina este principala 
    sursă de energie în lume, emoția pozitivă se mărea pe zi ce trece."
    show z default at center

    "În acea lume locuiești tu, o zână a armoniei și bunătății."

    python:
        name = renpy.input("Care este numele tău?")
        name = name.strip() or "Freya"
    
    z "Astăzi e o zi superbă..."
    show z think
    z "...dar, mi se pare ca vânturile de astăzi sunt neliniștite."
    show z scared
    z "Cred că se apropie o furtună puternică."
    
    "Vântul devine tot mai aspru pe secundă ce se apropie."
    
    "Începi să se îngrijorezi, fiindcă simți o energie negativă și te întrebi care e problema."
    show z think
    z "Sper că se va regla timpul de afară..."
    scene island_wind
    show z scared at center
    "Timpul devine tot mai rău și face ca insula să-și piardă echilibrul."
    "Începi să cazi în jos, puterea ta fiind prea slabă pentru a rezista."
    z "Ce se întâmplă cu energia?!?!"
    z "De ce puterile mele nu funcționează?..."
    scene black_image
    hide z
    z "Ajutor...cineva să mă ajute!!!!!"
    "În timpul căderii, te simți înconjurată de spirite rele."
    z"Cine sunteți?...Ce doriți?..."
    "Îți pierzi conștiința."

    jump ajunge_pamant

    
    
   
label ajunge_pamant:
    scene 
#Chapter 2: Exploreaza
label poiana_start:
    scene poiana_cadere
    "Te trezesti intr-o poiana in care nu ai mai fost vreodata"
    show z default at center 
    z "Unde sunt?...Cum am ajuns?...Trebuie sa caut pe cineva sa ma ajute"

    "Te primbli prin poiana ca sa explorezi lumea noua si sa observi care sunt schimbarile
    care a provocat acea furtuna ce a prabusit insula, si a fortat pierderea puterilor pozitive din aerul inconjurator"
    z "Oare ce s-a intamplat cu mea de aici...nu simt nici macar o emotie pozitiva"

    #poiana extra unde poate sa mearga
label intro_soarec:
    scene marginea_padurii
    "Iti continui drumul prin poiana pana ajungi la marginea padurii, unde observi o silueta la tulpina unui copac"
    show s default at right
    "Bine ai ajuns in lumea fiintelor de jos...Te asteptam demul"
    show z default at left    
    z "Cine suneti,un fel de ghid al acestei lumi?"  
    s "Sunt cel care iti va explica cum stau lucrurile aici si ce va trebui sa faci pe parcurs"
    z "Atunci va ascult fiindca doresc sa aduc lumea la normal" 
    s "Va trebui sa te indrepti inainte pentru a strange AURA care iti va aduce puteri pebtru 
    a invinge spiritele negre care au aparut in urma dezechilibrarii emotiilor si plus la asta 
    s-au inceput furturile care organizeaza spiritele pentru a aduce si mai mult" 
    z "Am inteles, va multumesc pentru informatie, atunci voi pleca imediat in calatorie "


label intalnire_furnica:
    scene poiana_pod
    "Ai pornit intr-o calatorie in care va trebui sa strangi AURA pentru a indeplini caseta 
    si de invinge spiritele negre"
    "Dupa de ai strabatut padurea,ai ajuns la un pod rupt care trebuia sa fie reparat,langa el observi
    o furnica care nu poate trece si cere ajutor de la tine fiindca te-a observat in vizorul sau"
    show f default at right
    "Buna draga zana!...ma ajuti te rog sa repar acest pod pentru a putea trece in sat,deoarece nu mai poate nimeni cine sa ma ajute"
    show z default at left
    "Dar ce s-a intamplat cu podul, s-a destramat?"
    f "Au trecut pe aici spiritele negre si au distrus singura cale de a ajunge acasa si am nevoie de cineva sa ma ajute"
    z "Desigur!...O sa va ajut cu cea mai mare placere"
    
screen pod_minigame:
    # aici va fi codul pentru minigame
    # primeste + aura daca reuseste in timp si - daca nup
    pass
label pod_succes:
    #daca ajuta furnica va fi o interactie pozitiva
    # inainte de a intra in sat soarecul arata ca e multumit
label pod_esec:
    #daca nu ajuta furnica ramane acolo trista, zana zboara peste rau mai departe
    # soarecul arata dezamagirea
label sat_soarec:
    # inainte de a intra in sat soarecul ii da mai multe detalii despre el


