# Multilayer-Perceptron-FIA---UFPEL:  Relatório final do Trabalho

**Nome dos Componentes:** Arthur Siqueira e Silva, Ihan Belmonte Bender

**Erro médio quadratico:** 0.0857

**Numero de épocas usadas:** 500 (iterações de 5 valores para mudança de pesos)

**Porcentagem do dataset usada para aprendizado:** 70%
**Porcentagem do dataset usada para teste:** 30%

**Topologia e arquitetura RNA:**
A rede neural foi construída através da linguagem Python, utilizando keras (theano como backend). Utiliza também o numpy, para trabalhar com matrizes

Consiste em:
- Input Layer de 9 Valores (ID excluido) utilizando Rectified Linear Unit ('relu') como ativação.
- 2 Hidden layers, com 15 e 12 "neurônios", respectivamente. Ambos utilizando Rectified Linear Unit ('relu') como ativação.
- Output Layer com 1 saida, utilizando Sigmoid ('sigmoid')


**Análise do comportamento da rede:**

A partir do treinamento da rede, a porcentagem de erros para os casos de teste chegaram a 100% após algumas iterações, baixando levemente mas convergindo novamente a 100%. Na bateria de testes, haviam 489 casos, enquanto na avaliação 210.
Na avaliação, onde a rede foi testada com valores que ainda não conhecia, obteve 91,43% de acertos, um valor bastante alto, tendo em vista que o treinamento foi pequeno e não suficiente para cobrir todos os casos.


Observações:

- A seed para gerar os valores aleatórios na numpy foi o número 17 (sem razão especial, podendo ser mudada).

- Para substituir os valores perdidos dos dados, foi obtido o valor medio da classe (2). Ai então, todos os valores perdidos foram trocados pelo valor 2.

- A classe "ID" foi ignorada, devido ao tamanho dos valores e por não fazer diferença no caso.

- Os valores da classe de "resposta" foram mudados de 2 e 4 para 0 e 1, respectivamente.

- No calculo do Erro médio quadrático, já que a rede é de classificação binária, foram considerados todos os erros como 1 e acertos como zero (de erro). Ao final, é dividido o somatório pelo total de testes, obtendo o erro médio da avaliação.


