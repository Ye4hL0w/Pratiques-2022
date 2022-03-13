def recherche(elt,tab):
    sortie=-1
    for indice in range(len(tab)):
        if tab[indice] == elt:
            sortie=indice
    return sortie

class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse
   
    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")] 
        
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           réservée, False sinon"""
        return self.adresse=='192.168.0.0' or self.adresse=='192.168.0.255'
             
    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse 
           IP qui suit l’adresse self
           si elle existe et False sinon"""
        if self.liste_octet()[3] < 254:
            octet_nouveau =  + self.adresse.liste_octet[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

adresse1=AdresseIP('192.168.0.1')
adresse2=AdresseIP('192.168.0.2')
adresse3=AdresseIP('192.168.0.255')