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
default full_page_size = (1920, 1080) 
default piece_coordinates = [(578,331), (769,331), (960,331), (1151,331), 
                            (578,470), (769,470), (960,470), (1151,470), 
                            (578,609), (769,609), (960,609), (1151,609)]
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
            $ aura +=100
            # show screen stats_screen
            "+100 AURA"
            jump poiana_start

        "Pe poteca ce iese din pădure":
            "Începi să mergi pe drumul ce trece prin pădure."
            jump pod_minigame
            
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
        xysize full_page_size #poate aici de jucat
        anchor(0,0)
        pos(578,331)

    draggroup:
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0,0)
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
                anchor(0,0)
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

