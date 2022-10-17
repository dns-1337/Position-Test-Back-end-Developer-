Position Test Back-end Developer

Desenvolvimento de Produto

Objetivo:

O objetivo desse desafio é demonstrar sua experiência e conhecimento como
back-end developer, assim saberemos como você pensa e como resolve
problemas na vida real.

O Problema:

Desenvolver uma API que tenha um endpoint que receba duas informações como
parâmetro, sendo o primeiro :hour e o segundo :minute e seja capaz de devolver

o ângulo entre os 2 ponteiros do relógio.

Requisitos do desafio:

● O movimento dos ponteiros ocorrem de minuto em minuto;
● Construir uma base Postgresql para armazenar as solicitações (id, hour,
minute, angle, date);
● O resultado não deverá ser recalculado caso a mesma consulta já tenha
sido executada;
● Deve ser retornado sempre o valor arredondado para o menor ângulo.

Exemplo de resultado:

REQUEST: $ curl http://localhost:8080/v{n}/rest/clock/6/0
RESULT: {"angle":180}

REQUEST: $ curl http://localhost:8080/v{n}/rest/clock/3
RESULT: {"angle":90}

REQUEST: $ curl http://localhost:8080/v{n}/rest/clock/9
RESULT: {"angle":90}

Requisitos técnicos:

● O desafio deve ser entregue escrito em Javascript (nodejs), golang, Scala
ou Python;

● O projeto precisa ser entregue em um repositório git no github (público)
sem mencionar a Harmo;

● Compartilhar em um diretório sql o dump da base com registros já gerados
pelo software;

● A interface de comunicação é REST;

● Conter documentação detalhada de como utilizar e rodar o projeto;

● O Content-Type de retorno deve ser JSON.
Diferenciais:

● Cobertura de testes unitários;

● Entregar o projeto preparado para rodar em um ambiente containerizado.
