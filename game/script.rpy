define z = Character("zana", color="#5454") #zana
define s = Character("soarec", color="#5454") #soarec
define f = Character("furnica", color="#5454") #furnica
define b = Character("broaste", color="#5454") #broaste

# de adaugat undeva pe aici cod ce seteaza aura bar
# jucatorul sa-si poate alege numele



#Chapter 1: Prolog
label start:
    # Freya exista fericita, se da putin background despre ea.
    # Incep niste vanturi mari si ea cade
    return
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
    # primeste + aura daca reuseste in timp si - daca nu
label pod_succes:
    #daca ajuta furnica va fi o interactie pozitiva
    # inainte de a intra in sat soarecul arata ca e multumit
label pod_esec:
    #daca nu ajuta furnica ramane acolo trista, zana zboara peste rau mai departe
    # soarecul arata dezamagirea
label sat_soarec:
    # inainte de a intra in sat soarecul ii da mai multe detalii despre el


