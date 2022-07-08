CREATE TABLE rame_ochelari(
	id_rama  NUMBER(5),
	nume_rama VARCHAR2(45),
    pret_rama  NUMBER(5)  NOT NULL,
    firma_rama VARCHAR2(50) NOT NULL
    
);
drop table rame_ochelari;

ALTER TABLE rame_ochelari ADD CONSTRAINT rame_ochelari_nume_rama_pk Primary Key(nume_rama) ;
--ALTER TABLE rame_ochelari ADD CONSTRAINT rame_ochelari_nume_rama_ck CHECK(nume_rama like '% %');
ALTER TABLE rame_ochelari ADD CONSTRAINT rame_ochelari_firma_rama_ck CHECK(nume_rama not like'SRL%');


CREATE TABLE dioptrii_ochelari(

    id_dioptrii  NUMBER(5),
	cilindru_ochi_sg  NUMBER(5),
    cilindru_ochi_dr  NUMBER(5),
    sfera_ochi_sg  NUMBER(5),
    sfera_ochi_dr  NUMBER(5),
    AX_sg NUMBER(5) not null,
    AX_dr NUMBER(5) not null,
    
CONSTRAINT dioptrii_ochelari_cilindru_ochi_sg_ck CHECK(cilindru_ochi_sg  between -2     and 2),
CONSTRAINT dioptrii_ochelari_cilindru_ochi_dr_ck CHECK(cilindru_ochi_dr between -2     and 2),
CONSTRAINT dioptrii_ochelari_sfera_ochi_sg_ck CHECK(sfera_ochi_sg  between -6     and 8),
CONSTRAINT dioptrii_ochelari_sfera_ochi_dr_ck CHECK(sfera_ochi_dr  between -6     and 8),
CONSTRAINT dioptrii_ochelari_AX_sg_ck CHECK(AX_sg  between 0    and 180),
CONSTRAINT dioptrii_ochelari_AX_dr_ck CHECK(AX_dr  between 0    and 180)
);
ALTER TABLE dioptrii_ochelari ADD CONSTRAINT dioptrii_ochelari_id_dioptrii_pk Primary Key(id_dioptrii);


drop table dioptrii_ochelari;


CREATE TABLE cumparator(
	id_cumparator  NUMBER(5) not null,
	rama  VARCHAR2(45),
    dioptrii  NUMBER(5)
);

ALTER TABLE cumparator ADD CONSTRAINT cumparator_id_cumparator_pk Primary Key(id_cumparator);
ALTER TABLE cumparator ADD CONSTRAINT cumparator_rama_fk FOREIGN KEY (rama) REFERENCES rame_ochelari(nume_rama);
ALTER TABLE cumparator ADD CONSTRAINT cumparator_dioptrii_fk FOREIGN KEY (dioptrii) REFERENCES dioptrii_ochelari(id_dioptrii) ;
drop table cumparator;

CREATE TABLE accesorii(
    id_cumparator NUMBER(5),
	toc_pret  NUMBER(5)not null,
	laveta_pret  NUMBER(5)not null,
    solutie_curatare_pret  NUMBER(5) not null

);
ALTER TABLE accesorii ADD CONSTRAINT accesorii_id_cumparator_fk FOREIGN KEY (id_cumparator) REFERENCES cumparator( id_cumparator);
drop table accesorii;


--rame_ochelari
INSERT INTO rame_ochelari VALUES (1,'Rama Dama',1200,'SRLVersace');
INSERT INTO rame_ochelari VALUES (2,'AlbDama',600,'SRLDaniel');
INSERT INTO rame_ochelari VALUES (1,'RamaBarbati',1000,'SRLGucci');
INSERT INTO rame_ochelari VALUES (1,'Negru',940,'SRLPrada');
INSERT INTO rame_ochelari VALUES (5,'Deluxe',830,'SRLVerde');

--dioptrii_ochelari
INSERT INTO dioptrii_ochelari VALUES (1,1,1,1,1,1,1);
INSERT INTO dioptrii_ochelari VALUES (2,1,1,2,5,15,24);
INSERT INTO dioptrii_ochelari VALUES (3,-1,1,-2,5,60,160);
INSERT INTO dioptrii_ochelari VALUES (4,-1,-1.4,-6,4,153,113);
INSERT INTO dioptrii_ochelari VALUES (5,-1.7,-1.7,-4,5,121,110);

--cumparator
INSERT INTO cumparator VALUES (1,'Rama Dama',1);
INSERT INTO cumparator VALUES (2,'AlbDama',2);
INSERT INTO cumparator VALUES (3,'RamaBarbati',3);
INSERT INTO cumparator VALUES (8,'Deluxe',4);

--accesorii
INSERT INTO accesorii VALUES (1,30,5,7);
INSERT INTO accesorii VALUES (2,55,5,7);
INSERT INTO accesorii VALUES (3,25,10,7);
INSERT INTO accesorii VALUES (8,25,10,7);
INSERT INTO accesorii VALUES (7,25,10,7);









