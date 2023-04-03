# Budget tracker

Sovelluksen avulla käyttäjät voivat asettaa itselleen budjetin ja tarkkailla sen muutosta tulojen sekä menojen suhteen. Jokaisella rekisteröityneellä käyttäjällä on oma yksilöllinen budjettinäkymä.

Tämä sovellus on Helsingin yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikka -kurssin harjoitustyö.

## Huomio Python-versiosta

Sovelluksen käyttäminen vaatii vähintään Python-version `3.8`. Sovelluksen toimivuutta vanhemmilla versioilla ei voi taata.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

- [Changelog](dokumentaatio/changelog.md)

## Asennus

⚠️ **Huom! Sovellus hyödyntää Pythonin UI-kirjastoa [customtkinter](https://github.com/TomSchimansky/CustomTkinter). Kirjaston asentaminen tapahtuu alla olevalla komennolla. Kirjasto tulee asentaa myös virtuaaliympäristössä, jotta testit toimivat.**

1. Asenna customtkinter -kirjasto komennolla:

```bash
pip install customtkinter

tai

pip3 install customtkinter
```

2. Asenna riippuvuudet komennolla:

```bash
poetry install
```

3. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

4. Käynnistä sovellus komennolla:

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
