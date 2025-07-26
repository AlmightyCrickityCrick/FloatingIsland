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
define f = Character("Rumi", color="#5454") #furnica
image f happy = im.Scale("broastedefault.png", 1400, 1100)
image f sad = im.Scale("broastedefault.png", 1400, 1100)
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
image poiana_pod = im.Scale("poianapod.png", 1920, 1080)
image poiana_gol = im.Scale("poianafpod.png", 1920, 1080)
image black_image = im.Scale("black_image.png", 1920, 1080)
image marginea_padurii = im.Scale("marginea_padurii.png", 1920, 1080)
image sat_broaste = im.Scale("sat_broaste.png", 1920, 1080)
image night = im.Scale("night.png", 1920, 1080)
image tower = im.Scale("tower.png", 1920, 1080)
image cristal = im.Scale("cristal.png", 1920, 1080)

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
    def aura_ending(aura): #aici for fi toate endings
        if aura >=200:
            pass
        elif aura <0:
            pass
        else:
            pass

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
            show screen stats_screen()
            $ aura +=50
            # show screen stats_screen
            "+100 AURA"
            jump intro_soarec

        "Pe poteca ce iese din pădure":
            "Începi să mergi pe drumul ce trece prin pădure."
            jump intro_soarec
            
#Chapter 2: Exploreaza
label intro_soarec:
    scene marginea_padurii
    "Iti continui drumul prin poiana pana ajungi la marginea padurii, unde observi o silueta la tulpina unui copac"
    show s default at right
    "Bine ai ajuns in lumea fiintelor de jos...Te asteptam demul"
    show z default at left
    z "Cine suneti,un fel de ghid al acestei lumi?"
    s "Sunt cel care iti va explica cum stau lucrurile aici si ce va trebui sa faci pe parcurs"
    z "Atunci va ascult fiindca doresc sa aduc lumea la normal"
    show screen stats_screen()
    s "Va trebui sa te indrepti inainte pentru a strange AURA care iti va aduce puteri pebtru
    a invinge spiritele negre care au aparut in urma dezechilibrarii emotiilor si plus la asta
    s-au inceput furturile care organizeaza spiritele pentru a aduce si mai mult"
    z "Am inteles, va multumesc pentru informatie, atunci voi pleca imediat in calatorie."
    jump intalnire_furnica
label intalnire_furnica:
    scene poiana_gol
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
    hide f default
    hide z default
    $ setup_puzzle()
    call screen reassemble_puzzle
    return

label reassemble_complete:
    scene poiana_pod
    show f happy at right
    show z happy at left
    "Ai reușit să repari podul către sat."
    $ aura+=50
    "+100 AURA"

    "Acum furnica te va îndrepta spre sat unde s-au organizat cele mai mari pagube."
    f "Acolo locuiesc broaște înțelepte care au tot feluri de ritualuri pentru fiecare năpastă,"
    f "dacă observi ceva straniu să nu te uimești și să fii calmă."
    f "Acolo vei ajuta cel mai mult."
    hide f happy
    hide z happy
    "Împreună cu furnica ați plecat în drum către sat ,ținându-vă de vorbă ca să treacă timpul mai repede și să ajungeți cu o dispoziție bună."
    jump sat_broaste


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

# label pod_minigame:
#     scene poiana_gol
#     show screen stats_screen()
#     $ setup_puzzle()
#     call screen reassemble_puzzle

#     return

label sat_broaste:
    scene sat_broaste
    "Peste ceva timp ați ajuns la marginea satului,unde ați văzut în centrul său niște broaște care dansau în jurul unui rug mare care pâlpâia tot mai tare."
    show z default at left
    show f happy at right
    f "Îți mulțumesc pentru ajutor, și ție îți doresc succes în continuare"
    hide f happy
    show z default at center

    "Ai ajuns în centrul satului unde te-au observat broaștele."
    show b default at right
    show z default at left
    "Cu suspiciune, încep să-ți vorbească:"

    b"Dacă nu mă greșesc ești zâna care a venit de pe insula din ceruri, așai?"

    z"Da, mă numesc [name] și am venit să rezolv problema cu spiritele negre,"
    z"ca să readuc echilibrul în lume și să mă întorc pe insula mea."
    b "Spiritele negre au distrus grădinile noastre, ne-au lăsat fără hrană, au distrus și case."
    b"Vom fi încântați dacă vei rezolva această problemă în cel mai curând timp, "
    b"însă avem câteva întrebări pentru tine mai întâi:"
    jump broaste_minigame


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
            $ aura +=100
            "+50 AURA"
        "Nu știu cum să vă demonstrez.":
            "Broaștele nu par convinse de răspunsul tău."
        "Cum îndrăzniți deodată să mă acuzați? doar nu v-am făcut nimic rău.":
            show b diss
            "Broaștele sunt nemulțumite cu răspunsul tău."
            $ aura -=100
            "-100 AURA"
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
            $ aura -=200
            "-200 AURA"
label broaste_aftermath:
    if aura > 100:
        jump broaste_pozitiv
    else:
        jump broaste_mid

 
label broaste_pozitiv:
    "Ai obținut încrederea broscuțelor și AURA în același timp."
    "Energia pozitivă pe care o emani sperie orice spirit negativ"
    "Satul pare salvat."
    show b happy at right
    show z happy at left
    b "Mulțumim pentru ajutor!"
    b "Ești magică! Îți urăm succes în aventura ta."
    jump plecare_sat

label broaste_mid:
    show z default at left
    show b diss at right
    "Broaștele nu au mare încredere în tine."
    "Nu ai reușit să obții destulă AURA și satul lor continuă să fie bântuit."
    jump plecare_sat

label plecare_sat:
    "A venit timpul să pleci din sat în căutarea spiritelor."
    scene night
    show z think at center
    "Continui să mergi prin pădure, cînd te întâlnești din nou cu Chiță."
    show z default at left
    show s default at right
    s "Bună! Să știi că următoarea ta oprire este esențială."
    s "În pădure se află un turn cu un cristal."
    s "El va determina soarta acestei lumi."
    s "Și desigur, soarta ta."
    s "Caută-l."
    hide s default
    "La fel de brusc cum apăruse, atât de brusc dispăruse."
    show z think at center
    "Ai fost pusă pe gânduri de cele spuse de el, însă îți continui drumul."


