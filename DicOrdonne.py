#!/usr/bin/python3.4
# -*-coding:utf-8 -*

class DicOrdonne:
    """Création d'un dictionnaire ordonné, soit vide soit copié soit prérempli"""

    def __init__(self, base={}, **donnees):
        self._cles = []
        self._valeurs = []

        if type(base) not in (dict, DicOrdonne):
            raise TypeError( \
                    "le type attendu est un dictionnaire (usuel ou ordonne)")

        # on recupere les donnes de base
        for cle in base:
            self[cle] = base[cle]
            print(self[cle])

        # on recupere les donnees de donnees
        for cle in donnees:
            self[cle] = donnees[cle]
            print(cle)

    def __repr__(self):
        """representation de notre objet"""
        chaine = "{"
        premierPass = True
        for cle, valeur in self.items():
            if not premierPass:
                chaine += ", "
            else:
                premierPass = False
            chaine += repr(cle) + ": " + repr(valeur)
        chaine += "}"
        return chaine

    def __str__(self):
        """Affichage du dictionnaire"""
        return repr(self)

    def __len__(self):
        """renvoie la taille du dictionnaire"""
        return len(self._cles)

    def __contains__(self, cle):
        """renvoie true si la clé est dans la liste"""
        return cle in self._cles


    def __getitem__(self,cle):
        """renvoie la valeur correspond à la clé si elle existe"""
        if cle not in self._cles:
            raise KeyError( \
                "La clé",cle,"ne se trouve pas dans le dictionnaire")
        else:
            indice = self._cles.index(cle)
            return self._valeurs[indice]

    def __setitem__(self, cle, valeur):
        """Modifie une clé présente ou l'ajoute à la suite du dictionnaire"""
        if cle in self._cles:
            indice = self._cles.index(cle)
            self._valeurs[indice] = valeur
        else:
            self._cles.append(cle)
            self._valeurs.append(valeur)

    def __delitem__(self,cle):
        """supprime une clé"""
        if cle not in self.cles:
            raise KeyError( \
            "La clé", cle, "ne se trouve pas dans le dictionnaire")
        else:
            indice = self._cles.index(cle)
            del self._cles[indice]
            del self._valeurs[indice]

    def __iter__(self):
        """parcours de l'objet"""
        return iter(self._cles)

    def __add__(self, autreObjet):
        """renvoie un nouveau dictionnaire contenant les deux dictionnaires"""
        if not type(autreObjet) is type(self):
            raise TypeError( \
            "Impossible de concaténer", self, "et", autreObjet)
        else:
            nouveau = DicOrdonne()

            for cle, valeur in self.items():
                nouveau[cle] = valeur

            for cle, valeur in autreObjet.items():
                nouveau[cle] = valeur
            return nouveau

    def items(self):
        """renvoie un generateur avec les couples (cle, valeur)"""
        for i, cle in enumerate(self._cles):
            valeur = self._valeurs[i]
            yield (cle, valeur)

    def keys(self):
        """renvoie la liste des clés"""
        return list(self._cles)

    def values(self):
        """renvoie la liste des valeurs"""
        return list(self._valeurs)

    def reverse(self):
        """inversion du dictionnaire"""
        cles = []
        valeurs = []
        for cle, valeur in self.items():
            cles.insert(0,cle)
            valeurs.insert(0, valeur)
        self._cles = cles
        self._valeurs = valeurs

    def sort(self):
        """permet de trier le dictionnaire en fonction de ses clés"""
        clesTriees = sorted(self._cles)
        valeurs = []
        for cle in clesTriees:
            valeur = self[cle]
            valeurs.append(valeur)
        self._cles = clesTriees
        self._valeurs = valeurs
