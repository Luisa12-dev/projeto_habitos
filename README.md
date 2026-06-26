#  Sistema de Acompanhamento de Hábitos Saudáveis 
## Documentação do Projeto 
**Programação 1 · UPE · Profª Aeda** 

---

## 1. Apresentação do Projeto 
O **Sistema de Acompanhamento de Hábitos Saudáveis** é uma aplicação desenvolvida em Python com persistência de dados em SQLite, criada com o objetivo de auxiliar usuários no monitoramento de hábitos relacionados à saúde e ao bem-estar. 

A proposta do sistema é permitir que cada usuário cadastre seus hábitos, registre diariamente sua realização e acompanhe seu progresso por meio de relatórios. O projeto foi desenvolvido no contexto da disciplina de Programação, com foco na aplicação prática de conceitos como modularização, persistência em banco de dados, operações de CRUD e organização de sistemas em camadas funcionais. 

Além disso, o sistema está alinhado ao **ODS 3 — Saúde e Bem-Estar**, pois incentiva a construção de rotinas mais saudáveis e o acompanhamento contínuo de práticas positivas no dia a dia.

---

## 2. Objetivo do Sistema 
O objetivo do sistema é oferecer uma forma simples e organizada de registrar hábitos saudáveis e acompanhar sua execução ao longo do tempo. Com isso, o usuário consegue visualizar sua constância, identificar hábitos que estão sendo cumpridos com maior frequência e observar sua evolução pessoal.

Entre os hábitos que podem ser acompanhados no sistema, destacam-se exemplos como:
*  Ingestão de água; 
*  Prática de atividade física; 
*  Horas de sono; 
*  Alimentação saudável; 
*  Leitura; 
*  Meditação; 
*  Redução do tempo de tela, entre outros.

Dessa forma, o sistema funciona como uma ferramenta de apoio ao autocuidado, ao planejamento pessoal e à manutenção de rotinas mais equilibradas.

---

## 3. Público-Alvo 
O sistema é destinado a qualquer pessoa que deseje monitorar hábitos saudáveis de forma simples, organizada e acessível. Seu uso pode beneficiar:
* Estudantes que desejam melhorar sua rotina; 
* Pessoas que estão tentando criar novos hábitos; 
* Usuários que desejam acompanhar metas de saúde e bem-estar; 
* Indivíduos que procuram maior disciplina e constância em atividades diárias.

---

## 4. Equipe de Desenvolvimento 

| Nome | GitHub | Responsabilidade |
| :--- | :--- | :--- |
| **Ana Luísa Oliveira Braga** | @Luisa12-dev | Líder técnica — banco de dados, menu principal, relatórios e integração |
| **Gabriel Santos** | @GabrielSilvaSantos | CRUD de usuários e CRUD hábitos |
| **Jafia Alves Melo** | @JafiaAlvesMelo |  CRUD de registros diários, suporte durante toda a realização do projeto e conferência do funcionamento dos códigos implementados. | 
 



---

## 5. Funcionalidades do Sistema 
O sistema foi dividido em quatro grandes áreas funcionais: usuários, hábitos, registros diários e relatórios.

### 5.1. Gerenciamento de Usuários 
Módulo desenvolvido por **Gabriel Santos**. Permite realizar o cadastro e a manutenção dos dados das pessoas que utilizarão o sistema. As funcionalidades implementadas são:
* Cadastrar usuário; 
* Listar usuários cadastrados; 
* Editar nome e e-mail de um usuário; 
* Excluir usuário do sistema.

Durante o cadastro, o sistema realiza validações básicas, como:
* Impedir nome vazio; 
* Verificar se o e-mail contém o caractere `@`.

Além disso, a exclusão de um usuário exige confirmação antes de ser concluída.

### 5.2. Gerenciamento de Hábitos 
Módulo desenvolvido por **Gabriel Santos**. Permite que cada usuário cadastre e administre seus próprios hábitos saudáveis. Para cada hábito, são armazenadas informações como:
* Usuário ao qual o hábito pertence; 
* Nome do hábito; 
* Descrição; 
* Frequência; 
* Meta de realização.

As operações disponíveis são:
* Cadastrar hábito; 
* Listar hábitos de um usuário; 
* Editar hábito; 
* Excluir hábito.

No cadastro, o sistema permite escolher a frequência do hábito entre três opções: **Diária**, **Semanal** ou **Mensal**. Essa estrutura torna o sistema flexível para diferentes tipos de rotina e objetivos.

### 5.3. Registros Diários de Hábitos 
Módulo desenvolvido por **Jafia Alves Melo**. Responsável por armazenar as informações sobre a realização dos hábitos ao longo do tempo. Cada registro contém:
* ID do usuário; 
* ID do hábito; 
* Data da prática; 
* Status do hábito no dia; 
* Observações complementares.

As funcionalidades disponíveis nesse módulo são:
* Criar um novo registro; 
* Listar todos os registros; 
* Consultar um registro específico; 
* Atualizar um registro; 
* Excluir um registro.

Na criação de registros, o sistema realiza validações importantes:
* Verifica se o ID do usuário informado existe; 
* Confirma se o nome digitado corresponde ao usuário cadastrado naquele ID; 
* Verifica se o hábito informado pertence ao usuário selecionado.

### 5.4. Relatórios de Acompanhamento 
Módulo desenvolvido por **Ana Luísa Oliveira Braga**. Permite acompanhar o desempenho do usuário em relação aos seus hábitos cadastrados. O sistema disponibiliza três tipos de relatório no terminal e um relatório visual completo em HTML:

#### Relatório Geral por Usuário 
* Nome de cada hábito; 
* Quantidade total de registros realizados; 
* Quantidade de vezes em que o hábito foi concluído; 
* Taxa de progresso por hábito; 
* Índice geral de autocuidado do usuário.

#### Evolução dos Últimos 7 Dias 
* Lista os registros dos últimos 7 dias do usuário; 
* Exibe ícone visual (`OK`/`X`) indicando se cada hábito foi cumprido ou não.

#### Ranking de Hábitos 
* Lista os hábitos do usuário ordenados do mais cumprido para o menos cumprido; 
* Exibe a taxa de sucesso de cada hábito.

#### Relatório Completo em HTML (funcionalidade extra) 
* Gera automaticamente um arquivo `relatorio.html` com os três relatórios acima reunidos; 
* Abre o relatório no navegador padrão do usuário automaticamente; 
* Exibe badges coloridos: verde (taxa $\ge$ 70%), laranja (taxa $\ge$ 40%) e vermelho (abaixo de 40%);
* Funcionalidade desenvolvida por iniciativa própria da líder técnica, não prevista nos requisitos originais.

---

## 6. Requisitos Funcionais 

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



---

## 7. Requisitos Não Funcionais 
* O sistema deve ser executado em Python 3.8 ou superior.
* O armazenamento dos dados deve ser feito em SQLite.
* O sistema deve funcionar em modo texto/terminal, sem necessidade de interface gráfica.
* O banco de dados deve ser criado automaticamente na primeira execução.
* O código deve ser organizado em módulos separados por responsabilidade.
* O sistema deve utilizar apenas bibliotecas nativas do Python, sem dependência de pacotes externos.
* A interação com o usuário deve ocorrer por meio de menus simples e objetivos.

---

## 8. Regras de Negócio 
* Cada hábito deve estar obrigatoriamente vinculado a um usuário.
* Um registro diário deve estar vinculado a um usuário e a um hábito.
* O hábito registrado deve pertencer ao usuário informado.
* O cadastro de usuários exige nome e e-mail válidos.
* O e-mail do usuário não pode ser duplicado no banco de dados.
* A frequência do hábito deve ser definida no momento do cadastro.
* Exclusões de usuários e hábitos dependem de confirmação do operador.

---

## 9. Estrutura do Banco de Dados 
O sistema utiliza o banco de dados SQLite, por meio do arquivo `habitos.db`, criado automaticamente na primeira execução.

### 9.1. Tabela `usuarios` 

| Campo | Descrição |
| :--- | :--- |
| **id** | Identificador único do usuário (gerado automaticamente) |
| **nome** | Nome completo do usuário |
| **email** | E-mail do usuário (único no sistema) |
| **data_cadastro** | Data em que o usuário foi cadastrado |



### 9.2. Tabela `habitos` 

| Campo | Descrição |
| :--- | :--- |
| **id** | Identificador único do hábito |
| **id_usuario** | Chave estrangeira que identifica o dono do hábito |
| **nome** | Nome do hábito |
| **descricao** | Descrição do hábito (opcional) |
| **frequencia** | Frequência do hábito: Diária, Semanal ou Mensal |
| **meta** | Meta de realização definida para o hábito |



### 9.3. Tabela `registros` 

| Campo | Descrição |
| :--- | :--- |
| **id** | Identificador único do registro |
| **id_usuario** | Usuário responsável pelo registro |
| **id_habito** | Hábito relacionado ao registro |
| **data** | Data do registro |
| **status** | Situação do hábito naquele dia |
| **observacao** | Observações complementares (opcional) |



---

## 10. Estrutura do Projeto 
O projeto foi organizado em módulos para facilitar a manutenção, a leitura e a divisão de responsabilidades entre os integrantes da equipe.

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



---

## 11. Fluxo de Funcionamento do Sistema 
O sistema é executado pelo arquivo `main.py`. Ao iniciar, o programa cria o banco de dados, caso ele ainda não exista, e exibe um menu principal com as opções de navegação. A partir desse menu, o usuário pode:
1. Acessar o módulo de usuários; 
2. Acessar o módulo de hábitos; 
3. Acessar o módulo de registros diários; 
4. Gerar relatórios; 
5. Encerrar a aplicação.

O fluxo geral esperado de uso do sistema é:
* Cadastrar um usuário; 
* Cadastrar hábitos vinculados a esse usuário; 
* Registrar diariamente o cumprimento ou não desses hábitos; 
* Gerar relatórios para acompanhar o desempenho.

---

## 12. Tecnologias Utilizadas 

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



---

## 13. Contribuição para o ODS 3 — Saúde e Bem-Estar 
O projeto está relacionado ao **Objetivo de Desenvolvimento Sustentável 3 (ODS 3)**, que busca assegurar uma vida saudável e promover o bem-estar para todos, em todas as idades.

Ao permitir o acompanhamento de hábitos como sono, hidratação, alimentação e atividade física, o sistema incentiva o autocuidado e a adoção de práticas saudáveis no cotidiano. O módulo de relatórios, que inclui a visualização em HTML com gráficos de taxa de sucesso, transforma dados de registros diários em informações visuais que ajudam o usuário a entender seu progresso e manter a motivação.

---

## 14. Possíveis Melhorias Futuras 
* Impedir registros duplicados do mesmo hábito no mesmo dia; 
* Padronizar os valores permitidos para o campo status; 
* Validar datas digitadas pelo usuário; 
* Melhorar o tratamento de erros e mensagens exibidas; 
* Criar gráficos de desempenho por hábito; 
* Incluir autenticação de usuários com senha; 
* Desenvolver uma interface gráfica ou aplicação web completa.

---

## 15. Considerações Finais 
O **Sistema de Acompanhamento de Hábitos Saudáveis** permitiu aplicar, na prática, conhecimentos fundamentais de programação, como modularização, manipulação de banco de dados, uso de funções, validação de entradas e desenvolvimento de operações de CRUD.

Além do aspecto técnico, o projeto também se destaca por abordar uma temática relevante e atual: a construção de hábitos saudáveis e o incentivo ao autocuidado. Dessa forma, a aplicação cumpre um papel duplo: serve como exercício acadêmico de programação e, ao mesmo tempo, propõe uma solução útil para o acompanhamento de rotinas de saúde e bem-estar.
