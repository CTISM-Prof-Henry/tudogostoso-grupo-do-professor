PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE materias (
            id_materia INTEGER NOT NULL,
            nome TEXT NOT NULL,
            periodos INTEGER NOT NULL,
            PRIMARY KEY (id_materia)
        );
INSERT INTO materias VALUES(1,'Internet das Coisas',3);
INSERT INTO materias VALUES(2,'Banco de Dados',3);
INSERT INTO materias VALUES(3,'Desenvolvimento de Sistemas',3);
INSERT INTO materias VALUES(4,'Sociologia',1);
INSERT INTO materias VALUES(5,'Física',3);
INSERT INTO materias VALUES(6,'Princípios de Gestão',3);
INSERT INTO materias VALUES(7,'História',2);
CREATE TABLE professores (
            id_professor INTEGER NOT NULL,
            nome TEXT NOT NULL,
            cabelo TEXT NOT NULL,
            barba TEXT NOT NULL,
            PRIMARY KEY (id_professor)
        );
INSERT INTO professores VALUES(1,'Fábio','não','não');
INSERT INTO professores VALUES(2,'Henry','sim','sim');
INSERT INTO professores VALUES(3,'Rafael Pereira','sim','sim');
INSERT INTO professores VALUES(4,'Lairane','sim','não');
INSERT INTO professores VALUES(5,'Mário','sim','não');
INSERT INTO professores VALUES(6,'Gustavo','sim','sim');
INSERT INTO professores VALUES(7,'Karina','sim','não');
INSERT INTO professores VALUES(8,'Roberto','sim','não');
INSERT INTO professores VALUES(9,'Priscila','sim','não');
INSERT INTO professores VALUES(10,'Shirley','sim','não');
CREATE TABLE professores_para_materias (
            id_professor INTEGER NOT NULL,
            id_materia INTEGER NOT NULL,
            data_inicio TEXT NOT NULL DEFAULT '2022-04-11',
            data_fim TEXT NOT NULL DEFAULT '2023-02-15',
            PRIMARY KEY (id_professor, id_materia, data_inicio, data_fim),
            FOREIGN KEY (id_professor) REFERENCES professores(id_professor),
            FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
        );
INSERT INTO professores_para_materias VALUES(1,1,'2022-04-11','2023-02-15');
INSERT INTO professores_para_materias VALUES(1,2,'2022-04-11','2023-02-15');
INSERT INTO professores_para_materias VALUES(2,3,'2022-04-11','2023-02-15');
INSERT INTO professores_para_materias VALUES(4,5,'2022-04-11','2022-05-11');
INSERT INTO professores_para_materias VALUES(5,5,'2022-05-11','2022-06-11');
INSERT INTO professores_para_materias VALUES(6,5,'2022-06-11','2023-02-15');
INSERT INTO professores_para_materias VALUES(7,6,'2022-04-11','2022-05-11');
INSERT INTO professores_para_materias VALUES(8,6,'2022-05-11','2022-06-11');
INSERT INTO professores_para_materias VALUES(9,6,'2022-06-11','2023-02-15');
INSERT INTO professores_para_materias VALUES(10,6,'2022-06-11','2023-02-15');
COMMIT;
