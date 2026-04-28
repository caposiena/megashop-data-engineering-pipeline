# MegaShop Data Engineering Pipeline

Progetto finale del modulo di Data Engineering.

## Obiettivo

L’obiettivo è simulare il lavoro di un Data Engineer, costruendo una pipeline dati che gestisca grandi volumi di informazioni passando da strumenti base (Pandas) a tecnologie Big Data (Dask e PySpark).

## Struttura del progetto

* data_local: contiene i dati (json, parquet e output finale)
* src: contiene gli script Python
* reports: contiene il grafico finale

## Esercizio 1

* Lettura file JSON con Pandas (uno alla volta)
* Uso di Dask per leggere tutti i file insieme
* Aggregazioni sui dati

## Esercizio 2

* Creazione pipeline ETL con PySpark
* Join tra transazioni, prodotti e regioni
* Creazione dataset finale
* Salvataggio in formato parquet partizionato per anno

## Esercizio 3

* Calcolo fatturato per categoria
* Conversione in Pandas
* Creazione grafico con Matplotlib/Seaborn

## Esercizio 4 (bonus)

* Streaming con Spark
* Lettura file JSON in tempo reale
* Conteggio transazioni per regione

## Tecnologie usate

Python, Pandas, Dask, PySpark, Matplotlib, Seaborn

## Note

Per eseguire PySpark su Windows è stato necessario configurare JAVA_HOME e HADOOP_HOME.
