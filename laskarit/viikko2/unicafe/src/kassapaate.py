class Kassapaate:
    EDULLINEN = 240
    MAUKAS = 400
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0
        
    def _kateismaksu(self, maksu, hinta):
        if maksu >= hinta:
            self.kassassa_rahaa += hinta
            self._paivita_myydyt_lounaat(hinta)
            return maksu - hinta
        else:
            return maksu
          
    def _paivita_myydyt_lounaat(self, hinta):
        if hinta == self.EDULLINEN:
            self.edulliset += 1
        else:
            self.maukkaat += 1

    def syo_edullisesti_kateisella(self, maksu):
        return self._kateismaksu(maksu, self.EDULLINEN)

    def syo_maukkaasti_kateisella(self, maksu):
        return self._kateismaksu(maksu, self.MAUKAS)
          
    def _on_tarpeeksi_rahaa_kortilla(self, kortti, summa):
        return kortti.saldo >= summa

    def syo_edullisesti_kortilla(self, kortti):
        if self._on_tarpeeksi_rahaa_kortilla(kortti, self.EDULLINEN):
            kortti.ota_rahaa(self.EDULLINEN)
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti):
        if self._on_tarpeeksi_rahaa_kortilla(kortti, self.MAUKAS):
            kortti.ota_rahaa(self.MAUKAS)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return
