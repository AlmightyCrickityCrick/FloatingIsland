#personaje
define z = Character("[name]", color="#8ca969") #zana
image z default = im.Scale("zana.png", 1400, 1100)
image z happy = im.Scale("zana happy.png", 1400, 1100)
image z think = im.Scale("zana ganditoare.png", 1400, 1100)
image z scared = im.Scale("zana scared.png", 1400, 1100)
define s = Character("Chiță", color="#805D49") #soarec
image s happy = im.Scale("soarec happy.png", 1400, 1100)
image s default = im.Scale("soarec.png", 1400, 1100)
image s diss = im.Scale("soarec dissapointed.png", 1400, 1100)
define f = Character("Rumi", color="#5454") #furnica
define b = Character("Familia Broscăneanu", color="#57882D") #broaste
image b default = im.Scale("broastedefault.png", 1400, 1100)
image b happy = im.Scale("broastehappy.png", 1400, 1100)
image b diss = im.Scale("broastedissapointed.png", 1400, 1100)

default aura = 0
default char_ypos=0.1


#backgrounds
image island = im.Scale("island.png", 1920, 1080)
image field = im.Scale("Field.png", 1920, 1080)
image field_bridge = im.Scale("Field + bridge.png", 1920, 1080)
image island_wind = im.Scale("island_wind.png", 1920, 1080)
image poiana = im.Scale("poiana.png", 1920, 1080)
image poiana_aura = im.Scale("poiana_aura.png", 1920, 1080)
image poiana_pod = im.Scale("poiana_pod.png", 1920, 1080)
image poiana_gol = im.Scale("poianafpod.png", 1920, 1080)
image black_image = im.Scale("black_image.png", 1920, 1080)
#image puzzle_frame = im.Scale("puzzle_frame.png", 1920, 1080)

#pozitionari
transform center:
    ypos 0.1
    xpos 0.15

transform left:
    ypos 0.1
    xpos -0.1

transform right:
    ypos 0.1
    xpos 0.4

default finished_pieces = 0
#python code
init python:
    import random
    def setup_puzzle():
        for i in range(page_pieces):
            start_x = 400 #1200
            start_y = 200 #200
            end_x = 1500 #1700
            end_y = 800 #800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)

    def piece_drop(dropped_on, dragged_piece):
        global finished_pieces
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False    
            finished_pieces+=1
            if finished_pieces==page_pieces:
                renpy.jump("reassemble_complete")
        return

default page_pieces = 12
default full_page_size = (1050,500) 
default piece_coordinates = [(885,357), (1090,349), (1288,329), (1490,359), 
                            (885,451), (1029,481), (1268,464), (1437,524), 
                            (887,611), (1064,625), (1279,633), (1474,652)]
default initial_piece_coordinates = []
#aura bar
screen stats_screen():
    frame:
        xalign 0.05
        yalign 0.01
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
    scene poiana
    "Te trezești într-o poiană în care nu ai mai fost vreodată."
    show z scared at center 
    z "Unde sunt?...Cum am ajuns aici?..."
    show z think
    z "Trebuie să caut pe cineva să mă ajute."
    "Te primbli prin poiană ca să explorezi lumea nouă."
    "Încerci să-ți dai seama ce a putut cauza furtuna, dar nu găsești răspunsul."
    "Începi, totuși, să simți că îți revin puterile."
    menu:
        "Unde dorești să mergi mai departe?"
        "La poiana ascunsă din apropiere":
            "Decizi să explorezi puțin locul din împrejurime."
            scene poiana_aura
            show z happy at center
            "Simți o energie pozitivă ce te pătrunde."
            show screen stats_screen()
            $ aura +=100
            # show screen stats_screen
            "+100 AURA"
            jump broaste_minigame

        "Pe poteca ce iese din pădure":
            "Începi să mergi pe drumul ce trece prin pădure."
            jump broaste_minigame
            
#Chapter 2: Exploreaza
label intro_soarec:
    #Vede prima data soarecul se ii povesteste despre cum lucreaza aura bar si ii
    # da alte detalii
label intalnire_furnica:
    #Vede furnica ce i se plange ca nu poate ajunge acasa ca podul e stricat.
    # screen cu minigame

screen reassemble_puzzle:
    #image "poiana_pod"
    frame:
        background "chenar.png"
        xysize full_page_size 
        anchor(0.5,0.5)
        pos(1300,515)

    draggroup:
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5,0.5)
                focus_mask True
                drag_raise True
                image "Pieces/piesa%s.png" % (i+1)
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5,0.5)
                focus_mask True
                image "Pieces/piesa%s.png" % (i+1) alpha 0.5

label pod_minigame:
    scene poiana_gol
    show screen stats_screen()
    $ setup_puzzle()
    call screen reassemble_puzzle

    return

label reassemble_complete:
    "ai completat puzzle"

label broaste_minigame:
    show b default at right
    show z default at left
    menu:
        b"Cine ești?"
        "Mă numesc [name]. Am venit să vă ajut.":
            show b happy
            "Broaștelor le place răspunsul tău."
            $ aura +=50
            "+50 AURA"
        "Nu cred că e important pentru conversația noastră":
            show b diss
            "Broaștele sunt nemulțumite cu răspunsul tău."
            $ aura -=50
            "-50 AURA"
        "[name], o zână.":
            "Broaștele nu par convinse de răspunsul tău."
    show b default
    menu:
        b"Ce plănuiești să faci aici?"
        "Nu știu, sunt pierdută.":
            "Broaștele nu par convinse de răspunsul tău."
        "Vreau să aflu de unde s-au pornit spiritele rele.":
            show b happy
            "Broaștelor le place răspunsul tău."
            $ aura +=50
            "+50 AURA"
        "Vreau să ajung acasă cât mai repede.":
            show b diss
            "Broaștele sunt nemulțumite cu răspunsul tău."
            $ aura -=50
            "-50 AURA"
    show b default
    menu:
        b"Cum știm că nu ești de partea cea rea?"
        "Am fost afectată și eu de spiritele rele și vreau să restabilesc pacea.":
            show b happy
            "Broaștelor le place răspunsul tău."
            $ aura +=50
            "+50 AURA"
        "Nu știu cum să vă demonstrez.":
            "Broaștele nu par convinse de răspunsul tău."
        "Cum îndrăzniți deodată să mă acuzați? doar nu v-am făcut nimic rău.":
            show b diss
            "Broaștele sunt nemulțumite cu răspunsul tău."
            $ aura -=50
            "-50 AURA"
    show b default
    menu:
        b"Demonstrează că ești de partea noastră."
        "Sunt gata să vă ofer din aura mea pentru a vă ajuta satul. (-100 AURA)":
            show b happy
            "Broaștelor le place răspunsul tău."
            $ aura -=100
            "-100 AURA"
            "Totuși, prin bunătatea oferită, sporești spiritele pozitive."
            "Primești din energia lor."
            $ aura *=2
            "AURA ta se dublează."
        "Nu pot, cer doar să aveți încredere în mine.":
            "Broaștele nu par convinse de răspunsul tău."
        "V-am spus deja tot, ar fi inteligent din partea voastră să mă credeți.":
            show b diss
            "Broaștele sunt nemulțumite cu răspunsul tău."
            $ aura -=50
            "-50 AURA"

