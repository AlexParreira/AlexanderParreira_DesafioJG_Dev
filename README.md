Autor: Alexander de Oliveira Parreir<br>
Turma: Super Esteg Jovem Gênios<br>
Data da Entrega:07/07/2020<br>


### Descrição
<br>
O software consiste em um game em linha de comando que reproduz parte do jogo O Show do Milhão, um jogo de perguntas e respostas com objetivo de premiar o vencedor com um prêmio de 1 milhão de reais, o jogador inicia com R$500,00 o jogo  é dividido em  4 rodadas contendo 24 perguntas cada uma com um valor, cada rodada valendo um determinado valor.

### Operação do Programa
<br>
O usuário deve fornecer os valores conforme solicitado pelo programa. Os valores são solicitados. um por vez, por uma mensagem informando o'que deve ser digitado. Após cada digitação o usuário deverá pressionar a tecla ENTER para chamar a próxima solicitação.

### Algoritmo Utilizado
<br>

Após cada pergunta o usuário terá que digitar entradas específicas para cada situação como:

    -Se a entrada for R:
		Uma mensagem solicitando uma entrada com a resposta da questão aparecerá.
		
    -Se a entrada for P:
		Uma mensagem informando o número de pulo restante aparecerá e iniciará uma nova questão, porém caso o variável cont_pulo esteja em 0, uma mensagem vai informar o valor da variável seguida de uma mensagem informando que ao continuar ele aceitará estar desistindo da partida, para continuar ou não ele terá que confirmar com as letras ‘N’ para não e ‘S‘ para sim.
		
    	-Se a entrada for S:
			Uma mensagem de encerramento vai aparecer.

    	-Se a entrada for N:
			A variável cont_pulo permanecerá em 0 e a pergunta aparecerá novamente.

    -Se a entrada for J:
	Uma mensagem mostrando o valor da variável cont_ajuda aparecerá e a pergunta será refeita porém duas questões erradas ficaram em vermelho e uma mensagem solicitando a resposta aparecerá. Caso o número de ajudas tenha acabado, uma mensagem informará sobre, uma mensagem informando que ele não possui mais ajuda aparecerá e que ele poderá responder ou pular caso ainda tenha pulos.
    -Se a entrada for qualquer outra:
	Uma mensagem de entrada invalida aparecerá e a pergunta será refeita.
Condições de contorno
O programa aceita qualquer valor de entrada, tanto tipos caractere ou inteiro.

### Teste
<br>

O programa foi testado através de entra certas e entradas erradas. O programa se comportou de maneira desejada.

### Sugestões
<br>

Para ter mais valores de pergunta basta adicioná las dentro da variável Perguntas não esquecendo de adicionar um dict  ao Respostas e a resposta correta ao Teste_Resp

### Comentários 
<br>

A complexidade do programa serviu para testar e mostrar meu desempenho para etapa processo seletivo do estágio.
