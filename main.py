import random
import time
import unicodedata
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, Line, RoundedRectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, ListProperty

# =====================================================
# 1. DONNÉES DU JEU (Identiques à ta version Pygame)
# =====================================================
FR = [
    ("ECOLE", "École", "lieu où l'on apprend", ""), ("LIVRE", "École", "on le lit page après page", ""),
    ("CAHIER", "École", "on y écrit ses leçons", ""), ("STYLO", "École", "il sert à écrire à l'encre", ""),
    ("CRAIE", "École", "bâton blanc pour écrire au tableau", ""), ("TABLEAU", "École", "mur noir où le maître écrit", ""),
    ("ELEVE", "École", "il apprend à l'école", ""), ("MAITRE", "École", "il enseigne aux élèves", ""),
    ("LECON", "École", "ce que le maître enseigne", ""), ("EXAMEN", "École", "épreuve de fin d'année", ""),
    ("LYCEE", "École", "école après le collège", ""), ("CARTABLE", "École", "sac de l'écolier", ""),
    ("DICTEE", "École", "exercice où l'on écrit ce qu'on entend", ""), ("RECREATION", "École", "pause dans la cour", ""),
    ("UNIVERSITE", "École", "études supérieures", ""), ("BIBLIOTHEQUE", "École", "lieu où l'on emprunte des livres", ""),
    ("YAOUNDE", "Villes et lieux", "capitale du Cameroun", ""), ("DOUALA", "Villes et lieux", "capitale économique", ""),
    ("GAROUA", "Villes et lieux", "chef-lieu du Nord", ""), ("MAROUA", "Villes et lieux", "chef-lieu de l'Extrême-Nord", ""),
    ("BAFOUSSAM", "Villes et lieux", "chef-lieu de l'Ouest", ""), ("BAMENDA", "Villes et lieux", "chef-lieu du Nord-Ouest", ""),
    ("BERTOUA", "Villes et lieux", "chef-lieu de l'Est", ""), ("EBOLOWA", "Villes et lieux", "chef-lieu du Sud", ""),
    ("NGAOUNDERE", "Villes et lieux", "chef-lieu de l'Adamaoua", ""), ("KRIBI", "Villes et lieux", "ville balnéaire du Sud", ""),
    ("LIMBE", "Villes et lieux", "ville au pied du Mont Cameroun", ""), ("CAMEROUN", "Villes et lieux", "pays d'Afrique centrale", ""),
    ("AFRIQUE", "Villes et lieux", "continent du Cameroun", ""), ("MARCHE", "Villes et lieux", "lieu où l'on achète et vend", ""),
    ("VILLAGE", "Villes et lieux", "petit groupe de maisons", ""), ("STADE", "Villes et lieux", "lieu des matchs", ""),
    ("HOPITAL", "Villes et lieux", "lieu où l'on soigne les malades", ""), ("EGLISE", "Villes et lieux", "lieu de prière chrétien", ""),
    ("MOSQUEE", "Villes et lieux", "lieu de prière musulman", ""), ("AEROPORT", "Villes et lieux", "lieu où atterrissent les avions", ""),
    ("FORET", "Nature", "grand espace plein d'arbres", ""), ("SAVANE", "Nature", "grande plaine d'herbes hautes", ""),
    ("MONTAGNE", "Nature", "très haute colline", ""), ("FLEUVE", "Nature", "grand cours d'eau vers la mer", ""),
    ("RIVIERE", "Nature", "cours d'eau plus petit", ""), ("SOLEIL", "Nature", "étoile qui nous éclaire le jour", ""),
    ("LUNE", "Nature", "elle brille dans la nuit", ""), ("ETOILE", "Nature", "point lumineux dans le ciel", ""),
    ("PLUIE", "Nature", "eau qui tombe des nuages", ""), ("VENT", "Nature", "air qui souffle", ""),
    ("ARBRE", "Nature", "il a un tronc et des feuilles", ""), ("FLEUR", "Nature", "elle sent bon et a des pétales", ""),
    ("PLAGE", "Nature", "bord de mer couvert de sable", ""), ("OCEAN", "Nature", "immense étendue d'eau salée", ""),
    ("VOLCAN", "Nature", "montagne qui peut cracher du feu", ""), ("CASCADE", "Nature", "chute d'eau", ""),
    ("LION", "Animaux", "le roi des animaux", ""), ("ELEPHANT", "Animaux", "très gros animal à trompe", ""),
    ("GIRAFE", "Animaux", "animal au très long cou", ""), ("SINGE", "Animaux", "il aime les bananes", ""),
    ("GORILLE", "Animaux", "grand singe de la forêt", ""), ("CROCODILE", "Animaux", "reptile aux grandes dents", ""),
    ("HIPPOPOTAME", "Animaux", "gros animal qui vit dans l'eau", ""), ("PANTHERE", "Animaux", "grand félin noir ou tacheté", ""),
    ("ANTILOPE", "Animaux", "animal rapide aux cornes fines", ""), ("SERPENT", "Animaux", "reptile sans pattes", ""),
    ("POISSON", "Animaux", "il vit dans l'eau", ""), ("POULET", "Animaux", "petit de la poule", ""),
    ("CHEVRE", "Animaux", "elle donne du lait et bêle", ""), ("MOUTON", "Animaux", "animal à la laine", ""),
    ("VACHE", "Animaux", "elle donne du lait", ""), ("OISEAU", "Animaux", "il a des ailes et des plumes", ""),
    ("MANIOC", "Cuisine", "tubercule très consommé", ""), ("PLANTAIN", "Cuisine", "banane à cuire", ""),
    ("BANANE", "Cuisine", "fruit jaune", ""), ("MANGUE", "Cuisine", "fruit sucré à gros noyau", ""),
    ("ANANAS", "Cuisine", "fruit piquant à couronne", ""), ("PAPAYE", "Cuisine", "fruit orange du papayer", ""),
    ("ARACHIDE", "Cuisine", "cacahuète", ""), ("HARICOT", "Cuisine", "graine qu'on fait cuire", ""),
    ("TOMATE", "Cuisine", "légume rouge", ""), ("OIGNON", "Cuisine", "légume qui fait pleurer", ""),
    ("PIMENT", "Cuisine", "il rend la sauce piquante", ""), ("CACAO", "Cuisine", "il sert à faire le chocolat", ""),
    ("CAFE", "Cuisine", "boisson noire et chaude", ""), ("MAIS", "Cuisine", "céréale aux grains jaunes", ""),
    ("NDOLE", "Cuisine", "plat de feuilles amères et d'arachides", ""), ("KOKI", "Cuisine", "gâteau de haricots à la vapeur", ""),
    ("BOBOLO", "Cuisine", "bâton de manioc", ""), ("MACABO", "Cuisine", "tubercule proche du taro", ""),
    ("IGNAME", "Cuisine", "gros tubercule", ""), ("BALAFON", "Culture", "instrument de musique en bois", ""),
    ("TAMBOUR", "Culture", "instrument qu'on frappe", ""), ("DANSE", "Culture", "on bouge au rythme de la musique", ""),
    ("MUSIQUE", "Culture", "art des sons", ""), ("FETE", "Culture", "jour de joie et de réjouissances", ""),
    ("MASQUE", "Culture", "objet des cérémonies traditionnelles", ""), ("BOUBOU", "Culture", "tenue ample du Nord", ""),
    ("KABA", "Culture", "robe longue camerounaise", ""), ("TOGHU", "Culture", "tenue traditionnelle du Grassfield", ""),
    ("MAKOSSA", "Culture", "musique et danse du littoral", ""), ("BIKUTSI", "Culture", "rythme et danse beti", ""),
    ("FOOTBALL", "Culture", "sport des Lions Indomptables", ""), ("INDEPENDANCE", "Culture", "liberté d'un pays", ""),
    ("DRAPEAU", "Culture", "vert, rouge, jaune avec une étoile", ""), ("HYMNE", "Culture", "chant officiel du pays", ""),
    ("UNITE", "Culture", "union de tous", ""), ("PAIX", "Culture", "absence de guerre", ""),
    ("AMITIE", "Culture", "lien entre bons amis", ""), ("FAMILLE", "Famille", "papa, maman et les enfants", ""),
    ("MERE", "Famille", "maman", ""), ("PERE", "Famille", "papa", ""),
    ("FRERE", "Famille", "garçon de mes parents", ""), ("SOEUR", "Famille", "fille de mes parents", ""),
    ("ENFANT", "Famille", "petit garçon ou petite fille", ""), ("TANTE", "Famille", "sœur du père ou de la mère", ""),
    ("ONCLE", "Famille", "frère du père ou de la mère", ""), ("COUSIN", "Famille", "fils de l'oncle ou de la tante", ""),
    ("VOISIN", "Famille", "il habite à côté de chez moi", ""),
]

EN = [
    ("SCHOOL", "École", "école", "skoul"), ("BOOK", "École", "livre", "bouk"),
    ("PENCIL", "École", "crayon", "pèn-sil"), ("TEACHER", "École", "enseignant", "ti-tcheur"),
    ("STUDENT", "École", "élève", "stiou-dent"), ("LESSON", "École", "leçon", "lè-sonn"),
    ("HOMEWORK", "École", "devoirs", "hom-oeurk"), ("LIBRARY", "École", "bibliothèque", "laï-bre-ri"),
    ("UNIVERSITY", "École", "université", "iou-ni-veur-si-ti"), ("KNOWLEDGE", "École", "connaissance", "no-lidj"),
    ("LANGUAGE", "École", "langue", "lan-gouidj"), ("ENGLISH", "École", "anglais", "in-glich"),
    ("FRENCH", "École", "français", "frènch"), ("HOUSE", "Vie quotidienne", "maison", "haouss"),
    ("HOME", "Vie quotidienne", "chez soi", "home"), ("TABLE", "Vie quotidienne", "table", "té-beul"),
    ("CHAIR", "Vie quotidienne", "chaise", "tchèr"), ("WINDOW", "Vie quotidienne", "fenêtre", "ouine-do"),
    ("DOOR", "Vie quotidienne", "porte", "dor"), ("MORNING", "Vie quotidienne", "matin", "mor-nine"),
    ("EVENING", "Vie quotidienne", "soir", "ive-nine"), ("NIGHT", "Vie quotidienne", "nuit", "naït"),
    ("WEEKEND", "Vie quotidienne", "fin de semaine", "ouik-ènd"), ("HAPPY", "Vie quotidienne", "heureux", "ha-pi"),
    ("WELCOME", "Vie quotidienne", "bienvenue", "ouèl-keum"), ("BEAUTIFUL", "Vie quotidienne", "beau, belle", "biou-ti-foul"),
    ("TOGETHER", "Vie quotidienne", "ensemble", "tou-gué-zeur"), ("ADVENTURE", "Vie quotidienne", "aventure", "ad-vèn-tcheur"),
    ("FAMILY", "Famille", "famille", "fa-mi-li"), ("MOTHER", "Famille", "mère", "mo-zeur"),
    ("FATHER", "Famille", "père", "fa-zeur"), ("BROTHER", "Famille", "frère", "bro-zeur"),
    ("SISTER", "Famille", "sœur", "sis-teur"), ("CHILD", "Famille", "enfant", "tchaïld"),
    ("FRIEND", "Famille", "ami", "frènd"), ("NEIGHBOUR", "Famille", "voisin", "néi-beur"),
    ("FRIENDSHIP", "Famille", "amitié", "frènd-chip"), ("CHILDHOOD", "Famille", "enfance", "tchaïld-houd"),
    ("SUN", "Nature", "soleil", "sonn"), ("MOON", "Nature", "lune", "moune"),
    ("STAR", "Nature", "étoile", "star"), ("RAIN", "Nature", "pluie", "réne"),
    ("WIND", "Nature", "vent", "ouinde"), ("RIVER", "Nature", "rivière", "ri-veur"),
    ("FOREST", "Nature", "forêt", "fo-rest"), ("MOUNTAIN", "Nature", "montagne", "maoun-tène"),
    ("BEACH", "Nature", "plage", "bitche"), ("OCEAN", "Nature", "océan", "o-chenn"),
    ("TREE", "Nature", "arbre", "tri"), ("FLOWER", "Nature", "fleur", "flaoueur"),
    ("GARDEN", "Nature", "jardin", "gar-dènn"), ("FIELD", "Nature", "champ", "fild"),
    ("LION", "Animaux", "lion", "laï-eunn"), ("ELEPHANT", "Animaux", "éléphant", "è-li-fanntt"),
    ("MONKEY", "Animaux", "singe", "monn-ki"), ("BIRD", "Animaux", "oiseau", "beurd"),
    ("FISH", "Animaux", "poisson", "fiche"), ("CHICKEN", "Animaux", "poulet", "tchi-kine"),
    ("GOAT", "Animaux", "chèvre", "gaute"), ("HORSE", "Animaux", "cheval", "hors"),
    ("SNAKE", "Animaux", "serpent", "snéke"), ("BREAD", "Cuisine", "pain", "brèd"),
    ("RICE", "Cuisine", "riz", "raïce"), ("BEANS", "Cuisine", "haricots", "binz"),
    ("PEPPER", "Cuisine", "piment, poivre", "pè-peur"), ("COFFEE", "Cuisine", "café", "ko-fi"),
    ("BANANA", "Cuisine", "banane", "beu-na-neu"), ("MANGO", "Cuisine", "mangue", "manng-go"),
    ("PINEAPPLE", "Cuisine", "ananas", "païne-a-peul"), ("PEANUT", "Cuisine", "arachide", "pi-neutt"),
    ("CASSAVA", "Cuisine", "manioc", "ka-sa-va"), ("TOMATO", "Cuisine", "tomate", "to-mé-to"),
    ("ONION", "Cuisine", "oignon", "o-nieunn"), ("WATER", "Cuisine", "eau", "ouo-teur"),
    ("MILK", "Cuisine", "lait", "milk"), ("MARKET", "Villes et lieux", "marché", "mar-kit"),
    ("VILLAGE", "Villes et lieux", "village", "vi-lidj"), ("CITY", "Villes et lieux", "ville", "si-ti"),
    ("COUNTRY", "Villes et lieux", "pays", "konn-tri"), ("STREET", "Villes et lieux", "rue", "strit"),
    ("HOSPITAL", "Villes et lieux", "hôpital", "hos-pi-teul"), ("CHURCH", "Villes et lieux", "église", "tcheurtch"),
    ("STADIUM", "Villes et lieux", "stade", "sté-di-eum"), ("AIRPORT", "Villes et lieux", "aéroport", "èr-port"),
    ("CAPITAL", "Villes et lieux", "capitale", "ka-pi-teul"), ("CAMEROON", "Villes et lieux", "Cameroun", "ka-meu-roune"),
    ("AFRICA", "Villes et lieux", "Afrique", "a-fri-ka"), ("MUSIC", "Culture", "musique", "miou-zik"),
    ("DANCE", "Culture", "danse", "dance"), ("FOOTBALL", "Culture", "football", "fout-bol"),
    ("FESTIVAL", "Culture", "festival", "fès-ti-veul"), ("TRADITION", "Culture", "tradition", "tra-di-chonn"),
    ("HERITAGE", "Culture", "héritage", "hè-ri-tidj"), ("CELEBRATION", "Culture", "célébration", "sè-lé-bré-chonn"),
    ("INDEPENDENCE", "Culture", "indépendance", "in-di-pèn-dennce"), ("AGRICULTURE", "Culture", "agriculture", "a-gri-keul-tcheur"),
    ("PEACE", "Culture", "paix", "pisse"),
]

FF = [
    ("JAM", "Salutations", "paix", "djam"), ("JARAMA", "Salutations", "merci", "dja-ra-ma"),
    ("JAMTAN", "Salutations", "paix seulement (réponse au salut)", "djam-tan"), ("BAABA", "Famille", "père", "baa-ba"),
    ("INNA", "Famille", "mère", "inn-na"), ("DEBBO", "Famille", "femme", "dèb-bo"),
    ("GORKO", "Famille", "homme", "gor-ko"), ("SUKAABE", "Famille", "enfants", "sou-kaa-bé"),
    ("MAWDO", "Famille", "personne âgée, ancien", "maw-do"), ("NAGGE", "Animaux", "vache", "nag-gué"),
    ("NGAARI", "Animaux", "taureau", "n-gaa-ri"), ("MBEEWA", "Animaux", "chèvre", "m-béé-wa"),
    ("MBAALU", "Animaux", "mouton", "m-baa-lou"), ("PUCCU", "Animaux", "cheval", "pout-tchou"),
    ("MBABBA", "Animaux", "âne", "m-bab-ba"), ("GERTOGAL", "Animaux", "poule", "guèr-to-gal"),
    ("NDIYAM", "Nature", "eau", "n-di-yam"), ("NAANGE", "Nature", "soleil", "naan-gué"),
    ("LEWRU", "Nature", "lune", "lèw-rou"), ("LADDE", "Nature", "brousse", "lad-dé"),
    ("LEKKI", "Nature", "arbre", "lèk-ki"), ("LEYDI", "Nature", "pays, terre", "lèy-di"),
    ("HENNDU", "Nature", "vent", "hèn-dou"), ("NGESA", "Nature", "champ", "n-gué-sa"),
    ("SAARE", "Vie quotidienne", "maison", "saa-ré"), ("SUUDU", "Vie quotidienne", "case, chambre", "souu-dou"),
    ("WURO", "Vie quotidienne", "village", "wou-ro"), ("LAAWOL", "Vie quotidienne", "chemin", "laa-wol"),
    ("CEEDE", "Vie quotidienne", "argent", "tchéé-dé"), ("KOSAM", "Vie quotidienne", "lait", "ko-sam"),
    ("NYAAMDU", "Vie quotidienne", "nourriture", "nyaam-dou"), ("HOORE", "Vie quotidienne", "tête", "hoo-ré"),
    ("BERNDE", "Vie quotidienne", "cœur", "bèrn-dé"), ("NAFOORE", "Vie quotidienne", "richesse, utilité", "na-foo-ré"),
    ("TATI", "Nombres", "trois", "ta-ti"), ("NAY", "Nombres", "quatre", "naï"),
    ("JOWI", "Nombres", "cinq", "djo-wi"), ("JEEGOM", "Nombres", "six", "djéé-gom"),
    ("JEEDIDI", "Nombres", "sept", "djéé-di-di"), ("JEETATI", "Nombres", "huit", "djéé-ta-ti"),
    ("JEENAY", "Nombres", "neuf", "djéé-naï"), ("SAPPO", "Nombres", "dix", "sap-po"),
    ("FULFULDE", "Peuple et traditions", "langue des Peuls", "foul-foul-dé"), ("PULAAKU", "Peuple et traditions", "code d'honneur peul", "pou-laa-kou"),
    ("FULBE", "Peuple et traditions", "les Peuls", "foul-bé"), ("PULLO", "Peuple et traditions", "un Peul", "poul-lo"),
    ("LAMIDO", "Peuple et traditions", "chef traditionnel peul", "la-mi-do"), ("GAYNAAKO", "Peuple et traditions", "berger", "gaï-naa-ko"),
]

MOTS = {"fr": FR, "en": EN, "ff": FF}

COULEURS = {
    "École": (1, 0.66, 0.23), "Villes et lieux": (0.58, 0.62, 1), "Nature": (0.47, 0.86, 0.47),
    "Animaux": (0.94, 0.86, 0.31), "Cuisine": (0.82, 0.54, 0.35), "Culture": (0.9, 0.43, 0.78),
    "Famille": (0.31, 0.74, 1), "Vie quotidienne": (0.43, 0.9, 0.82), "Salutations": (1, 0.5, 0.5),
    "Nombres": (0.74, 0.58, 1), "Peuple et traditions": (0.66, 0.66, 0.66),
}

def couleur_cat(cat):
    return COULEURS.get(cat, (0.66, 0.66, 0.66))

DROITE, BAS, DIAG, HAUT_DROITE = (0, 1), (1, 0), (1, 1), (-1, 1)
TOUTES = [DROITE, BAS, DIAG, HAUT_DROITE]

NIVEAUX = {
    1: dict(n=5, nbmin=3, nbmax=5, kmax=9, tmot=30, dirs=[DROITE, BAS]),
    2: dict(n=6, nbmin=4, nbmax=6, kmax=9, tmot=28, dirs=[DROITE, BAS]),
    3: dict(n=6, nbmin=4, nbmax=7, kmax=9, tmot=26, dirs=[DROITE, BAS, DIAG]),
    4: dict(n=7, nbmin=5, nbmax=8, kmax=10, tmot=24, dirs=[DROITE, BAS, DIAG]),
    5: dict(n=7, nbmin=5, nbmax=9, kmax=10, tmot=22, dirs=TOUTES),
    6: dict(n=8, nbmin=6, nbmax=10, kmax=11, tmot=20, dirs=TOUTES),
    7: dict(n=8, nbmin=7, nbmax=11, kmax=11, tmot=19, dirs=TOUTES),
    8: dict(n=9, nbmin=8, nbmax=12, kmax=12, tmot=18, dirs=TOUTES),
    9: dict(n=9, nbmin=9, nbmax=13, kmax=12, tmot=17, dirs=TOUTES),
    10: dict(n=10, nbmin=10, nbmax=14, kmax=12, tmot=16, dirs=TOUTES),
}
NB_NIVEAUX = len(NIVEAUX)
LONGUEUR_MIN_CACHE = 4

# =====================================================
# 2. LOGIQUE DE GRILLE (identique à Pygame)
# =====================================================
def conflit(mot, autres):
    r = mot[::-1]
    for a in autres:
        if mot in a or r in a or a in mot or a in r:
            return True
    return False

def placer_mot(grille, n, mot, dirs, essais=50):
    L = len(mot)
    meilleur = None
    for _ in range(essais):
        dl, dc = random.choice(dirs)
        l, c = random.randrange(n), random.randrange(n)
        fl, fc = l + dl * (L - 1), c + dc * (L - 1)
        if not (0 <= fl < n and 0 <= fc < n):
            continue
        neuf = 0
        ok = True
        cases = []
        for i in range(L):
            a, b = l + dl * i, c + dc * i
            g = grille[a][b]
            if g == "":
                neuf += 1
            elif g != mot[i]:
                ok = False
                break
            cases.append((a, b))
        if ok and neuf > 0:
            score = neuf + random.random()
            if meilleur is None or score > meilleur[0]:
                meilleur = (score, cases)
    return meilleur[1] if meilleur else None

def tentative(n, cfg, pool, niveau, deja_vus, kmax):
    tendance = (niveau - 5.5) / 4.5
    candidats = [m for m in pool if len(m[0]) <= n]
    candidats.sort(key=lambda m: (4 if m[0] in deja_vus else 0) - 0.4 * tendance * len(m[0]) + random.uniform(0, 3))
    grille = [[""] * n for _ in range(n)]
    places = []
    for m in candidats:
        if len(places) >= cfg["nbmax"]:
            break
        if conflit(m[0], [p[0][0] for p in places]):
            continue
        cases = placer_mot(grille, n, m[0], cfg["dirs"])
        if not cases:
            continue
        for i, (a, b) in enumerate(cases):
            grille[a][b] = m[0][i]
        places.append((m, cases))
        if len(places) >= cfg["nbmin"]:
            vides = [(l, c) for l in range(n) for c in range(n) if grille[l][c] == ""]
            k = len(vides)
            if k < LONGUEUR_MIN_CACHE:
                return None
            if k <= kmax:
                noms = {p[0][0] for p in places}
                cand = [h for h in pool if len(h[0]) == k and h[0] not in noms]
                if cand:
                    neufs = [h for h in cand if h[0] not in deja_vus]
                    cache = random.choice(neufs or cand)
                    for (l, c), lettre in zip(vides, cache[0]):
                        grille[l][c] = lettre
                    return grille, places, cache
    return None

def grille_secours(langue):
    pool = MOTS[langue]
    n = 6
    while True:
        grille = [[""] * n for _ in range(n)]
        places = []
        cand = [m for m in pool if len(m[0]) <= n]
        random.shuffle(cand)
        for m in cand:
            if len(places) >= 4:
                break
            if conflit(m[0], [p[0][0] for p in places]):
                continue
            cases = placer_mot(grille, n, m[0], [DROITE, BAS, DIAG])
            if cases:
                for i, (a, b) in enumerate(cases):
                    grille[a][b] = m[0][i]
                places.append((m, cases))
        if len(places) >= 3:
            break
    for l in range(n):
        for c in range(n):
            if grille[l][c] == "":
                grille[l][c] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return n, grille, [p[0] for p in places], {p[0][0]: p[1] for p in places}, None

def creer_grille(langue, niveau, deja_vus, budget=0.4):
    cfg = NIVEAUX[niveau]
    pool = MOTS[langue]
    kmax = min(cfg["kmax"], max(len(m[0]) for m in pool))
    for n in range(cfg["n"], 4, -1):
        longs = sorted((len(m[0]) for m in pool if len(m[0]) <= n), reverse=True)[:cfg["nbmax"]]
        if n * n - kmax > 0.85 * sum(longs):
            continue
        fin = time.time() + budget
        while time.time() < fin:
            r = tentative(n, cfg, pool, niveau, deja_vus, kmax)
            if r:
                grille, places, cache = r
                return (n, grille, [p[0] for p in places], {p[0][0]: p[1] for p in places}, cache)
    return grille_secours(langue)

# =====================================================
# 3. INTERFACE KIVY
# =====================================================
class Case(Label):
    def __init__(self, ligne, col, **kwargs):
        super().__init__(**kwargs)
        self.ligne = ligne
        self.col = col
        self.selected = False

class GrilleWidget(Widget):
    def __init__(self, jeu, **kwargs):
        super().__init__(**kwargs)
        self.jeu = jeu
        self.selection = []
        self.bind(pos=self.redessiner, size=self.redessiner)
        
        # On crée les labels une seule fois
        self.cases_labels = []
        for l in range(10): # Max 10x10
            ligne_labels = []
            for c in range(10):
                case = Case(l, c)
                case.font_size = '20sp'
                case.bold = True
                case.color = (0.15, 0.15, 0.25, 1)
                self.add_widget(case)
                ligne_labels.append(case)
            self.cases_labels.append(ligne_labels)
            
        self.bind(pos=self.repositionner, size=self.repositionner)

    def charger_grille(self, grille):
        self.grille_data = grille
        self.n = len(grille)
        self.selection = []
        self.repositionner()
        self.redessiner()

    def repositionner(self, *args):
        if not hasattr(self, 'n'): return
        n = self.n
        # Calcul de la taille optimale d'une case
        taille_case = min(self.width / n, self.height / n) * 0.9
        self.taille_case = taille_case
        offset_x = (self.width - (taille_case * n)) / 2
        offset_y = (self.height - (taille_case * n)) / 2
        
        for l in range(10):
            for c in range(10):
                label = self.cases_labels[l][c]
                if l < n and c < n:
                    label.text = self.grille_data[l][c]
                    label.size = (taille_case, taille_case)
                    label.pos = (self.x + offset_x + c * taille_case, 
                                 self.y + offset_y + (n - 1 - l) * taille_case)
                    label.font_size = taille_case * 0.5
                    label.opacity = 1
                else:
                    label.opacity = 0

    def get_case_at_pos(self, x, y):
        if not hasattr(self, 'n'): return None
        n = self.n
        taille_case = self.taille_case
        offset_x = (self.width - (taille_case * n)) / 2
        offset_y = (self.height - (taille_case * n)) / 2
        
        # Coordonnées locales
        lx = x - (self.x + offset_x)
        ly = y - (self.y + offset_y)
        
        c = int(lx // taille_case)
        l = n - 1 - int(ly // taille_case)
        
        if 0 <= l < n and 0 <= c < n:
            return (l, c)
        return None

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos): return False
        case = self.get_case_at_pos(touch.x, touch.y)
        if case:
            self.selection = [case]
            self.redessiner()
            return True
        return False

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos): return False
        case = self.get_case_at_pos(touch.x, touch.y)
        if case and case not in self.selection:
            # On vérifie que c'est bien une ligne continue
            if len(self.selection) > 0:
                last_l, last_c = self.selection[-1]
                dl = case[0] - last_l
                dc = case[1] - last_c
                if abs(dl) <= 1 and abs(dc) <= 1 and (dl == 0 or dc == 0 or abs(dl) == abs(dc)):
                    # On vérifie si on ne fait pas demi-tour sur une case déjà prise
                    if case not in self.selection:
                        self.selection.append(case)
                        self.redessiner()
                        return True
        return False

    def on_touch_up(self, touch):
        if self.selection:
            self.jeu.valider_selection(self.selection)
            self.selection = []
            self.redessiner()
            return True
        return False

    def redessiner(self, *args):
        self.canvas.after.clear()
        if not hasattr(self, 'n') or not self.selection:
            return
            
        with self.canvas.after:
            # Couleur de sélection
            Color(0.6, 0.7, 1, 0.5)
            
            n = self.n
            taille_case = self.taille_case
            offset_x = (self.width - (taille_case * n)) / 2
            offset_y = (self.height - (taille_case * n)) / 2
            
            # Dessin des mots déjà trouvés
            for mot, cases in self.jeu.trouves.items():
                cat = next(m[1] for m in self.jeu.mots if m[0] == mot)
                c_col = couleur_cat(cat)
                Color(c_col[0], c_col[1], c_col[2], 0.4)
                
                for i in range(len(cases) - 1):
                    l1, c1 = cases[i]
                    l2, c2 = cases[i+1]
                    x1 = self.x + offset_x + c1 * taille_case + taille_case/2
                    y1 = self.y + offset_y + (n - 1 - l1) * taille_case + taille_case/2
                    x2 = self.x + offset_x + c2 * taille_case + taille_case/2
                    y2 = self.y + offset_y + (n - 1 - l2) * taille_case + taille_case/2
                    Line(points=[x1, y1, x2, y2], width=taille_case*0.7)
            
            # Dessin de la sélection en cours
            if self.selection:
                Color(0.3, 0.5, 0.9, 0.5)
                points = []
                for (l, c) in self.selection:
                    x = self.x + offset_x + c * taille_case + taille_case/2
                    y = self.y + offset_y + (n - 1 - l) * taille_case + taille_case/2
                    points.extend([x, y])
                if len(points) >= 4:
                    Line(points=points, width=taille_case*0.7, joint='round')
                elif len(points) == 2:
                    Line(points=[points[0], points[1], points[0]+1, points[1]+1], width=taille_case*0.7)

class JeuKivy(App):
    def build(self):
        self.title = "NSOE WORD"
        Window.clearcolor = (0.33, 0.76, 0.89, 1) # Fond bleu clair
        
        self.langue = "fr"
        self.niveau = 1
        self.score = 0
        self.trouves = {}
        self.mots = []
        self.cache = None
        self.deja_vus = {"fr": set(), "en": set(), "ff": set()}
        
        self.root_layout = FloatLayout()
        
        # Bouton Nouvelle Partie (pour test)
        self.btn_test = Button(text="Nouveau niveau", size_hint=(0.4, 0.1), pos_hint={'x': 0.05, 'top': 0.95})
        self.btn_test.bind(on_release=lambda x: self.lancer_niveau())
        self.root_layout.add_widget(self.btn_test)
        
        # Label info mot
        self.label_info = Label(text="", size_hint=(0.8, 0.1), pos_hint={'x': 0.1, 'y': 0.75}, color=(0,0,0,1))
        self.root_layout.add_widget(self.label_info)
        
        # Grille
        self.grille_widget = GrilleWidget(self, size_hint=(0.9, 0.6), pos_hint={'center_x': 0.5, 'y': 0.1})
        self.root_layout.add_widget(self.grille_widget)
        
        # On lance un niveau au démarrage
        Clock.schedule_once(lambda dt: self.lancer_niveau(), 0.1)
        
        return self.root_layout

    def lancer_niveau(self):
        n, grille, mots, positions, cache = creer_grille(self.langue, self.niveau, self.deja_vus[self.langue])
        self.mots = mots
        self.trouves = {}
        self.cache = cache
        self.score = 0
        self.grille_widget.charger_grille(grille)
        self.label_info.text = f"Mots à trouver : {len(mots)}"
        if cache:
            self.label_info.text += f" | Mot caché : {len(cache[0])} lettres"

    def valider_selection(self, selection):
        if len(selection) < 2:
            return
        lettres = "".join([self.grille_widget.grille_data[l][c] for l, c in selection])
        
        for entree in self.mots:
            mot, cat, sens, prono = entree
            if mot in self.trouves:
                continue
            if lettres == mot:
                self.trouves[mot] = list(selection)
                self.score += 10 + 2 * len(mot)
                self.label_info.text = f"Trouvé ! {mot} = {sens}"
                self.grille_widget.redessiner()
                
                if len(self.trouves) == len(self.mots):
                    self.label_info.text = "Bravo ! Tu as trouvé tous les mots."
                return
        
        self.label_info.text = "Raté, réessaie."

if __name__ == '__main__':
    JeuKivy().run()
