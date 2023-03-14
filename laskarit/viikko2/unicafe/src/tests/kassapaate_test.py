import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_rahaa_on_100000(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edulliset_on_0(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_maukkaat_on_0(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
    
    def test_kateisosto_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        
    def test_kateisosto_edullinen_kassassa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_kateisosto_maukas_kassassa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_edullinen_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kateisosto_maukas_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_kateisosto_edullinen_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        
    def test_kateisosto_maukas_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        
    def test_kateisosto_edullinen_ei_riittava_kassassa_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kateisosto_maukas_ei_riittava_kassassa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisosto_edullinen_ei_riittava_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_kateisosto_maukas_ei_riittava_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_korttiosto_edullinen(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        
    def test_korttiosto_maukas(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
    
    def test_korttiosto_edullinen_kortilla_rahaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.60 euroa")
    
    def test_korttiosto_maukas_kortilla_rahaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        
    def test_korttiosto_edullinen_edulliset(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_korttiosto_maukas_maukkaat(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_korttiosto_edullinen_ei_riittava(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        
    def test_korttiosto_maukas_ei_riittava(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        
    def test_korttiosto_kassassa_rahaa_ei_muutu(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kortin_saldo_muuttuu_ladattaessa_kortille(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        
    def test_kortille_ladattaessa_kassassa_rahaa_muuttuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)