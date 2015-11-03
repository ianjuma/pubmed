### Mining Pubmed data

#### Setting up

```python
$ sudo pip install -r requirements.txt
```


#### How to run

```python
$ python scrap_pubmed.py
```


#### Sample demo

```python
$ python scrap_pubmed.py

Enter keyword to search for: 
malaria
Enter number # of articles to fetch (number): 
1
Article ID:  26003037
ISSN No:  0065-308X
Date published: 2015-05-08
Impact factor - Article/ Journal not Found on cite factor

Development of malaria transmission-blocking vaccines: from concept to
product.

Despite decades of effort battling against malaria, the disease is still a
major cause of morbidity and mortality. Transmission-blocking vaccines (TBVs)
that target sexual stage parasite development could be an ... 

---------------------- AUTHORS ------------------------ 

Wu Yimin -- Laboratory of Malaria Immunology and Vaccinology, National
Institute of Allergy and Infectious Diseases, Rockville, MD, USA.
Sinden Robert E -- The Jenner Institute, Oxford, UK.
Churcher Thomas S -- MRC Centre for Outbreak Analysis and Modelling,
Department of Infectious Disease Epidemiology, School of Public Health,
Imperial College London, London, UK.
Tsuboi Takafumi -- Division of Malaria Research, Ehime University, Matsuyama,
total author # - 3 authors
---------------------------  END  ---------------------------------

```

### Output
```python
$ This produces a .txt file named pubmed.txt
```
