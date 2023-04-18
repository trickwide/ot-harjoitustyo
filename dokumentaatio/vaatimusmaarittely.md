# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa omista tuloistaan ja menoistaan. Sovelluksessa on kirjautumismahdollisuus, joten useampi käyttäjä voi käyttää sovellusta ilman, että käyttäjät näkevät toistensa tekemiä budjetteja.

## Käyttäjät

Alkuvaiheessa sovelluksella on vain yksi käyttäjärooli eli _normaali käyttäjä_. Tavoitteena on myöhemmin lisätä hallinnollinen "super user" eli _pääkäyttäjä_, jolla on laajemmat käyttöoikeudet.

## Suunnitellut toiminnallisuudet

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen :heavy_check_mark:
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 5 merkkiä :heavy_check_mark:
- Käyttäjä voi kirjautua järjestelmään :heavy_check_mark:
  - Käyttäjä pääsee kirjautumaan järjestelmään, kun on syöttänyt olemassaolevan käyttäjätunnuksen ja salasanan kirjautumislomakkeelle :heavy_check_mark:
  - Mikäli käyttäjätunnusta ei ole olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä :heavy_check_mark:

### Kirjautumisen jälkeen

- Käyttäjä näkee budjettinsa eriteltynä: _tulot_, _menot_, _budjetti_ :heavy_check_mark:
- Käyttäjä voi syöttää budjettinsa :heavy_check_mark:
- Käyttäjä voi syöttää uuden tulon :heavy_check_mark:
  - Järjestelmään syötetty tulo näkyy vain nykyiselle kirjautuneelle käyttäjälle :heavy_check_mark:
- Käyttäjä voi syöttää uuden menon :heavy_check_mark:
  - Järjestelmään syötetty tulo näkyy vain nykyiselle kirjautuneelle käyttäjälle :heavy_check_mark:
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
