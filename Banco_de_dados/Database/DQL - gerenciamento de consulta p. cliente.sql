SELECT
	tb1.nome_animal,
    tb1.especie,
    tb2.dt_consulta,
    tb2.hr_consulta, 
    tb2.status,
    tb3.finalidade
FROM db_dogtor.animal tb1
INNER JOIN  db_dogtor.consulta tb2 ON 
	tb1.id_animal = tb2.fk_animal
INNER JOIN db_dogtor.tipo_consulta tb3 ON 
	tb2.fk_id_consulta = tb3.id_consulta
WHERE tb2.fk_cpf = '12345678901';