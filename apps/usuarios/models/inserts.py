"""

-- INSERTS Area
INSERT INTO Area VALUES('AAVEN','Administrador Ventas');
INSERT INTO Area VALUES('AACOM','Administrador Compras');
INSERT INTO Area VALUES('AAALM','Administrador Almacén');
INSERT INTO Area VALUES('SADMI','Super Administrador');
INSERT INTO Area VALUES('AA','Área Almacén');
INSERT INTO Area VALUES('AC','Área Compras');
INSERT INTO Area VALUES('AV','Área Ventas');

-- INSERTS EMPLOYEE

INSERT INTO Employee VALUES('SA001','edgar@mail.com','pbkdf2_sha256$150000$wE9JmStZJWPh$TRMl/z4tXQYs2VqerMc3di0d0trHq2tPANELEoxmjm4=','Edgar', 'Gómez', '2019-09-23 09:46:31.22461-05', 'SADMI', TRUE, FALSE, FALSE);
INSERT INTO Employee VALUES('SA002','paola@mail.com','pbkdf2_sha256$150000$k0PywcaQyaaV$v/aW088rgR4LrYXJKCgviu956N7j09bmDQz4fIBl2h0=','Paola', 'Quezada', '2019-09-23 09:46:31.22461-05', 'SADMI', TRUE, FALSE, FALSE);

-- Password: employee123
INSERT INTO Employee VALUES('AA001','juan@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Juan', 'López', '2019-09-23 09:46:31.22461-05', 'AA', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AC001','maria@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Maria', 'Echeverria', '2019-09-23 09:46:31.22461-05', 'AC', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AC002','saul@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Saul', 'Dorantes', '2019-09-23 09:46:31.22461-05', 'AC', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AV001','rodrigo@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Rodrigo', 'Huerta', '2019-09-23 09:46:31.22461-05', 'AV', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AV002','anahi@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Anahi', 'Martinez', '2019-09-23 09:46:31.22461-05', 'AV', FALSE, FALSE, TRUE);

-- Password: admin123
INSERT INTO Employee VALUES('AAC01','margarita@mail.com','pbkdf2_sha256$150000$xwzLHlVLuCzf$fdbqPpA02u1sVusR90/nAhu/b7DQUWcLqDzBAMkwaKM=','Margarita', 'Prado', '2019-09-23 09:46:31.22461-05', 'AACOM', FALSE, TRUE, FALSE);
INSERT INTO Employee VALUES('AAL01','alejandro@mail.com','pbkdf2_sha256$150000$xwzLHlVLuCzf$fdbqPpA02u1sVusR90/nAhu/b7DQUWcLqDzBAMkwaKM=','Alejandro', 'León', '2019-09-23 09:46:31.22461-05', 'AAALM', FALSE, TRUE, FALSE);


-- INSERTS CLIENT

INSERT INTO Client VALUES('CL001','Luis Perez','LUPE0201694','Calle Santa Fe #18', 'luis@mail.com', '442-210-1520');
INSERT INTO Client VALUES('CL002','Andrea Montes','AN856985984','Calle Santa Fe #18', 'luis@mail.com', '442-210-1520');

-- INSERTS CATEGORY

INSERT INTO Category VALUES('BOMBON','Bombones', 'Golosina elaborada con azúcar, claras, saborizantes y grenetina, cubierta con azúcar glass y almidón.');
INSERT INTO Category VALUES('CARAMELO','Caramelos', 'El caramelo es un alimento preparado generalmente a base de azúcar.');
INSERT INTO Category VALUES('CHOCOLATE','Chocolates', 'El chocolate se obtiene mezclando azúcar con dos productos derivados de la manipulación de las semillas del cacao.');
INSERT INTO Category VALUES('GALLETA','Galletas', 'La galleta es un producto alimenticio pequeño y plano, dulce o salado, horneado.');
INSERT INTO Category VALUES('GOMITA','Gomitas', 'Caramelos masticables muy dulces, elaborados con gelatina animal añadiendo edulcorantes, saborizantes y colorantes alimentarios');
INSERT INTO Category VALUES('PALETA','Paletas', 'Helado hecho a base de agua, colorante, saborizante y azúcar, de forma alargada y con un palo que lo atraviesa para tomarlo.');
INSERT INTO Category VALUES('PAPA','Papas', 'Se preparan cortándose en rodajas o en forma de bastones y friéndolas en aceite caliente hasta que queden doradas.');

-- INSERTS PROVIDER

INSERT INTO Provider VALUES('DLAROSA','De la Rosa', 'RO180201694', 'Avenida Siempre Viva #18', 'durose@mail.com', '2101616');
INSERT INTO Provider VALUES('RIKOLINO','Rikolino', 'RIDU180204UF8', 'Calle Hinojosa #5', 'rikolino@mail.com', '2101617');
INSERT INTO Provider VALUES('WONKA','Wonka', 'DUWO180207UV6', 'Avenida Revolucion #30', 'wonka@mail.com', '2101618');
INSERT INTO Provider VALUES('JOLLYRAN','Jolly Rancher', 'JORD1803074910', 'Carretera 57 #255', 'jolly@mail.com', '2101619');
INSERT INTO Provider VALUES('GABI','Gabi', 'GAGA180309I74', 'Carretera San Juan S/N', 'gabiga@mail.com', '2101716');
INSERT INTO Provider VALUES('MARINELA','Marinela', 'MAGA180329FU9', 'Epigmenio Gonzales #13', 'marinela@mail.com', '2101717');
INSERT INTO Provider VALUES('GAMESA','Gamesa', 'GAGA100920QY8', 'Calle Benito Juarez #515', 'gamesa@mail.com', '2101718');
INSERT INTO Provider VALUES('CORONADO','Coronado', 'CODU1004111P6', 'Avenida Allende #8A', 'coronado@mail.com', '2101719');
INSERT INTO Provider VALUES('SABRITAS','Sabritas', 'PASA101011396', 'Carretera Mexico-Qro #853', 'sabritas@mail.com', '2102016');
INSERT INTO Provider VALUES('COYOTES','Coyotes', 'PACO151211GS0', 'Avenida Roldan #95', 'coyotes@mail.com', '2102017');


-- INSERTS BOMBON

INSERT INTO Product VALUES(generate_product_id(),'MALVAVISCO CHOC ATREVETE', 'Caja con 28P', 478.91, 'BOMBON', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'MALVALLENO SABOR FRESA', 'Caja con 12P', 254.52, 'BOMBON', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'AMBELITOS MEDIANO DELICIAS ', 'Caja con 15P', 146.99, 'BOMBON', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON AMBELITOS M.M. DELICIAS', 'Caja con 5P', 142.32, 'BOMBON', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'MALVAVISCO FIGURAS DELICIAS', 'Caja con 60P', 279.97, 'BOMBON', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON GRAGEA', 'Caja con 36P', 420.57, 'BOMBON', 'GABI');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON ARCOIRIS', 'Caja con 36P', 420.57, 'BOMBON', 'GABI');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON ANILLO', 'Caja con 28P', 359.83, 'BOMBON', 'GABI');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON MINI', 'Caja con 15P', 233.60, 'BOMBON', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON GRAGEA CORAZON', 'Caja con 18P', 276.79, 'BOMBON', 'RIKOLINO');


-- INSERTS CARAMELO

INSERT INTO Product VALUES(generate_product_id(),'NEW LOOK CANDY', 'Caja con 28P', 584.74, 'CARAMELO', 'JOLLYRAN');
INSERT INTO Product VALUES(generate_product_id(),'PAQUETE DIVERSION', 'Caja con 6P', 715.18, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'APPLE GREEN RING', 'Caja con 8P', 441.26, 'CARAMELO', 'WONKA');
INSERT INTO Product VALUES(generate_product_id(),'CARAMELO SUAVE DISNEY', 'Caja con 30P', 733.02, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CARAMELO HANNA MONTANA', 'Caja con 30P', 525.33, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CARAMELO SUAVE TOY', 'Caja con 30P', 733.02, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'REVOLCADITAS MANGO', 'Caja con 24P', 741.29, 'CARAMELO', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'CONFITADO CHICO', 'Caja con 50P', 918.32, 'CARAMELO', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'CONFITADO CHICO', 'Caja con 50P', 918.32, 'CARAMELO', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'CHILIROKAS FRESA', 'Caja con 24P', 517.52, 'CARAMELO', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'CHILIROKAS SDA', 'Caja con 24P', 587.52, 'CARAMELO', 'CORONADO');


-- INSERTS CHOCOLATE

INSERT INTO Product VALUES(generate_product_id(),'BUBULUBU', 'Caja con 24P', 313.16, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'DUVALIN', 'Caja con 24P', 416.73, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'BON O BON', 'Caja con 12P', 663.24, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'POLLITOS DE CHOCOLATE', 'Caja con 20P', 525.54, 'CHOCOLATE', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'PALETON GRAGONS', 'Caja con 12P', 355.60, 'CHOCOLATE', 'JOLLYRAN');
INSERT INTO Product VALUES(generate_product_id(),'BALON CHUTAZO', 'Caja con 20P', 524.08, 'CHOCOLATE', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'CANASTA ROMPOPE', 'Caja con 24P', 278.49 , 'CHOCOLATE', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'CANASTA FRESA', 'Caja con 24P', 305.59 , 'CHOCOLATE', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'KRANKY GRANEL', 'Caja con 12P', 207.24, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CHOCORETAS', 'Caja con 10P', 460.05, 'CHOCOLATE', 'RIKOLINO');

-- INSERTS PAPAS
INSERT INTO Product VALUES(generate_product_id(),'PAPA HABANERA  30G', 'Caja con 20P ', 321.92, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA JALAPEÑO  30G', 'Caja con 20P ', 354.64, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA ADOBADA  30G', 'Caja con 20P ', 321.92, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA MIX  30G', 'Caja con 30P ', 474.58, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA FUEGO  50G', 'Caja con 8P ', 181.79, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'TOSTITOS', 'Caja con 24P ', 390.11, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'DORITOS NACHO', 'Caja con 18P ', 231.64, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'DORITOS DINAMITA', 'Caja con 18P ', 241.42, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'FRITOS SAL', 'Caja con 6P ', 197.95, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'FRITOS CJORIZO', 'Caja con 6P ', 197.95, 'PAPA', 'SABRITAS');

-- INSERTS PALETAS
INSERT INTO Product VALUES(generate_product_id(),'PALETON CORONADO', 'Caja con 50P ', 572.51, 'PALETA', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA TIRA CORONADO', 'Caja con 50P ', 477.63, 'PALETA', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA PAYASO', 'Caja con 18P ', 801.36, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA PAYASO MINI', 'Caja con 15P ', 637.86, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA BOLA CAJETA', 'Caja con 40P ', 710.29, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA AGRIMIEL', 'Caja con 20P ', 219.38, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CHUPETA ICE CREAM', 'Caja con 12P ', 448.34, 'PALETA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'PALETON DE LA ROSA', 'Caja con 12P ', 491.44, 'PALETA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'PALETA PELUCA MANGO', 'Caja con 18P ', 495.42, 'PALETA', 'DLAROSA');

-- INSERTS GOMITAS
INSERT INTO Product VALUES(generate_product_id(),'GOMA MORA', 'Caja con 16P ', 360.10, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'GOMA FRAMBUESA', 'Caja con 16P ', 360.10, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'GOMA GRENETINA', 'Caja con 16P ', 345.47, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'GOMITA GAHOT', 'Caja con 20P ', 408.89, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'JOLLY RANCHER FILLED GUMMIES', 'Caja 25LBS ', 620.73, 'GOMITA', 'JOLLYRAN');

-- INSERTS GALLETAS
INSERT INTO Product VALUES(generate_product_id(),'BARRITAS FRESA', 'Caja con 12P ', 290.14, 'GALLETA', 'MARINELA');
INSERT INTO Product VALUES(generate_product_id(),'BARRITAS PIÑA', 'Caja con 12P ', 311.63, 'GALLETA', 'MARINELA');
INSERT INTO Product VALUES(generate_product_id(),'PRINCIPE', 'Caja con 9P ', 251.95, 'GALLETA', 'MARINELA');

-- INSERTS STOCK
INSERT INTO Stock VALUES(2, 'PROD0002', 20);
INSERT INTO Stock VALUES(3, 'PROD0003', 20);
INSERT INTO Stock VALUES(4, 'PROD0004', 20);
INSERT INTO Stock VALUES(5, 'PROD0005', 20);
INSERT INTO Stock VALUES(6, 'PROD0006', 20);
INSERT INTO Stock VALUES(7, 'PROD0007', 20);
INSERT INTO Stock VALUES(8, 'PROD0008', 20);
INSERT INTO Stock VALUES(9, 'PROD0009', 20);
INSERT INTO Stock VALUES(10, 'PROD0010', 20);
INSERT INTO Stock VALUES(11, 'PROD0011', 20);
INSERT INTO Stock VALUES(12, 'PROD0012', 20);
INSERT INTO Stock VALUES(13, 'PROD0013', 20);
INSERT INTO Stock VALUES(14, 'PROD0014', 20);
INSERT INTO Stock VALUES(15, 'PROD0015', 20);
INSERT INTO Stock VALUES(16, 'PROD0016', 20);
INSERT INTO Stock VALUES(17, 'PROD0017', 20);
INSERT INTO Stock VALUES(18, 'PROD0018', 20);
INSERT INTO Stock VALUES(19, 'PROD0019', 20);
INSERT INTO Stock VALUES(20, 'PROD0020', 20);
INSERT INTO Stock VALUES(21, 'PROD0021', 20);
INSERT INTO Stock VALUES(22, 'PROD0022', 20);
INSERT INTO Stock VALUES(23, 'PROD0023', 20);
INSERT INTO Stock VALUES(24, 'PROD0024', 20);
INSERT INTO Stock VALUES(25, 'PROD0025', 20);
INSERT INTO Stock VALUES(26, 'PROD0026', 20);
INSERT INTO Stock VALUES(27, 'PROD0027', 20);
INSERT INTO Stock VALUES(28, 'PROD0028', 20);
INSERT INTO Stock VALUES(29, 'PROD0029', 20);
INSERT INTO Stock VALUES(30, 'PROD0030', 20);
INSERT INTO Stock VALUES(31, 'PROD0031', 20);
INSERT INTO Stock VALUES(32, 'PROD0032', 20);
INSERT INTO Stock VALUES(33, 'PROD0033', 20);
INSERT INTO Stock VALUES(34, 'PROD0034', 20);
INSERT INTO Stock VALUES(35, 'PROD0035', 20);
INSERT INTO Stock VALUES(36, 'PROD0036', 20);
INSERT INTO Stock VALUES(37, 'PROD0037', 20);
INSERT INTO Stock VALUES(38, 'PROD0038', 20);
INSERT INTO Stock VALUES(39, 'PROD0039', 20);
INSERT INTO Stock VALUES(40, 'PROD0040', 20);
INSERT INTO Stock VALUES(41, 'PROD0041', 20);
INSERT INTO Stock VALUES(42, 'PROD0042', 20);
INSERT INTO Stock VALUES(43, 'PROD0043', 20);
INSERT INTO Stock VALUES(44, 'PROD0044', 20);
INSERT INTO Stock VALUES(45, 'PROD0045', 20);
INSERT INTO Stock VALUES(46, 'PROD0046', 20);
INSERT INTO Stock VALUES(47, 'PROD0047', 20);
INSERT INTO Stock VALUES(48, 'PROD0048', 20);
INSERT INTO Stock VALUES(49, 'PROD0049', 20);
INSERT INTO Stock VALUES(50, 'PROD0050', 20);
INSERT INTO Stock VALUES(51, 'PROD0051', 20);
INSERT INTO Stock VALUES(52, 'PROD0052', 20);
INSERT INTO Stock VALUES(53, 'PROD0053', 20);
INSERT INTO Stock VALUES(54, 'PROD0054', 20);
INSERT INTO Stock VALUES(55, 'PROD0055', 20);
INSERT INTO Stock VALUES(56, 'PROD0056', 20);
INSERT INTO Stock VALUES(57, 'PROD0057', 20);
INSERT INTO Stock VALUES(58, 'PROD0058', 20);

"""