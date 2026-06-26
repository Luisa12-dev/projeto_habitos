 Sistema de Acompanhamento de Hábitos Saudáveis

Documentação do Projeto
Programação 1  ·  UPE  ·  Profª Aeda
1. Apresentação do Projeto
O Sistema de Acompanhamento de Hábitos Saudáveis é uma aplicação desenvolvida em Python com persistência de dados em SQLite, criada com o objetivo de auxiliar usuários no monitoramento de hábitos relacionados à saúde e ao bem-estar. A proposta do sistema é permitir que cada usuário cadastre seus hábitos, registre diariamente sua realização e acompanhe seu progresso por meio de relatórios.

O projeto foi desenvolvido no contexto da disciplina de Programação, com foco na aplicação prática de conceitos como modularização, persistência em banco de dados, operações de CRUD e organização de sistemas em camadas funcionais. Além disso, o sistema está alinhado ao ODS 3 — Saúde e Bem-Estar, pois incentiva a construção de rotinas mais saudáveis e o acompanhamento contínuo de práticas positivas no dia a dia.

2. Objetivo do Sistema
O objetivo do sistema é oferecer uma forma simples e organizada de registrar hábitos saudáveis e acompanhar sua execução ao longo do tempo. Com isso, o usuário consegue visualizar sua constância, identificar hábitos que estão sendo cumpridos com maior frequência e observar sua evolução pessoal.

Entre os hábitos que podem ser acompanhados no sistema, destacam-se exemplos como:
•	ingestão de água;
•	prática de atividade física;
•	horas de sono;
•	alimentação saudável;
•	leitura;
•	meditação;
•	redução do tempo de tela, entre outros.

Dessa forma, o sistema funciona como uma ferramenta de apoio ao autocuidado, ao planejamento pessoal e à manutenção de rotinas mais equilibradas.

3. Público-Alvo
O sistema é destinado a qualquer pessoa que deseje monitorar hábitos saudáveis de forma simples, organizada e acessível. Seu uso pode beneficiar:
•	estudantes que desejam melhorar sua rotina;
•	pessoas que estão tentando criar novos hábitos;
•	usuários que desejam acompanhar metas de saúde e bem-estar;
•	indivíduos que procuram maior disciplina e constância em atividades diárias.

4. Equipe de Desenvolvimento
Nome	GitHub	Responsabilidade
Ana Luísa Oliveira Braga	@Luisa12-dev	Líder técnica — banco de dados, menu principal, relatórios e integração
Gabriel Santos	@GabrielSilvaSantos	CRUD de hábitos
Jafia Alves Melo	@JafiaAlvesMelo	CRUD de usuários CRUD de registros diários

5. Funcionalidades do Sistema
O sistema foi dividido em quatro grandes áreas funcionais: usuários, hábitos, registros diários e relatórios.

5.1. Gerenciamento de Usuários
Módulo desenvolvido por Jáfia Alves. Permite realizar o cadastro e a manutenção dos dados das pessoas que utilizarão o sistema. As funcionalidades implementadas são:
•	cadastrar usuário;
•	listar usuários cadastrados;
•	editar nome e e-mail de um usuário;
•	excluir usuário do sistema.

Durante o cadastro, o sistema realiza validações básicas, como:
•	impedir nome vazio;
•	verificar se o e-mail contém o caractere "@".

Além disso, a exclusão de um usuário exige confirmação antes de ser concluída.

5.2. Gerenciamento de Hábitos
Módulo desenvolvido por Gabriel Santos. Permite que cada usuário cadastre e administre seus próprios hábitos saudáveis. Para cada hábito, são armazenadas informações como:
•	usuário ao qual o hábito pertence;
•	nome do hábito;
•	descrição;
•	frequência;
•	meta de realização.

As operações disponíveis são:
•	cadastrar hábito;
•	listar hábitos de um usuário;
•	editar hábito;
•	excluir hábito.

No cadastro, o sistema permite escolher a frequência do hábito entre três opções: Diária, Semanal ou Mensal. Essa estrutura torna o sistema flexível para diferentes tipos de rotina e objetivos.

5.3. Registros Diários de Hábitos
Módulo desenvolvido por Jafia Alves Melo. Responsável por armazenar as informações sobre a realização dos hábitos ao longo do tempo. Cada registro contém:
•	ID do usuário;
•	ID do hábito;
•	data da prática;
•	status do hábito no dia;
•	observações complementares.

As funcionalidades disponíveis nesse módulo são:
•	criar um novo registro;
•	listar todos os registros;
•	consultar um registro específico;
•	atualizar um registro;
•	excluir um registro.

Na criação de registros, o sistema realiza validações importantes:
•	verifica se o ID do usuário informado existe;
•	confirma se o nome digitado corresponde ao usuário cadastrado naquele ID;
•	verifica se o hábito informado pertence ao usuário selecionado.

5.4. Relatórios de Acompanhamento
Módulo desenvolvido por Ana Luísa Oliveira Braga. Permite acompanhar o desempenho do usuário em relação aos seus hábitos cadastrados. O sistema disponibiliza três tipos de relatório no terminal e um relatório visual completo em HTML:

Relatório Geral por Usuário
•	nome de cada hábito;
•	quantidade total de registros realizados;
•	quantidade de vezes em que o hábito foi concluído;
•	taxa de progresso por hábito;
•	índice geral de autocuidado do usuário.

Evolução dos Últimos 7 Dias
•	lista os registros dos últimos 7 dias do usuário;
•	exibe ícone visual (OK/X) indicando se cada hábito foi cumprido ou não.

Ranking de Hábitos
•	lista os hábitos do usuário ordenados do mais cumprido para o menos cumprido;
•	exibe a taxa de sucesso de cada hábito.

Relatório Completo em HTML (funcionalidade extra)
•	gera automaticamente um arquivo relatorio.html com os três relatórios acima reunidos;
•	abre o relatório no navegador padrão do usuário automaticamente;
•	exibe badges coloridos: verde (taxa >= 70%), laranja (taxa >= 40%) e vermelho (abaixo de 40%);
•	funcionalidade desenvolvida por iniciativa própria da líder técnica, não prevista nos requisitos originais.

6. Requisitos Funcionais
Código	Descrição
RF01	Permitir o cadastro de usuários.
RF02	Permitir a listagem de usuários cadastrados.
RF03	Permitir a edição de dados de usuários.
RF04	Permitir a exclusão de usuários.
RF05	Permitir o cadastro de hábitos vinculados a um usuário.
RF06	Permitir a listagem de hábitos por usuário.
RF07	Permitir a edição de hábitos.
RF08	Permitir a exclusão de hábitos.
RF09	Permitir o registro diário da realização de hábitos.
RF10	Permitir a consulta de todos os registros cadastrados.
RF11	Permitir a consulta de um registro específico.
RF12	Permitir a atualização de registros.
RF13	Permitir a exclusão de registros.
RF14	Gerar relatório geral por usuário com taxa de progresso por hábito.
RF15	Calcular um índice geral de autocuidado com base nos registros do usuário.
RF16	Exibir evolução dos últimos 7 dias por usuário.
RF17	Gerar ranking de hábitos mais cumpridos por usuário.
RF18	Gerar relatório completo em HTML aberto automaticamente no navegador.

7. Requisitos Não Funcionais
•	O sistema deve ser executado em Python 3.8 ou superior.
•	O armazenamento dos dados deve ser feito em SQLite.
•	O sistema deve funcionar em modo texto/terminal, sem necessidade de interface gráfica.
•	O banco de dados deve ser criado automaticamente na primeira execução.
•	O código deve ser organizado em módulos separados por responsabilidade.
•	O sistema deve utilizar apenas bibliotecas nativas do Python, sem dependência de pacotes externos.
•	A interação com o usuário deve ocorrer por meio de menus simples e objetivos.

8. Regras de Negócio
•	Cada hábito deve estar obrigatoriamente vinculado a um usuário.
•	Um registro diário deve estar vinculado a um usuário e a um hábito.
•	O hábito registrado deve pertencer ao usuário informado.
•	O cadastro de usuários exige nome e e-mail válidos.
•	O e-mail do usuário não pode ser duplicado no banco de dados.
•	A frequência do hábito deve ser definida no momento do cadastro.
•	Exclusões de usuários e hábitos dependem de confirmação do operador.

9. Estrutura do Banco de Dados
O sistema utiliza o banco de dados SQLite, por meio do arquivo habitos.db, criado automaticamente na primeira execução.

9.1. Tabela usuarios
Campo	Descrição
id	Identificador único do usuário (gerado automaticamente)
nome	Nome completo do usuário
email	E-mail do usuário (único no sistema)
data_cadastro	Data em que o usuário foi cadastrado

9.2. Tabela habitos
Campo	Descrição
id	Identificador único do hábito
id_usuario	Chave estrangeira que identifica o dono do hábito
nome	Nome do hábito
descricao	Descrição do hábito (opcional)
frequencia	Frequência do hábito: Diária, Semanal ou Mensal
meta	Meta de realização definida para o hábito

9.3. Tabela registros
Campo	Descrição
id	Identificador único do registro
id_usuario	Usuário responsável pelo registro
id_habito	Hábito relacionado ao registro
data	Data do registro
status	Situação do hábito naquele dia
observacao	Observações complementares (opcional)

10. Estrutura do Projeto
O projeto foi organizado em módulos para facilitar a manutenção, a leitura e a divisão de responsabilidades entre os integrantes da equipe.

Arquivo	Responsabilidade
main.py	Menu principal e ponto de entrada do sistema
banco.py	Conexão com o banco e criação das tabelas
usuarios.py	CRUD de usuários
habitos.py	CRUD de hábitos
registros_diarios.py	CRUD de registros diários
relatorio.py	Geração de relatórios no terminal e em HTML
habitos.db	Banco de dados SQLite (gerado automaticamente)
relatorio.html	Relatório visual gerado ao usar a opção HTML

11. Fluxo de Funcionamento do Sistema
O sistema é executado pelo arquivo main.py. Ao iniciar, o programa cria o banco de dados, caso ele ainda não exista, e exibe um menu principal com as opções de navegação. A partir desse menu, o usuário pode:
1.	acessar o módulo de usuários;
2.	acessar o módulo de hábitos;
3.	acessar o módulo de registros diários;
4.	gerar relatórios;
5.	encerrar a aplicação.

O fluxo geral esperado de uso do sistema é:
6.	cadastrar um usuário;
7.	cadastrar hábitos vinculados a esse usuário;
8.	registrar diariamente o cumprimento ou não desses hábitos;
9.	gerar relatórios para acompanhar o desempenho.

12. Tecnologias Utilizadas
Tecnologia	Uso no projeto
Python 3.8+	Linguagem principal do sistema
SQLite (sqlite3)	Banco de dados relacional — armazenamento persistente
os	Manipulação de caminhos do arquivo do banco de dados
datetime	Geração automática da data de cadastro dos usuários
sys	Configuração do caminho de importação dos módulos
webbrowser	Abertura automática do relatório HTML no navegador
HTML + CSS	Geração do relatório visual (funcionalidade extra)
Git + GitHub	Controle de versão e hospedagem do repositório

13. Contribuição para o ODS 3 — Saúde e Bem-Estar
O projeto está relacionado ao Objetivo de Desenvolvimento Sustentável 3 (ODS 3), que busca assegurar uma vida saudável e promover o bem-estar para todos, em todas as idades.

Ao permitir o acompanhamento de hábitos como sono, hidratação, alimentação e atividade física, o sistema incentiva o autocuidado e a adoção de práticas saudáveis no cotidiano. O módulo de relatórios, que inclui a visualização em HTML com gráficos de taxa de sucesso, transforma dados de registros diários em informações visuais que ajudam o usuário a entender seu progresso e manter a motivação.

14. Possíveis Melhorias Futuras
•	Impedir registros duplicados do mesmo hábito no mesmo dia;
•	Padronizar os valores permitidos para o campo status;
•	Validar datas digitadas pelo usuário;
•	Melhorar o tratamento de erros e mensagens exibidas;
•	Criar gráficos de desempenho por hábito;
•	Incluir autenticação de usuários com senha;
•	Desenvolver uma interface gráfica ou aplicação web completa.

15. Considerações Finais
O Sistema de Acompanhamento de Hábitos Saudáveis permitiu aplicar, na prática, conhecimentos fundamentais de programação, como modularização, manipulação de banco de dados, uso de funções, validação de entradas e desenvolvimento de operações de CRUD.

Além do aspecto técnico, o projeto também se destaca por abordar uma temática relevante e atual: a construção de hábitos saudáveis e o incentivo ao autocuidado. Dessa forma, a aplicação cumpre um papel duplo: serve como exercício acadêmico de programação e, ao mesmo tempo, propõe uma solução útil para o acompanhamento de rotinas de saúde e bem-estar.














#  Sistema de Acompanhamento de Hábitos Saudáveis 
## Documentação do Projeto 
[cite_start]**Programação 1 · UPE · Profª Aeda** [cite: 3]

---

## [cite_start]1. Apresentação do Projeto [cite: 4]
[cite_start]O **Sistema de Acompanhamento de Hábitos Saudáveis** é uma aplicação desenvolvida em Python com persistência de dados em SQLite, criada com o objetivo de auxiliar usuários no monitoramento de hábitos relacionados à saúde e ao bem-estar[cite: 5]. 

[cite_start]A proposta do sistema é permitir que cada usuário cadastre seus hábitos, registre diariamente sua realização e acompanhe seu progresso por meio de relatórios[cite: 6]. [cite_start]O projeto foi desenvolvido no contexto da disciplina de Programação, com foco na aplicação prática de conceitos como modularização, persistência em banco de dados, operações de CRUD e organização de sistemas em camadas funcionais[cite: 7]. 

[cite_start]Além disso, o sistema está alinhado ao **ODS 3 — Saúde e Bem-Estar**, pois incentiva a construção de rotinas mais saudáveis e o acompanhamento contínuo de práticas positivas no dia a dia[cite: 8].

---

## [cite_start]2. Objetivo do Sistema [cite: 9]
[cite_start]O objetivo do sistema é oferecer uma forma simples e organizada de registrar hábitos saudáveis e acompanhar sua execução ao longo do tempo[cite: 10]. [cite_start]Com isso, o usuário consegue visualizar sua constância, identificar hábitos que estão sendo cumpridos com maior frequência e observar sua evolução pessoal[cite: 11].

[cite_start]Entre os hábitos que podem ser acompanhados no sistema, destacam-se exemplos como[cite: 12]:
* [cite_start]💧 Ingestão de água; [cite: 13]
* [cite_start]🏃 Prática de atividade física; [cite: 14]
* [cite_start]🛌 Horas de sono; [cite: 15]
* [cite_start]🍏 Alimentação saudável; [cite: 16]
* [cite_start]📚 Leitura; [cite: 17]
* [cite_start]🧘 Meditação; [cite: 18]
* [cite_start]📱 Redução do tempo de tela, entre outros[cite: 19].

[cite_start]Dessa forma, o sistema funciona como uma ferramenta de apoio ao autocuidado, ao planejamento pessoal e à manutenção de rotinas mais equilibradas[cite: 20].

---

## [cite_start]3. Público-Alvo [cite: 21]
[cite_start]O sistema é destinado a qualquer pessoa que deseje monitorar hábitos saudáveis de forma simples, organizada e acessível[cite: 22]. [cite_start]Seu uso pode beneficiar[cite: 23]:
* [cite_start]Estudantes que desejam melhorar sua rotina; [cite: 24]
* [cite_start]Pessoas que estão tentando criar novos hábitos; [cite: 25]
* [cite_start]Usuários que desejam acompanhar metas de saúde e bem-estar; [cite: 26]
* [cite_start]Indivíduos que procuram maior disciplina e constância em atividades diárias[cite: 27].

---

## [cite_start]4. Equipe de Desenvolvimento [cite: 28]

| Nome | GitHub | Responsabilidade |
| :--- | :--- | :--- |
| **Ana Luísa Oliveira Braga** | @Luisa12-dev | Líder técnica — banco de dados, menu principal, relatórios e integração |
| **Gabriel Santos** | @GabrielSilvaSantos | CRUD de usuários e CRUD hábitos |
| **Jafia Alves Melo** | @JafiaAlvesMelo |  CRUD de registros diários |

[cite_start][cite: 29]

---

## [cite_start]5. Funcionalidades do Sistema [cite: 30]
[cite_start]O sistema foi dividido em quatro grandes áreas funcionais: usuários, hábitos, registros diários e relatórios[cite: 31].

### 5.1. [cite_start]Gerenciamento de Usuários [cite: 32]
Módulo desenvolvido por **Gabriel Santos**. [cite_start]Permite realizar o cadastro e a manutenção dos dados das pessoas que utilizarão o sistema[cite: 33]. [cite_start]As funcionalidades implementadas são[cite: 34]:
* [cite_start]Cadastrar usuário; [cite: 35]
* [cite_start]Listar usuários cadastrados; [cite: 36]
* [cite_start]Editar nome e e-mail de um usuário; [cite: 37]
* [cite_start]Excluir usuário do sistema[cite: 38].

[cite_start]Durante o cadastro, o sistema realiza validações básicas, como[cite: 39]:
* [cite_start]Impedir nome vazio; [cite: 40]
* [cite_start]Verificar se o e-mail contém o caractere `@`[cite: 41].

[cite_start]Além disso, a exclusão de um usuário exige confirmação antes de ser concluída[cite: 42].

### 5.2. [cite_start]Gerenciamento de Hábitos [cite: 43]
Módulo desenvolvido por **Gabriel Santos**. [cite_start]Permite que cada usuário cadastre e administre seus próprios hábitos saudáveis[cite: 44]. [cite_start]Para cada hábito, são armazenadas informações como[cite: 45]:
* [cite_start]Usuário ao qual o hábito pertence; [cite: 46]
* [cite_start]Nome do hábito; [cite: 47]
* [cite_start]Descrição; [cite: 48]
* [cite_start]Frequência; [cite: 49]
* [cite_start]Meta de realização[cite: 50].

[cite_start]As operações disponíveis são[cite: 51]:
* [cite_start]Cadastrar hábito; [cite: 52]
* [cite_start]Listar hábitos de um usuário; [cite: 53]
* [cite_start]Editar hábito; [cite: 54]
* [cite_start]Excluir hábito[cite: 55].

[cite_start]No cadastro, o sistema permite escolher a frequência do hábito entre três opções: **Diária**, **Semanal** ou **Mensal**[cite: 56]. [cite_start]Essa estrutura torna o sistema flexível para diferentes tipos de rotina e objetivos[cite: 57].

### 5.3. [cite_start]Registros Diários de Hábitos [cite: 58]
Módulo desenvolvido por **Jafia Alves Melo**. [cite_start]Responsável por armazenar as informações sobre a realização dos hábitos ao longo do tempo[cite: 59]. [cite_start]Cada registro contém[cite: 60]:
* [cite_start]ID do usuário; [cite: 61]
* [cite_start]ID do hábito; [cite: 62]
* [cite_start]Data da prática; [cite: 63]
* [cite_start]Status do hábito no dia; [cite: 64]
* [cite_start]Observações complementares[cite: 65].

[cite_start]As funcionalidades disponíveis nesse módulo são[cite: 66]:
* [cite_start]Criar um novo registro; [cite: 67]
* [cite_start]Listar todos os registros; [cite: 68]
* [cite_start]Consultar um registro específico; [cite: 69]
* [cite_start]Atualizar um registro; [cite: 70]
* [cite_start]Excluir um registro[cite: 71].

[cite_start]Na criação de registros, o sistema realiza validações importantes[cite: 72]:
* [cite_start]Verifica se o ID do usuário informado existe; [cite: 73]
* [cite_start]Confirma se o nome digitado corresponde ao usuário cadastrado naquele ID; [cite: 74]
* [cite_start]Verifica se o hábito informado pertence ao usuário selecionado[cite: 75].

### 5.4. [cite_start]Relatórios de Acompanhamento [cite: 76]
Módulo desenvolvido por **Ana Luísa Oliveira Braga**. [cite_start]Permite acompanhar o desempenho do usuário em relação aos seus hábitos cadastrados[cite: 77]. [cite_start]O sistema disponibiliza três tipos de relatório no terminal e um relatório visual completo em HTML[cite: 78]:

#### [cite_start]Relatório Geral por Usuário [cite: 79]
* [cite_start]Nome de cada hábito; [cite: 80]
* [cite_start]Quantidade total de registros realizados; [cite: 81]
* [cite_start]Quantidade de vezes em que o hábito foi concluído; [cite: 82]
* [cite_start]Taxa de progresso por hábito; [cite: 83]
* [cite_start]Índice geral de autocuidado do usuário[cite: 84].

#### [cite_start]Evolução dos Últimos 7 Dias [cite: 85]
* [cite_start]Lista os registros dos últimos 7 dias do usuário; [cite: 86]
* [cite_start]Exibe ícone visual (`OK`/`X`) indicando se cada hábito foi cumprido ou não[cite: 87].

#### [cite_start]Ranking de Hábitos [cite: 88]
* [cite_start]Lista os hábitos do usuário ordenados do mais cumprido para o menos cumprido; [cite: 89]
* [cite_start]Exibe a taxa de sucesso de cada hábito[cite: 90].

#### [cite_start]Relatório Completo em HTML (funcionalidade extra) [cite: 91]
* [cite_start]Gera automaticamente um arquivo `relatorio.html` com os três relatórios acima reunidos; [cite: 92]
* [cite_start]Abre o relatório no navegador padrão do usuário automaticamente; [cite: 93]
* [cite_start]Exibe badges coloridos: verde (taxa $\ge$ 70%), laranja (taxa $\ge$ 40%) e vermelho (abaixo de 40%)[cite: 94];
* [cite_start]Funcionalidade desenvolvida por iniciativa própria da líder técnica, não prevista nos requisitos originais[cite: 95].

---

## [cite_start]6. Requisitos Funcionais [cite: 96]

| Código | Descrição |
| :--- | :--- |
| **RF01** | Permitir o cadastro de usuários. |
| **RF02** | Permitir a listagem de usuários cadastrados. |
| **RF03** | Permitir a edição de dados de usuários. |
| **RF04** | Permitir a exclusão de usuários. |
| **RF05** | Permitir o cadastro de hábitos vinculados a um usuário. |
| **RF06** | Permitir a listagem de hábitos por usuário. |
| **RF07** | Permitir a edição de hábitos. |
| **RF08** | Permitir a exclusão de hábitos. |
| **RF09** | Permitir o registro diário da realização de hábitos. |
| **RF10** | Permitir a consulta de todos os registros cadastrados. |
| **RF11** | Permitir a consulta de um registro específico. |
| **RF12** | Permitir a atualização de registros. |
| **RF13** | Permitir a exclusão de registros. |
| **RF14** | Gerar relatório geral por usuário com taxa de progresso por hábito. |
| **RF15** | Calcular um índice geral de autocuidado com base nos registros do usuário. |
| **RF16** | Exibir evolução dos últimos 7 dias por usuário. |
| **RF17** | Gerar ranking de hábitos mais cumpridos por usuário. |
| **RF18** | Gerar relatório completo em HTML aberto automaticamente no navegador. |

[cite_start][cite: 97]

---

## [cite_start]7. Requisitos Não Funcionais [cite: 98]
* [cite_start]O sistema deve ser executado em Python 3.8 ou superior[cite: 99].
* [cite_start]O armazenamento dos dados deve ser feito em SQLite[cite: 100].
* [cite_start]O sistema deve funcionar em modo texto/terminal, sem necessidade de interface gráfica[cite: 101].
* [cite_start]O banco de dados deve ser criado automaticamente na primeira execução[cite: 102].
* [cite_start]O código deve ser organizado em módulos separados por responsabilidade[cite: 103].
* [cite_start]O sistema deve utilizar apenas bibliotecas nativas do Python, sem dependência de pacotes externos[cite: 104].
* [cite_start]A interação com o usuário deve ocorrer por meio de menus simples e objetivos[cite: 105].

---

## [cite_start]8. Regras de Negócio [cite: 106]
* [cite_start]Cada hábito deve estar obrigatoriamente vinculado a um usuário[cite: 107].
* [cite_start]Um registro diário deve estar vinculado a um usuário e a um hábito[cite: 108].
* [cite_start]O hábito registrado deve pertencer ao usuário informado[cite: 109].
* [cite_start]O cadastro de usuários exige nome e e-mail válidos[cite: 110].
* [cite_start]O e-mail do usuário não pode ser duplicado no banco de dados[cite: 111].
* [cite_start]A frequência do hábito deve ser definida no momento do cadastro[cite: 112].
* [cite_start]Exclusões de usuários e hábitos dependem de confirmação do operador[cite: 113].

---

## [cite_start]9. Estrutura do Banco de Dados [cite: 114]
[cite_start]O sistema utiliza o banco de dados SQLite, por meio do arquivo `habitos.db`, criado automaticamente na primeira execução[cite: 115].

### 9.1. [cite_start]Tabela `usuarios` [cite: 116]

| Campo | Descrição |
| :--- | :--- |
| **id** | Identificador único do usuário (gerado automaticamente) |
| **nome** | Nome completo do usuário |
| **email** | E-mail do usuário (único no sistema) |
| **data_cadastro** | Data em que o usuário foi cadastrado |

[cite_start][cite: 117]

### 9.2. [cite_start]Tabela `habitos` [cite: 118]

| Campo | Descrição |
| :--- | :--- |
| **id** | Identificador único do hábito |
| **id_usuario** | Chave estrangeira que identifica o dono do hábito |
| **nome** | Nome do hábito |
| **descricao** | Descrição do hábito (opcional) |
| **frequencia** | Frequência do hábito: Diária, Semanal ou Mensal |
| **meta** | Meta de realização definida para o hábito |

[cite_start][cite: 119]

### 9.3. [cite_start]Tabela `registros` [cite: 120]

| Campo | Descrição |
| :--- | :--- |
| **id** | Identificador único do registro |
| **id_usuario** | Usuário responsável pelo registro |
| **id_habito** | Hábito relacionado ao registro |
| **data** | Data do registro |
| **status** | Situação do hábito naquele dia |
| **observacao** | Observações complementares (opcional) |

[cite_start][cite: 121]

---

## [cite_start]10. Estrutura do Projeto [cite: 122]
[cite_start]O projeto foi organizado em módulos para facilitar a manutenção, a leitura e a divisão de responsabilidades entre os integrantes da equipe[cite: 123].

| Arquivo | Responsabilidade |
| :--- | :--- |
| **`main.py`** | Menu principal e ponto de entrada do sistema |
| **`banco.py`** | Conexão com o banco e criação das tabelas |
| **`usuarios.py`** | CRUD de usuários |
| **`habitos.py`** | CRUD de hábitos |
| **`registros_diarios.py`** | CRUD de registros diários |
| **`relatorio.py`** | Geração de relatórios no terminal e em HTML |
| *`habitos.db`* | Banco de dados SQLite (gerado automaticamente) |
| *`relatorio.html`* | Relatório visual gerado ao usar a opção HTML |

[cite_start][cite: 124]

---

## [cite_start]11. Fluxo de Funcionamento do Sistema [cite: 125]
[cite_start]O sistema é executado pelo arquivo `main.py`[cite: 126]. [cite_start]Ao iniciar, o programa cria o banco de dados, caso ele ainda não exista, e exibe um menu principal com as opções de navegação[cite: 126]. [cite_start]A partir desse menu, o usuário pode[cite: 127]:
1. [cite_start]Acessar o módulo de usuários; [cite: 128]
2. [cite_start]Acessar o módulo de hábitos; [cite: 129]
3. [cite_start]Acessar o módulo de registros diários; [cite: 130]
4. [cite_start]Gerar relatórios; [cite: 131]
5. [cite_start]Encerrar a aplicação[cite: 132].

[cite_start]O fluxo geral esperado de uso do sistema é[cite: 133]:
* Cadastrar um usuário; [cite: 134]
* [cite_start]Cadastrar hábitos vinculados a esse usuário; [cite: 135]
* [cite_start]Registrar diariamente o cumprimento ou não desses hábitos; [cite: 136]
* Gerar relatórios para acompanhar o desempenho[cite: 137].

---

## 12. Tecnologias Utilizadas [cite: 138]

| Tecnologia | Uso no projeto |
| :--- | :--- |
| **Python 3.8+** | Linguagem principal do sistema |
| **SQLite (sqlite3)** | Banco de dados relacional — armazenamento persistente |
| **os** | Manipulação de caminhos do arquivo do banco de dados |
| **datetime** | Geração automática da data de cadastro dos usuários |
| **sys** | Configuração do caminho de importação dos módulos |
| **webbrowser** | Abertura automática do relatório HTML no navegador |
| **HTML + CSS** | Geração do relatório visual (funcionalidade extra) |
| **Git + GitHub** | Controle de versão e hospedagem do repositório |

[cite_start][cite: 139]

---

## 13. Contribuição para o ODS 3 — Saúde e Bem-Estar [cite: 140]
O projeto está relacionado ao **Objetivo de Desenvolvimento Sustentável 3 (ODS 3)**, que busca assegurar uma vida saudável e promover o bem-estar para todos, em todas as idades[cite: 141].

Ao permitir o acompanhamento de hábitos como sono, hidratação, alimentação e atividade física, o sistema incentiva o autocuidado e a adoção de práticas saudáveis no cotidiano[cite: 142]. O módulo de relatórios, que inclui a visualização em HTML com gráficos de taxa de sucesso, transforma dados de registros diários em informações visuais que ajudam o usuário a entender seu progresso e manter a motivação[cite: 143].

---

## 14. Possíveis Melhorias Futuras [cite: 144]
* [cite_start]Impedir registros duplicados do mesmo hábito no mesmo dia; [cite: 145]
* [cite_start]Padronizar os valores permitidos para o campo status; [cite: 146]
* Validar datas digitadas pelo usuário; [cite: 147]
* [cite_start]Melhorar o tratamento de erros e mensagens exibidas; [cite: 148]
* [cite_start]Criar gráficos de desempenho por hábito; [cite: 149]
* Incluir autenticação de usuários com senha; [cite: 150]
* [cite_start]Desenvolver uma interface gráfica ou aplicação web completa[cite: 151].

---

## [cite_start]15. Considerações Finais [cite: 152]
[cite_start]O **Sistema de Acompanhamento de Hábitos Saudáveis** permitiu aplicar, na prática, conhecimentos fundamentais de programação, como modularização, manipulação de banco de dados, uso de funções, validação de entradas e desenvolvimento de operações de CRUD[cite: 153].

[cite_start]Além do aspecto técnico, o projeto também se destaca por abordar uma temática relevante e atual: a construção de hábitos saudáveis e o incentivo ao autocuidado[cite: 154]. [cite_start]Dessa forma, a aplicação cumpre um papel duplo: serve como exercício acadêmico de programação e, ao mesmo tempo, propõe uma solução útil para o acompanhamento de rotinas de saúde e bem-estar[cite: 155].j