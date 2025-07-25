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
    # Freya este pe pamant si incepe putin sa exploreze zona.
    # Este optiunea de a explora (o poiana) sa primeasca extra aura. ( cu call)
#Chapter 2: Exploreaza
label poiana_start:
    #poiana extra unde poate sa mearga
label intro_soarec:
    #Vede prima data soarecul se ii povesteste despre cum lucreaza aura bar si ii
    # da alte detalii
label intalnire_furnica:
    #Vede furnica ce i se plange ca nu poate ajunge acasa ca podul e stricat.
    # screen cu minigame
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


