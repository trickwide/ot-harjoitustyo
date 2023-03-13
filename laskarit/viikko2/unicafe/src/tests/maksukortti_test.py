import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")
    
    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        bool = self.maksukortti.ota_rahaa(250)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")
        self.assertEqual(bool, True)
        
    def test_saldo_ei_muutu_jos_otetaan_liikaa(self):
        bool = self.maksukortti.ota_rahaa(1500)
      
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(bool, False)
        
        
        
