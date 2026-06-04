USE db_dogtor;

INSERT INTO login (
    fk_funcionario,
    senha,
    fk_cpf,
    fk_cargo
)

VALUES (
    NULL,
    'Lune@2',
    '12345678900',
    NULL
)

INSERT INTO login (
    fk_funcionario,
    senha,
    fk_cpf,
    fk_cargo
)

VALUES (
    1,
    'Igor@1',
    NULL,
    '1'
)

-- Trocado NONE para NULL, pois MYSQL não permite o NONE
-- Correção de syntax, foi esquecido algumas virgulas e pontos virgulas para encerrar comando (tomar mais cuidado)
-- a fk cargo recebe número int, então deve ser add a pk do cargo e não 'veterinário'. O que você tinha colocado antes
