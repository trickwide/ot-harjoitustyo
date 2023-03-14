# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa omista tuloistaan ja menoistaan. Sovelluksessa on kirjautumismahdollisuus, joten useampi käyttäjä voi käyttää sovellusta ilman, että käyttäjät näkevät toistensa tekemiä budjetteja.

## Käyttäjät

Alkuvaiheessa sovelluksella on vain yksi käyttäjärooli eli _normaali käyttäjä_. Tavoitteena on myöhemmin lisätä hallinnollinen "super user" eli _pääkäyttäjä_, jolla on laajemmat käyttöoikeudet.

## Suunnitellut toiminnallisuudet

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 5 merkkiä
- Käyttäjä voi kirjautua järjestelmään
  - Käyttäjä pääsee kirjautumaan järjestelmään, kun on syöttänyt olemassaolevan käyttäjätunnuksen ja salasanan kirjautumislomakkeelle
  - Mikäli käyttäjätunnusta ei ole olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen

- Käyttäjä näkee budjettinsa eriteltynä: _tulot_, _menot_, _budjettia jäljellä_
- Käyttäjä voi syöttää uuden tulon
  - Järjestelmään syötetty tulo näkyy vain nykyiselle kirjautuneelle käyttäjälle
- Käyttäjä voi syöttää uuden menon
  - Järjestelmään syötetty tulo näkyy vain nykyiselle kirjautuneelle käyttäjälle
- Käyttäjä voi poistaa kirjaamansa tulon
- Käyttäjä voi poistaa kirjaamansa menon
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion valmistumisen jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Edellisen kuukauden budjetin tarkastelu
- Budjetin jakautumisen esittäminen viikkoerittelyllä
- Näkymä, joka näyttää vain tulot tai menot
- Budjettien nimeäminen ja budjettien välillä vaihtaminen
- Salasanan muokkaaminen
- Käyttäjätunnuksen (ja siihen liittyvien budjettien) poisto
- Tulojen ja menojen syöttäminen toisille käyttäjille (pääkäyttäjä-ominaisuus)
- Käyttäjien yhdistäminen ryhmiin (pääkäyttäjä-ominaisuus)
- Ryhmäkohtainen budjettinäkymä (pääkäyttäjä-ominaisuus)
