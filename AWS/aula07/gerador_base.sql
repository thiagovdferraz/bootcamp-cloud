-- Criação da tabela de vendas
DROP TABLE IF EXISTS vendas;

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(50),
    produto VARCHAR(50),
    quantidade INT,
    valor_unitario DECIMAL(10,2),
    data_venda DATE
);

-- Procedimento para inserir dados aleatórios
DELIMITER $$
CREATE PROCEDURE GerarDadosVendas()
BEGIN
    DECLARE contador INT DEFAULT 0;
    
    WHILE contador < 100 DO
        INSERT INTO vendas (
            cliente,
            produto,
            quantidade,
            valor_unitario,
            data_venda
        ) VALUES (
            CONCAT('Cliente ', FLOOR(1 + RAND() * 10)), -- 10 clientes diferentes
            CONCAT('Produto ', FLOOR(1 + RAND() * 15)),  -- 15 produtos diferentes
            FLOOR(1 + RAND() * 20),                     -- Quantidade entre 1 e 20
            ROUND(10 + RAND() * 500, 2),                -- Preços entre 10.00 e 510.00
            DATE_ADD('2023-01-01', INTERVAL FLOOR(RAND() * 365) DAY) -- Datas em 2023
        );
        SET contador = contador + 1;
    END WHILE;
END$$
DELIMITER ;

-- Executar o procedimento
CALL GerarDadosVendas();

-- Remover o procedimento (opcional)
DROP PROCEDURE GerarDadosVendas;