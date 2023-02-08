# ExistDB-1
- Afegeix el fitxer a la col·lecció MP06UF3.
  - Crea les següents consultes (captura del teu programa amb el query i el resultat):
  - Mostra els títols dels CDs de Tina Turner.
  - Mostra els artistes dels CDs de la EU.
  - Mostra els artistes dels CDs que no siguin de la EU.
  - Mostra el títol concatenat amb l'any dels CDs de Andrea Bocelli.
  - Mostra els títols dels CDs anteriors a 1990.
  - Mostra els títols dels CDs de 1990 o posteriors.
  - Mostra els títols dels CDs que tinguin un preu inferior a 9 o superior a 10.
  - Mostra els títols dels CDs que tinguin un preu inferior a 10 i superior a 9.
  - Mostra els artistes dels CDs de la companyia EMI.
---
### Mostra els títols dels CDs de Tina Turner
~~~
/CATALOG/CD[ARTIST='Tina Turner']/TITLE
~~~
![Selecció_104](https://user-images.githubusercontent.com/91152783/217576998-fff0c8d3-72ca-4993-b7ca-61c5d7580996.png)
--
### Mostra els artistes dels CDs de la EU
~~~
/CATALOG/CD[COUNTRY='EU']/ARTIST/text()
~~~
![Selecció_103](https://user-images.githubusercontent.com/91152783/217576703-9e05a219-a5c7-457c-a264-f61a709a45ce.png)
--
### Mostra els artistes dels CDs que no siguin de la EU
~~~
/CATALOG/CD[not (COUNTRY='EU')]/ARTIST/text()
~~~
![Selecció_105](https://user-images.githubusercontent.com/91152783/217579287-06affe63-5e1e-4c4b-891b-92983da9286f.png)
--
### Mostra el títol concadenat amb l'any dels CDs de Andrea Bocelli.
~~~
concat("El títol es ", /CATALOG/CD[ARTIST='Andrea Bocelli']/TITLE/text(), "i es de l'any ", /CATALOG/CD[ARTIST='Andrea Bocelli']/YEAR/text())
~~~
![Selecció_106](https://user-images.githubusercontent.com/91152783/217584120-d5bab8e9-3c6f-410d-9c01-c382db132cdc.png)
--
### Mostra els títols dels CDs anteriors a 1990.
~~~
/CATALOG/CD[YEAR<'1990']/TITLE/text()
~~~
![Selecció_108](https://user-images.githubusercontent.com/91152783/217587038-1e96d37d-dfcf-463f-b861-b33c0ab45b86.png)
