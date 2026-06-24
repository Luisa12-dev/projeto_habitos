 Sistema de Acompanhamento de Hábitos Saudáveis

 1. Apresentação do Projeto

O **Sistema de Acompanhamento de Hábitos Saudáveis** é uma aplicação desenvolvida em Python com persistência de dados em SQLite, criada com o objetivo de auxiliar usuários no monitoramento de hábitos relacionados à saúde e ao bem-estar. A proposta do sistema é permitir que cada usuário cadastre seus hábitos, registre diariamente sua realização e acompanhe seu progresso por meio de relatórios.

O projeto foi desenvolvido no contexto da disciplina de **Programação**, com foco na aplicação prática de conceitos como **modularização**, **persistência em banco de dados**, **operações de CRUD** e **organização de sistemas em camadas funcionais**. Além disso, o sistema está alinhado ao **ODS 3 — Saúde e Bem-Estar**, pois incentiva a construção de rotinas mais saudáveis e o acompanhamento contínuo de práticas positivas no dia a dia.

## 2. Objetivo do Sistema

O objetivo do sistema é oferecer uma forma simples e organizada de registrar hábitos saudáveis e acompanhar sua execução ao longo do tempo. Com isso, o usuário consegue visualizar sua constância, identificar hábitos que estão sendo cumpridos com maior frequência e observar sua evolução pessoal.

Entre os hábitos que podem ser acompanhados no sistema, destacam-se exemplos como:

* ingestão de água;
* prática de atividade física;
* horas de sono;
* alimentação saudável;
* leitura;
* meditação;
* redução do tempo de tela, entre outros.

Dessa forma, o sistema funciona como uma ferramenta de apoio ao autocuidado, ao planejamento pessoal e à manutenção de rotinas mais equilibradas.

---

## 3. Público-Alvo

O sistema é destinado a qualquer pessoa que deseje monitorar hábitos saudáveis de forma simples, organizada e acessível. Seu uso pode beneficiar:

* estudantes que desejam melhorar sua rotina;
* pessoas que estão tentando criar novos hábitos;
* usuários que desejam acompanhar metas de saúde e bem-estar;
* indivíduos que procuram maior disciplina e constância em atividades diárias.

---

## 4. Equipe de Desenvolvimento

| Nome               | GitHub       | Responsabilidade                                           |
| ------------------ | ------------ | ---------------------------------------------------------- |
| Ana Luísa          | @Luisa12-dev | Líder técnica, banco de dados, menu principal e relatórios |
| (Nome da Pessoa 2) | @usuario     | CRUD de usuários e CRUD de hábitos                         |
| (Nome da Pessoa 3) | @usuario     | CRUD de registros diários                                  |

---

## 5. Funcionalidades do Sistema

O sistema foi dividido em quatro grandes áreas funcionais: **usuários**, **hábitos**, **registros diários** e **relatórios**.

### 5.1. Gerenciamento de Usuários

O módulo de usuários permite realizar o cadastro e a manutenção dos dados das pessoas que utilizarão o sistema. As funcionalidades implementadas são:

* cadastrar usuário;
* listar usuários cadastrados;
* editar nome e e-mail de um usuário;
* excluir usuário do sistema.

Durante o cadastro, o sistema realiza validações básicas, como:

* impedir nome vazio;
* verificar se o e-mail contém o caractere “@”.

Além disso, a exclusão de um usuário exige confirmação antes de ser concluída.

---

### 5.2. Gerenciamento de Hábitos

O módulo de hábitos permite que cada usuário cadastre e administre seus próprios hábitos saudáveis. Para cada hábito, são armazenadas informações como:

* usuário ao qual o hábito pertence;
* nome do hábito;
* descrição;
* frequência;
* meta de realização.

As operações disponíveis são:

* cadastrar hábito;
* listar hábitos de um usuário;
* editar hábito;
* excluir hábito.

No cadastro, o sistema permite escolher a frequência do hábito entre três opções:

* **Diária**
* **Semanal**
* **Mensal**

Essa estrutura torna o sistema flexível para diferentes tipos de rotina e objetivos.

---

### 5.3. Registros Diários de Hábitos

O módulo de registros diários é responsável por armazenar as informações sobre a realização dos hábitos ao longo do tempo. Cada registro contém:

* ID do usuário;
* ID do hábito;
* data da prática;
* status do hábito no dia;
* observações complementares.

As funcionalidades disponíveis nesse módulo são:

* criar um novo registro;
* listar todos os registros;
* consultar um registro específico;
* atualizar um registro;
* excluir um registro.

Na criação de registros, o sistema realiza validações importantes para garantir a consistência das informações:

* verifica se o ID do usuário informado existe;
* confirma se o nome digitado corresponde ao usuário cadastrado naquele ID;
* verifica se o hábito informado pertence ao usuário selecionado.

Essas verificações evitam registros associados a usuários ou hábitos incorretos.

---

### 5.4. Relatórios de Acompanhamento

O sistema possui um módulo de relatórios que permite acompanhar o desempenho do usuário em relação aos seus hábitos cadastrados. A funcionalidade atualmente implementada gera um **relatório geral por usuário**, contendo:

* nome de cada hábito;
* quantidade total de registros realizados;
* quantidade de vezes em que o hábito foi concluído;
* taxa de progresso por hábito;
* índice geral de autocuidado do usuário.

O cálculo do relatório considera os registros associados aos hábitos do usuário e contabiliza quantas vezes o status indica conclusão da atividade. Ao final, o sistema apresenta uma mensagem interpretativa com base no percentual de progresso geral.

Além da funcionalidade já implementada, o projeto prevê como expansão futura:

* relatório de evolução dos últimos 7 dias;
* ranking de hábitos mais cumpridos;
* totais gerais do sistema;
* relatórios mais detalhados com agrupamentos por período.

---

## 6. Requisitos Funcionais

Com base nas funcionalidades implementadas, o sistema atende aos seguintes requisitos funcionais:

* **RF01** – Permitir o cadastro de usuários.
* **RF02** – Permitir a listagem de usuários cadastrados.
* **RF03** – Permitir a edição de dados de usuários.
* **RF04** – Permitir a exclusão de usuários.
* **RF05** – Permitir o cadastro de hábitos vinculados a um usuário.
* **RF06** – Permitir a listagem de hábitos por usuário.
* **RF07** – Permitir a edição de hábitos.
* **RF08** – Permitir a exclusão de hábitos.
* **RF09** – Permitir o registro diário da realização de hábitos.
* **RF10** – Permitir a consulta de todos os registros cadastrados.
* **RF11** – Permitir a consulta de um registro específico.
* **RF12** – Permitir a atualização de registros.
* **RF13** – Permitir a exclusão de registros.
* **RF14** – Gerar relatório geral por usuário com taxa de progresso por hábito.
* **RF15** – Calcular um índice geral de autocuidado com base nos registros do usuário.

---

## 7. Requisitos Não Funcionais

Além das funcionalidades, o projeto apresenta requisitos não funcionais relacionados à implementação e ao funcionamento do sistema:

* O sistema deve ser executado em **Python 3.8 ou superior**.
* O armazenamento dos dados deve ser feito em **SQLite**.
* O sistema deve funcionar em **modo texto/terminal**, sem necessidade de interface gráfica.
* O banco de dados deve ser criado automaticamente na primeira execução.
* O código deve ser organizado em módulos separados por responsabilidade.
* O sistema deve utilizar apenas bibliotecas nativas do Python, sem dependência de pacotes externos.
* A interação com o usuário deve ocorrer por meio de menus simples e objetivos.

---

## 8. Regras de Negócio

O funcionamento do sistema segue algumas regras de negócio importantes:

* cada hábito deve estar obrigatoriamente vinculado a um usuário;
* um registro diário deve estar vinculado a um usuário e a um hábito;
* o hábito registrado deve pertencer ao usuário informado;
* o cadastro de usuários exige nome e e-mail válidos;
* o e-mail do usuário não pode ser duplicado no banco de dados;
* a frequência do hábito deve ser definida no momento do cadastro;
* a meta do hábito deve ser informada numericamente;
* exclusões de usuários e hábitos dependem da escolha do operador no menu e, em alguns casos, de confirmação.

---

## 9. Estrutura do Banco de Dados

O sistema utiliza o banco de dados **SQLite**, por meio do arquivo `habitos.db`, criado automaticamente quando o sistema é executado pela primeira vez.

O banco possui três tabelas principais:

### 9.1. Tabela `usuarios`

Armazena os dados dos usuários cadastrados no sistema.

**Campos:**

* `id` – identificador do usuário;
* `nome` – nome do usuário;
* `email` – e-mail do usuário;
* `data_cadastro` – data em que o usuário foi cadastrado.

---

### 9.2. Tabela `habitos`

Armazena os hábitos cadastrados pelos usuários.

**Campos:**

* `id` – identificador do hábito;
* `id_usuario` – chave estrangeira que identifica o dono do hábito;
* `nome` – nome do hábito;
* `descricao` – descrição do hábito;
* `frequencia` – frequência do hábito (diária, semanal ou mensal);
* `meta` – quantidade-meta definida para o hábito.

---

### 9.3. Tabela `registros`

Armazena os registros diários de execução dos hábitos.

**Campos:**

* `id` – identificador do registro;
* `id_usuario` – usuário responsável pelo registro;
* `id_habito` – hábito relacionado ao registro;
* `data` – data do registro;
* `status` – situação do hábito naquele dia;
* `observacao` – observações complementares.

---

## 10. Estrutura do Projeto

O projeto foi organizado em módulos para facilitar a manutenção, a leitura e a divisão de responsabilidades entre os integrantes da equipe.

```text
projeto_habitos/
├── main.py                  # menu principal e ponto de entrada do sistema
├── banco.py                 # conexão com o banco e criação das tabelas
├── usuarios.py              # CRUD de usuários
├── habitos.py               # CRUD de hábitos
├── registros_diarios.py     # CRUD de registros diários
├── relatorio.py             # geração de relatórios
└── habitos.db               # banco de dados SQLite (gerado automaticamente)
```

### Descrição dos módulos

* **main.py**: inicializa o banco e exibe o menu principal do sistema.
* **banco.py**: centraliza a conexão com o SQLite e cria as tabelas necessárias.
* **usuarios.py**: contém as funções de cadastro, listagem, edição e exclusão de usuários.
* **habitos.py**: contém as funções de cadastro, consulta, edição e exclusão de hábitos.
* **registros_diarios.py**: controla os registros diários associados aos hábitos.
* **relatorio.py**: gera relatórios de desempenho dos usuários com base nos registros cadastrados.

---

## 11. Fluxo de Funcionamento do Sistema

O sistema é executado pelo arquivo `main.py`. Ao iniciar, o programa cria o banco de dados, caso ele ainda não exista, e exibe um menu principal com as opções de navegação.

A partir desse menu, o usuário pode:

1. acessar o módulo de usuários;
2. acessar o módulo de hábitos;
3. acessar o módulo de registros diários;
4. gerar relatórios;
5. encerrar a aplicação.

Cada módulo possui seu próprio submenu, permitindo que as operações de cadastro, consulta, edição e exclusão sejam realizadas de forma separada e organizada.

O fluxo geral esperado de uso do sistema é:

1. cadastrar um usuário;
2. cadastrar hábitos vinculados a esse usuário;
3. registrar diariamente o cumprimento ou não desses hábitos;
4. gerar relatórios para acompanhar o desempenho.

---

## 12. Tecnologias Utilizadas

O sistema foi desenvolvido utilizando:

* **Python** como linguagem principal;
* **SQLite** como banco de dados relacional leve e embarcado;
* módulo **sqlite3** para conexão com o banco;
* módulo **os** para manipulação de caminhos do arquivo do banco;
* módulo **datetime** para registro da data de cadastro dos usuários;
* módulo **sys** para apoio à organização do projeto e importação dos módulos.

A escolha dessas tecnologias foi motivada pela simplicidade de uso, pela facilidade de configuração e pela adequação ao porte do projeto acadêmico.
13. Contribuição para o ODS 3 – Saúde e Bem-Estar

O projeto está relacionado ao **Objetivo de Desenvolvimento Sustentável 3 (ODS 3)**, que busca assegurar uma vida saudável e promover o bem-estar para todos, em todas as idades.

Ao permitir o acompanhamento de hábitos como sono, hidratação, alimentação e atividade física, o sistema incentiva o autocuidado e a adoção de práticas saudáveis no cotidiano. Mesmo sendo uma aplicação simples, ela contribui para a conscientização do usuário sobre a importância da regularidade de ações que impactam diretamente sua saúde física e mental.

---

## 14. Possíveis Melhorias Futuras

Como evolução do projeto, podem ser implementadas as seguintes melhorias:

* impedir registros duplicados do mesmo hábito no mesmo dia;
* padronizar os valores permitidos para o campo `status`;
* validar datas digitadas pelo usuário;
* melhorar o tratamento de erros e mensagens exibidas;
* gerar relatórios em HTML ou PDF;
* criar gráficos de desempenho por hábito;
* incluir autenticação de usuários;
* desenvolver uma interface gráfica para tornar a experiência mais amigável.

---

## 15. Considerações Finais

O **Sistema de Acompanhamento de Hábitos Saudáveis** permitiu aplicar, na prática, conhecimentos fundamentais de programação, como modularização, manipulação de banco de dados, uso de funções, validação de entradas e desenvolvimento de operações de CRUD.

Além do aspecto técnico, o projeto também se destaca por abordar uma temática relevante e atual: a construção de hábitos saudáveis e o incentivo ao autocuidado. Dessa forma, a aplicação cumpre um papel duplo: serve como exercício acadêmico de programação e, ao mesmo tempo, propõe uma solução útil para o acompanhamento de rotinas de saúde e bem-estar.
