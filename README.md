# Semantix
Semantix challenge

## Contexto
Gostaríamos de fazer um teste que será usado para sabermos a sua proficiência nas habilidades para a vaga. O teste consiste em algumas perguntas e exercícios práticos sobre Spark e as respostas e códigos implementados devem ser armazenados no GitHub. O link do seu repositório deve ser compartilhado conosco ao final do teste.

Quando usar alguma referência ou biblioteca externa, informe no arquivo README do seu projeto. Se tiver alguma dúvida, use o bom senso e se precisar deixe isso registrado na documentação do projeto.

## Perguntas de conhecimento

1. Qual​ o objetivo​ do​ comando​ *cache​* em​ Spark?

 *R:* Ó objetivo é permitir que os arquivos que estão sendo trabalhados sejam armazenados em cache, poupando processamentos desnecessários do tipo "lazy" que ja foram feitos e salvando-os na memória.

2. O​ mesmo​ código​ implementado​ em​ Spark​ é normalmente​ mais​ rápido​ que​ a implementação​ equivalente​ em
MapReduce.​ Por​ quê?

*R:* Um dos principais fatores que tornam as aplicações desenvolvidas em MapReduce mais lentas que o Spark é o uso da memória. É bastante comum ter que rodar diversas rotinas em sequência em MapReduce, nesse cenário cada resultado é armazenado no disco e para ser passado para a rotina seguinte tem que ser lido do disco novamente, tornando o processo ineficiênte. O Spark consegue um desempenho superior por permitir que os resultados sejam passados imediatamente para as rotinas seguitnes atraves do uso do "caching", onde os dados são armazenados diretamente na memória.

1. Qual​ é a função​ do​ *SparkContext​*?

*R:* Tem como função permitira as configurações que vão ser utilizadas na alocação de recursos do Spark, como memória e processadores, numero de cores. Também usa-se o SparkContext para criar RDDs, colocar rotinas em execução.

4. Explique​ com​ suas​ palavras​ o que​ é *Resilient​ Distributed​ Datasets​​* (RDD).

*R:* RDDs são a principal abstração de dados do Spark. Eles são chamados Resilient por serem tolerantes à falha, isto é, são capazes de recomputar partes de dados perdidas devido a falhas nos nós e são Distributed porque podem estar divididos em partições através de diferentes nós em um cluster.

5. *GroupByKey​* é menos​ eficiente​ que *reduceByKey​* em​ grandes​ dataset.​ Por​ quê?

*R:* Utilizando o ReduceByKey  o Spark realiza a operação desejada em todos os elementos com a mesma "key" (chave) para obter um resultado parcial antes de enviar para os executores que calculam o resultado final, ou seja, o conjunto de dados que vai ser transferido já está pré agrupado, sendo assim um conjunto menor. 
Utilizando o GroupByKey e a agregação em seguida, todos os elementos são enviados sem uma pré execução, resultado em uma quantidade enorme de dados sendo transferidos. Essa quantidade pode passar a quantidade alocada de memória, exigindo a utilização do disco e diminuindo ainda mais a performance.

1. Explique o que o código Scala abaixo faz.
```scala
val textFile​​ = sc​.textFile("hdfs://..."​)
val​​ counts​​ = textFile​.flatMap​(line​​ => line​.split​(" "))
                    .map​(word​​ =>​​ (word​,​ 1))
                    .reduceByKey​(_+_)
counts​.saveAsTextFile​("hdfs://..."​)
```

*R:* Nesse código Scala um arquivo texto é lido (1ª linha), em seguida, cada linha do arquivo é quebrada em uma sequência de palavras (separadas por espaço, 2ª linha). Cada palavra é transformada para o tipo mapa, com "key" sendo a palavra e o "value" sendo 1 (3ª linha). Cada elemento mapeado é somado por "key" (4ª linha) e por fim o RDD contendo a quantidade de cada palavra no arquivo inicial é escrito em um arquivo texto.

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
* /pub/winvn/readme.txt -> 2004 erros do tipo 404
* /pub/winvn/release.txt -> 1732 erros do tipo 404
* /shuttle/missions/STS-69/mission-STS-69.html -> 683 erros do tipo 404
* /shuttle/missions/sts-68/ksc-upclose.gif -> 428 erros do tipo 404
* /history/apollo/a-001/a-001-patch-small.gif -> 384 erros do tipo 404

4. Quantidade de erros 404 por dia.

*R:*
* 01/Jul/1995	-> 316 erros do tipo 404
* 02/Jul/1995	-> 291 erros do tipo 404
* 03/Jul/1995	-> 474 erros do tipo 404
* 04/Jul/1995	-> 359 erros do tipo 404
* 05/Jul/1995	-> 497 erros do tipo 404
* 06/Jul/1995	-> 640 erros do tipo 404
* 07/Jul/1995	-> 570 erros do tipo 404
* 08/Jul/1995	-> 302 erros do tipo 404
* 09/Jul/1995	-> 348 erros do tipo 404
* 10/Jul/1995	-> 398 erros do tipo 404
* 11/Jul/1995	-> 471 erros do tipo 404
* 12/Jul/1995	-> 471 erros do tipo 404
* 13/Jul/1995	-> 532 erros do tipo 404
* 14/Jul/1995	-> 413 erros do tipo 404
* 15/Jul/1995	-> 254 erros do tipo 404
* 16/Jul/1995	-> 257 erros do tipo 404
* 17/Jul/1995	-> 406 erros do tipo 404
* 18/Jul/1995	-> 465 erros do tipo 404
* 19/Jul/1995	-> 639 erros do tipo 404
* 20/Jul/1995	-> 428 erros do tipo 404
* 21/Jul/1995	-> 334 erros do tipo 404
* 22/Jul/1995	-> 192 erros do tipo 404
* 23/Jul/1995	-> 233 erros do tipo 404
* 24/Jul/1995	-> 328 erros do tipo 404
* 25/Jul/1995	-> 461 erros do tipo 404
* 26/Jul/1995	-> 336 erros do tipo 404
* 27/Jul/1995	-> 336 erros do tipo 404
* 28/Jul/1995	-> 94 erros do tipo 404
* 01/Aug/1995	-> 243 erros do tipo 404
* 03/Aug/1995	-> 304 erros do tipo 404
* 04/Aug/1995	-> 346 erros do tipo 404
* 05/Aug/1995	-> 236 erros do tipo 404
* 06/Aug/1995	-> 373 erros do tipo 404
* 07/Aug/1995	-> 537 erros do tipo 404
* 08/Aug/1995	-> 391 erros do tipo 404
* 09/Aug/1995	-> 279 erros do tipo 404
* 10/Aug/1995	-> 315 erros do tipo 404
* 11/Aug/1995	-> 263 erros do tipo 404
* 12/Aug/1995	-> 196 erros do tipo 404
* 13/Aug/1995	-> 216 erros do tipo 404
* 14/Aug/1995	-> 287 erros do tipo 404
* 15/Aug/1995	-> 327 erros do tipo 404
* 16/Aug/1995	-> 259 erros do tipo 404
* 17/Aug/1995	-> 271 erros do tipo 404
* 18/Aug/1995	-> 256 erros do tipo 404
* 19/Aug/1995	-> 209 erros do tipo 404
* 20/Aug/1995	-> 312 erros do tipo 404
* 21/Aug/1995	-> 305 erros do tipo 404
* 22/Aug/1995	-> 288 erros do tipo 404
* 23/Aug/1995	-> 345 erros do tipo 404
* 24/Aug/1995	-> 420 erros do tipo 404
* 25/Aug/1995	-> 415 erros do tipo 404
* 26/Aug/1995	-> 366 erros do tipo 404
* 27/Aug/1995	-> 370 erros do tipo 404
* 28/Aug/1995	-> 410 erros do tipo 404
* 29/Aug/1995	-> 420 erros do tipo 404
* 30/Aug/1995	-> 571 erros do tipo 404
* 31/Aug/1995	-> 526 erros do tipo 404

5. O total de bytes retornados.

*R:* 65524314915 bytes retornados

## Bibliotecas e versões utilizadas

* Java 8
* Python 3.7
* Spark 2.4.4
* Scala 2.11.12 
* Pyspark 2.4.4