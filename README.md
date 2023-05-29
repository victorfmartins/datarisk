# README - Fraud Prediction

## Overview

This repository contains a predictive model that estimates the probability of a customer defaulting on a debt for each new credit request made by a recurring client. The model is fed with data from three different databases, each containing specific details about the clients and their respective transactions.

## Data Schemas

### Client Registration Base (base_cadastral)

```SQL
|------------------|-----------------------|-----------------|
| Field            | Type                  | Constraints     |
|------------------|-----------------------|-----------------|
| ID_CLIENTE       | INT                   | PRIMARY KEY     |
| DATA_CADASTRO    | DATE                  | NOT NULL        |
| DDD              | VARCHAR(3)            | NOT NULL        |
| FLAG_PF          | CHAR(1)               | NOT NULL        |
| SEGMENTO_INDUSTRIAL| VARCHAR(255)        | NULL            |
| DOMINIO_EMAIL    | VARCHAR(255)          | NOT NULL        |
| PORTE            | VARCHAR(255)          | NULL            |
| CEP_2_DIG        | VARCHAR(2)            | NOT NULL        |
|------------------|-----------------------|-----------------|
```

### Client Information Base (base_info)

```SQL
|------------------|-----------------------|-----------------|
| Field            | Type                  | Constraints     |
|------------------|-----------------------|-----------------|
| ID_CLIENTE       | INT                   | PRIMARY KEY,    |
|                  |                       | FOREIGN KEY     |
|                  |                       | REFERENCES      |
|                  |                       | base_cadastral(ID_CLIENTE)|
| SAFRA_REF        | DATE                  | PRIMARY KEY     |
| RENDA_MES_ANTERIOR| DECIMAL(15,2)        | NULL            |
| NO_FUNCIONARIOS  | INT                   | NULL            |
|------------------|-----------------------|-----------------|
```

### Payments Base (base_pagamentos)

```SQL
|----------------------|-----------------------|-----------------|
| Field                | Type                  | Constraints     |
|----------------------|-----------------------|-----------------|
| ID_CLIENTE           | INT                   | FOREIGN KEY     |
|                      |                       | REFERENCES      |
|                      |                       | base_info(ID_CLIENTE)|
| SAFRA_REF            | DATE                  | FOREIGN KEY     |
|                      |                       | REFERENCES      |
|                      |                       | base_info(SAFRA_REF)|
| DATA_EMISSAO_DOCUMENTO| DATE                 | NOT NULL        |
| DATA_VENCIMENTO      | DATE                  | NOT NULL        |
| VALOR_A_PAGAR        | DECIMAL(15,2)         | NOT NULL        |
| TAXA                 | DECIMAL(5,2)          | NOT NULL        |
| DATA_PAGAMENTO       | DATE                  | NULL            |
|----------------------|-----------------------|-----------------|
```

## Data Description

The model leverages data from three databases, each detailed below:

### Client Registration Base (base_cadastral.csv)

A database storing immutable registration information about the clients. Each client has a unique identifier and their data does not change over time.

### Client Information Base (base_info.csv)

This database contains dynamic information about the clients, updated monthly. Each client will appear only once per reference month. The unique identifier for each entry is the combination of the client's ID and the reference month.

### Payments Base (base_pagamentos)

Two files, 'base_pagamentos_desenvolvimento.csv' for model development and 'base_pagamentos_teste.csv' for internal validation, constitute this database. It contains transaction history for the clients, and a client may have multiple transactions over the same period.

## Objective

The model's goal is to calculate the probability of a client defaulting on a given transaction. A default is defined as a loan repayment that is late by more than five days. 

For testing, 'base_pagamentos_test.csv' is provided. The final output of the model is a table containing the fields ID_CLIENTE, SAFRA_REF, and DEFAULT, where DEFAULT is the calculated probability of client default.

## Support

If you encounter any issues, have questions, or want to offer suggestions, please contact the project author via email at victorfm185@gmail.com.
