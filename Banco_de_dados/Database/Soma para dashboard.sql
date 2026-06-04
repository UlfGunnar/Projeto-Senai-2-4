SELECT
    tb1.finalidade,
    count(tb2.id_consulta) as total_consultas
FROM db_dogtor.tipo_consulta tb1
left join consulta tb2 on tb1.id_consulta = tb2.fk_tipo_consulta
group by tb1.id_consulta, tb1.finalidade;
