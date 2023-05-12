CREATE TABLE base_info (
    ID_CLIENTE BIGINT,
    SAFRA_REF VARCHAR(10),
    RENDA_MES_ANTERIOR DECIMAL(10, 1),
    NO_FUNCIONARIOS DECIMAL(10, 1),
    PRIMARY KEY (ID_CLIENTE, SAFRA_REF)
);

CREATE TABLE base_pagamentos_desenvolvimento (
    ID_CLIENTE BIGINT,
    SAFRA_REF VARCHAR(10),
    DATA_EMISSAO_DOCUMENTO DATE,
    DATA_PAGAMENTO DATE,
    DATA_VENCIMENTO DATE,
    VALOR_A_PAGAR DECIMAL(10, 2),
    TAXA DECIMAL(10, 2),
    FOREIGN KEY (ID_CLIENTE, SAFRA_REF) REFERENCES base_info (ID_CLIENTE, SAFRA_REF)
);

CREATE TABLE base_cadastral (
    ID_CLIENTE BIGINT PRIMARY KEY,
    DATA_CADASTRO DATE,
    DDD VARCHAR(3),
    FLAG_PF CHAR(1),
    SEGMENTO_INDUSTRIAL VARCHAR(50),
    DOMINIO_EMAIL VARCHAR(50),
    PORTE VARCHAR(20),
    CEP_2_DIG VARCHAR(2)
);

ALTER TABLE IF EXISTS base_info
  OWNER TO postgres;
ALTER TABLE IF EXISTS base_pagamentos_desenvolvimento
  OWNER TO postgres;
ALTER TABLE IF EXISTS base_cadastral
  OWNER TO postgres;

\copy base_info FROM 'var/lib/postgresql/data/pgadata/base_info.csv' DELIMITER ',' CSV HEADER;
\copy base_pagamentos_desenvolvimento FROM 'var/lib/postgresql/data/pgadata/base_pagamentos_desenvolvimento_clean.csv' DELIMITER ',' CSV HEADER;
\copy base_cadastral FROM 'var/lib/postgresql/data/pgadata/base_cadastral.csv' DELIMITER ',' CSV HEADER;

