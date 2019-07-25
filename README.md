# AND - Author Name Disambiguation

## Project
This project has the purpose of training a classifier which will be able to tell if two biomedical articles belong to the same author. To do so, a bunch of features are extracted from the two articles, such as e-mail address, affiliation name, city, country, date and so on. The articles are all taken from PubMed. 

Various classifier are trained with different algorithms, such as Random Forest and K-NN. Also a Neural Network is implemented.

## Environment requirements
Python3, JDK 8 or greater, 20GB of free space on disk

## Set-up
### Step 1:
Download the Text Categorization API from the following link:
https://lexsrv2.nlm.nih.gov/LexSysGroup/Projects/tc/2011/release/tc2011.tgz

### Step 2:
Unzip the tgz file. This should generate a 'tc2011' folder. Move the tc2011/data folder to the repository under '/main/'.
To make the relative test work, copy the folder also under 'test/retrievers_test/' .

### Step 3:
Open the project in an IDE of your preferece (PyCharm suggested) and create a new virtual evironment using a python3 interpreter.
Install all the requirements specified in the 'requirements.txt' file.

## Dataset
These are the files that make up the AND corpus: 
(1) 1500_pairs_train.csv
(2) 400_pairs_test.csv

These files contain randomly selected pairs of MEDLINE publications sharing an author with the same last name and first initial.

Each file has the following headers:

PMID1/2 - pubmed ID of a first/second publication in a pair.
Last_name1/2 - Author last names.
Initials1/2 - Author initials.
First_name1/2 - Author first names
Authorship - YES means that the authors are the same person and NO otherwise.

You should cite this data with the following publication:

Dina Vishnyakova, Raul Rodriguez-Esteban, Fabio Rinaldi, A new approach and gold standard toward author disambiguation in MEDLINE, Journal of the American Medical Informatics Association, , ocz028, https://doi.org/10.1093/jamia/ocz028

https://academic.oup.com/jamia/advance-article-abstract/doi/10.1093/jamia/ocz028/5432091
