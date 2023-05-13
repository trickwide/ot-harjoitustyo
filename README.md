# Budget tracker

Sovelluksen avulla käyttäjät voivat asettaa itselleen budjetin ja tarkkailla sen muutosta tulojen sekä menojen suhteen. Jokaisella rekisteröityneellä käyttäjällä on oma yksilöllinen budjettinäkymä.

Tämä sovellus on Helsingin yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikka -kurssin harjoitustyö.

## Huomio Python-versiosta

Sovelluksen käyttäminen vaatii vähintään Python-version `3.8`. Sovelluksen toimivuutta vanhemmilla versioilla ei voi taata.

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)

- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

- [Changelog](dokumentaatio/changelog.md)

- [Releases](https://github.com/trickwide/ot-harjoitustyo/releases)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [pylintrc](.pylintrc) määrittelemät tarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```
