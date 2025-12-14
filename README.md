# Pako vankilasta

Tekstipohjainen seikkailupeli, jossa pelaajan tehtävänä on paeta sähkökatkon runtelemaa vankilaa tutkimalla ympäristöä, keräämällä esineitä ja tekemällä oikeita valintoja. Projekti on toteutettu Pythonilla.

---

## Pelin idea

Pelaaja herää vankisellistä tilanteessa, jossa vankila on yllättäen autio. Sähköt ovat poikki ja monet ovet ovat auki. Tutkimalla vankilaa, keräämällä esineitä ja käyttämällä niitä oikein pelaaja voi lopulta paeta ulkomaailmaan.

Pelin lopussa pelaajan suoritus arvioidaan pisteiden perusteella ja hän saa pistemääräänsä vastaavan loppuviestin.

---

## Pelin ominaisuudet

* Tekstipohjainen seikkailupeli
* Useita huoneita ja liikkumissuunta vaihtoehtoja
* Esinejärjestelmä (ota, pudota, tarkista, käytä)
* Pistejärjestelmä
* Useita mahdollisia lopputuloksia pistemäärän mukaan
* Apujärjestelmä (`apua`-komento)

---

## Projektin rakenne

```
pako-vankilasta/
│
├── main.py        # Pelin käynnistys ja tervetulotoivotus
├── rooms.py       # Kaikki huoneet ja niiden logiikka
├── utils.py       # Yleiset toiminnot (komennot, pisteet, peli loppu)
├── items.py       # Esineet ja inventaario
└── README.md      # Projektin dokumentaatio
```

---

## Käytettävät komennot

Pelaaja voi käyttää seuraavia komentoja pelin aikana:

* `mene <suunta>` – Liiku huoneesta toiseen (i, l, p, e)
* `katsele` / `tutki` – Katso huoneen kuvaus uudelleen
* `ota <esine>` – Ota esine mukaasi
* `pudota <esine>` – Pudota esine huoneeseen
* `mukana` – Näytä inventaario
* `tarkista <esine>` – Tarkista esineen kuvaus
* `lataa <esine1> <esine2>` – Yhdistä esineitä (esim. taskulamppu + paristo)
* `syö <esine>` – Syö esine (jos mahdollista)
* `pue <esine>` – Pue esine päällesi
* `lue <esine>` – Lue esine
* `apua` – Näytä kaikki käytettävissä olevat komennot
* `lopeta` – Lopeta peli

---

##  Pelin loppu

Peli päättyy, kun pelaaja onnistuu pakenemaan vankilasta. Lopussa:

* näytetään pelaajan nimi
* näytetään lopullinen pistemäärä
* annetaan loppuviesti suorituksen perusteella

---

##  Teknologiat

* Python 3
* Ei ulkoisia kirjastoja

---

##  Tekijä

**Ilmari Takkunen**
GitHub: [ilmaritak]

---

## Huomioita

Tämä projekti on tarkoitettu oppimistarkoitukseen ja pythonin perusmekaniikkojen harjoitteluun. Koodirakenne on pidetty selkeänä ja helposti laajennettavana.

---

Hyviä pelihetkiä ja onnea pakoon!
