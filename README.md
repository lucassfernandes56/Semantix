# Semantix
Semantix challenge

## Contexto
Gostaríamos de fazer um teste que será usado para sabermos a sua proficiência nas habilidades para a vaga. O teste consiste em algumas perguntas e exercícios práticos sobre Spark e as respostas e códigos implementados devem ser armazenados no GitHub. O link do seu repositório deve ser compartilhado conosco ao final do teste.

Quando usar alguma referência ou biblioteca externa, informe no arquivo README do seu projeto. Se tiver alguma dúvida, use o bom senso e se precisar deixe isso registrado na documentação do projeto.

## Perguntas de conhecimento

1. Qual​ o objetivo​ do​ comando​ *cache​* em​ Spark?

*R:* 

2. O​ mesmo​ código​ implementado​ em​ Spark​ é normalmente​ mais​ rápido​ que​ a implementação​ equivalente​ em
MapReduce.​ Por​ quê?

*R:*

3. Qual​ é a função​ do​ *SparkContext​*?

*R:*

4. Explique​ com​ suas​ palavras​ o que​ é *Resilient​ Distributed​ Datasets​​* (RDD).

*R:*

5. *GroupByKey​* é menos​ eficiente​ que *reduceByKey​* em​ grandes​ dataset.​ Por​ quê?

*R:*

6. Explique o que o código Scala abaixo faz.
```scala
val textFile​​ = sc​.textFile("hdfs://..."​)
val​​ counts​​ = textFile​.flatMap​(line​​ => line​.split​("")).map​(word​​ =>​​ (word​,​ 1)).reduceByKey​(_+_)
counts​.saveAsTextFile​("hdfs://..."​)
```

*R:*

## HTTP​ requests​ to​ the​ NASA​ Kennedy​ Space​ Center​ WWW​ server
*Fonte​ oficial​ do​ dateset​:* http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html
*Dados​:*
* [Jul​ 01​ to​ Jul​ 31,​ ASCII​ format,​ 20.7​ MB​ gzip​ compressed​, 205.2​ MB.](ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz)
* [Aug​ 04​ to​ Aug​ 31,​ ASCII​ format,​ 21.8​ MB​ gzip​ compressed​, 167.8​ MB.](ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz)
*Sobre o dataset​:* Esses dois conjuntos de dados possuem todas as requisições HTTP para o servidor da NASA Kennedy
Space​ Center​ WWW​ na​ Flórida​ para​ um​ período​ específico.


Os​ logs​ estão​ em​ arquivos​ ASCII​ com​ uma​ linha​ por​ requisição​ com​ as​ seguintes​ colunas:
* *Host fazendo a requisição​* . Um hostname quando possível, caso contrário o endereço de internet se o nome
não​ puder​ ser​ identificado.
* *Timestamp​* no​ formato​ "DIA/MÊS/ANO:HH:MM:SS​ TIMEZONE"
* *Requisição​ (entre​ aspas)*
* *Código​ do​ retorno​ HTTP*
* *Total​ de​ bytes​ retornados*

Obs: toda a análise foi feita com os datasets de julho e agosto combinados.

1. Número de hosts únicos.

*R:* 55 hosts únicos.

2. O total de erros 404.

*R:* 20901 erros do tipo 404.

3. Os 5 URLs que mais causaram erro 404.

*R:*

4. Quantidade de erros 404 por dia.

*R:*

5. O total de bytes retornados.

*R:*


## Bibliotecas e versões utilizadas

* Java 11.0.4
* Python 3.7
* Spark 2.4.4
* Scala 2.11.12 
* sbt 1.3.3