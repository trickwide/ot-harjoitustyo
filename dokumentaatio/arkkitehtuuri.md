# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraavanlainen:

![Pakkausrakenne](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus _ui_ sisältää käyttöliittymästä, _database_ tietojen pysyväistallennuksesta ja _services_ tietojen tarkistuksesta vastaavan koodin.

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Rekisteröitymisnäkymä
- Kirjautumisnäkymä
- Päänäkymä ts. tietojen syöttö- ja tarkastelunäkymä

Jokainen käyttöliittymän näkymä on toteutettu omana luokkanaan. Vain yksi luokka on kerrallaan näkyvänä. Näkymien näyttämisesta vastaa [UI](../src/ui/user_interface.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta ja se kutsuu [database](../src/database/database.py) ja [services](../src/services/)-pakkauksien funktioita.

## Tietojen pysyväistallennus

Pakkauksen _database_ [database.py](../src/database/database.py)-tiedosto huolehtii tietojen tallentamisesta SQLite-tietokantaan.

## Päätoiminnallisuudet

### Uuden käyttäjän rekisteröinti

```mermaid
sequenceDiagram
    User->>Registration_screen: User opens application
    Registration_screen->>Registration_screen: __init__()
    Registration_screen->>CTk: create CTkEntry objects
    User->>Registration_screen: enter username
    User->>Registration_screen: enter password
    User->>Registration_screen: enter password confirmation
    User->>Registration_screen: click register
    Registration_screen->>Registration_screen: validate_registration()
    Registration_screen->>Validation: is_username_valid()
    alt username not valid
        Registration_screen->>Registration_screen: display_error_message()
    end
    Registration_screen->>Validation: is_password_valid()
    alt password not valid
        Registration_screen->>Registration_screen: display_error_message()
    end
    Registration_screen->>Registration_screen: compare passwords
    alt passwords do not match
        Registration_screen->>Registration_screen: display_error_message()
    end
    Registration_screen->>Database: create_connection()
    Registration_screen->>Database: add_user()
    alt user already exists
        Registration_screen->>Registration_screen: display_error_message()
    else registration successful
        Registration_screen->>Registration_screen: destroy()
        Registration_screen->>User: show_login_view()
    end
```

### Käyttäjän kirjautuminen

```mermaid
sequenceDiagram
    Login_screen->>Validation: validate_login(username, password)
    Validation->>Database: get_user(conn, username, password_hash)
    Database-->>Validation: user (if exists) or None
    alt user exists and password is correct
        Validation-->>Login_screen: show_main_window(user_id)
    else user doesn't exist or password is incorrect
        Validation-->>Login_screen: display_error_message("Invalid username or password")
    end
```

### Tietojen syöttäminen

```mermaid
sequenceDiagram
    User->>MainWindow: Select Option from Dropdown
    User->>MainWindow: Enter Value in Entry Field
    User->>MainWindow: Click Submit Button
    MainWindow->>Database: add_transaction
    MainWindow->>Database: get_budget_summary
    Database-->>MainWindow: Return budget_summary
    MainWindow->>Database: get_expense_summary
    Database-->>MainWindow: Return expense_summary
    MainWindow->>Database: get_income_summary
    Database-->>MainWindow: Return income_summary
    MainWindow-->>User: Update MainWindow
```

### Tietojen poistaminen

```mermaid
sequenceDiagram
    User->>MainWindow: Click on Delete Button in Transaction History
    MainWindow->>Database: delete_transaction
    MainWindow->>Database: get_budget_summary
    Database-->>MainWindow: Return budget_summary
    MainWindow->>Database: get_expense_summary
    Database-->>MainWindow: Return expense_summary
    MainWindow->>Database: get_income_summary
    Database-->>MainWindow: Return income_summary
    MainWindow-->>User: Update MainWindow
```
