"""

-- STORED PROCEDURE
CREATE OR REPLACE FUNCTION generate_product_id() RETURNS varchar AS 
$$
  DECLARE
    id_producto ProductKey;
  BEGIN
    SELECT TO_CHAR(nextval('seq_autoid_prod'::regclass),'"PROD"fm0000') INTO id_producto;
    return id_producto;
  END;
$$ LANGUAGE 'plpgsql';



CREATE OR REPLACE FUNCTION editStock(id_product ProductKey, new_amount numeric(10)) RETURNS BOOLEAN AS 
$$    
  BEGIN
    UPDATE Stock  
    SET amount = new_amount
    WHERE product = id_product;  
    RETURN found;
  END;
$$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION purchaseProduct(id_product ProductKey, amount_product numeric(10), provider ProviderKey, total numeric(12,2), buyer EmployeeKey) RETURNS BOOLEAN AS 
$$    
  DECLARE
	purchase_date timestamp; 
	amount_purchase decimal(10);
	current_amount decimal(10);
	new_amount decimal(10);
	id_purchase decimal(10);
  BEGIN
	SELECT now() INTO purchase_date;
	  Select nextval(pg_get_serial_sequence('Sale', 'id')) INTO id_purchase;
	amount_purchase:= amount_product;
	INSERT INTO Purchase VALUES(id_purchase, id_product, amount_product, provider, total, buyer, purchase_date);
	IF found THEN
	SELECT amount INTO current_amount FROM Stock WHERE product = id_product;
	new_amount := current_amount + amount_purchase;
		UPDATE Stock  
		SET amount = new_amount
		WHERE product = id_product; 
		RETURN found;   
	ELSE
		RETURN found;
	END IF;
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION deletePurchase(id_purchase decimal(10)) RETURNS BOOLEAN  AS
$$
   BEGIN
    DELETE FROM Purchase WHERE id = id_purchase;
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION sellProduct(id_product ProductKey, amount_product numeric(10), client ClientKey, total numeric(12,2), seller EmployeeKey) RETURNS BOOLEAN AS 
$$    
   DECLARE
    sell_date timestamp; 
    amount_sale decimal(10);
    current_amount decimal(10);
    new_amount decimal(10);
	id_sell decimal(10);
  BEGIN
    SELECT now() INTO sell_date;
	Select nextval(pg_get_serial_sequence('Sale', 'id')) INTO id_sell;
    amount_sale:= amount_product;
    INSERT INTO Sale VALUES(id_sell, id_product, amount_product, client, total, seller, sell_date);
    IF found THEN
    SELECT amount INTO current_amount FROM Stock WHERE product = id_product;
    new_amount := current_amount - amount_sale;
		UPDATE Stock  
        SET amount = new_amount
        WHERE product = id_product; 
        RETURN found;   
    ELSE
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION deleteSale(id_sale decimal(10)) RETURNS BOOLEAN  AS
$$
   BEGIN
    DELETE FROM Sale WHERE id = id_sale;
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';



-- STORED PROCEDURE
CREATE OR REPLACE FUNCTION addProduct(name VARCHAR(75), description VARCHAR(75), price DECIMAL(10,2), category CategoryKey, provider ProviderKey, amount_prod numeric(10)) RETURNS BOOLEAN AS 
$$    
  DECLARE
    id_product ProductKey;
	id_stock decimal(10);
  BEGIN
    SELECT generate_product_id() INTO id_product;
    INSERT INTO Product VALUES(id_product, name, description, price, category, provider);
    IF found THEN
		SELECT MAX(id) + 1 FROM Stock INTO id_stock;
        INSERT INTO Stock(id, product, amount) VALUES(id_stock, id_product, amount_prod);
        RETURN found;  
    ELSE
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';


SELECT addProduct('TRIKI TRAKES', 'Caja con 10P ', 291.45, 'GALLETA', 'MARINELA', 20);
SELECT addProduct('PLATIVOLOS', 'Caja con 12P ', 274.14, 'GALLETA', 'MARINELA', 20);
SELECT addProduct('POLVORONES', 'Caja con 12P ', 273.48, 'GALLETA', 'MARINELA', 20);
SELECT addProduct('MAMUT', 'Caja con 8P ', 253.77, 'GALLETA', 'GAMESA', 20);
SELECT addProduct('CHOKIS', 'Caja con 10P ', 102.57, 'GALLETA', 'GAMESA', 20);
SELECT addProduct('CREMAX FRESA', 'Caja con 8P ', 122.03, 'GALLETA', 'GAMESA', 20);
SELECT addProduct('EMPERADOR LIMON 212G', 'Caja con 10P ', 99.72, 'GALLETA', 'GAMESA', 20);




-- STORED PROCEDURE
CREATE OR REPLACE FUNCTION deleteProduct(id_product ProductKey) RETURNS BOOLEAN  AS
$$
   BEGIN
    DELETE FROM Product WHERE product_key = id_product;
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION editProduct(id_product ProductKey, new_name VARCHAR(75), new_description VARCHAR(75), new_price DECIMAL(10,2), new_category CategoryKey, new_provider ProviderKey, new_amount numeric(10)) RETURNS BOOLEAN AS 
$$    
  BEGIN
    UPDATE Product  
    SET name = new_name, description = new_description, price = new_price, category = new_category, provider = new_provider
    WHERE product_key = id_product;  
    IF found THEN
		UPDATE Stock  
        SET amount = new_amount
        WHERE product = id_product; 
        RETURN found;  
    ELSE
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION addNewEployee(emp_key EmployeeKey, email VARCHAR(75), passwrd VARCHAR(128), first_name varchar(50), last_name varchar(50), area AreaCode, super boolean, areab boolean, simplem boolean) RETURNS BOOLEAN AS 
$$
  DECLARE
	  date_join timestamp;     
  BEGIN
    SELECT now() INTO date_join;
    IF super THEN
        INSERT INTO Employee VALUES(emp_key, email, passwrd, first_name, last_name, date_join, area, TRUE, FALSE, FALSE);
        RETURN found;  
    ELSIF areab THEN
        IF area = 'AA' THEN
            INSERT INTO Employee VALUES('AAA01', email, passwrd, first_name, last_name, date_join, area, FALSE, TRUE, FALSE);
            RETURN found;
        ELSIF area = 'AC' THEN
            INSERT INTO Employee VALUES('AAC01', email, passwrd, first_name, last_name, date_join, area, FALSE, TRUE, FALSE);
            RETURN found;
        ELSE
            INSERT INTO Employee VALUES('AAV01', email, passwrd, first_name, last_name, date_join, area, FALSE, TRUE, FALSE);
            RETURN found;
        END IF;
    ELSE
        INSERT INTO Employee VALUES(emp_key, email, passwrd, first_name, last_name, date_join, area, FALSE, FALSE, TRUE);
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION deleteUser(id_user EmployeeKey) RETURNS BOOLEAN  AS
$$
   BEGIN
    DELETE FROM Employee WHERE emp_key = id_user;
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION insertNotif(id_not decimal(10), trans  varchar(5), receiver varchar(40), descrip varchar(128), area varchar(5)) RETURNS BOOLEAN  AS
$$
   BEGIN
   INSERT INTO Notification VALUES(id_not, trans, receiver, descrip, area);
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION editStaff(id_staff EmployeeKey, new_id EmployeeKey, new_name VARCHAR(50), new_ln VARCHAR(50), new_mail VARCHAR(75), new_area AreaCode) RETURNS BOOLEAN AS 
$$    
  BEGIN
    UPDATE Employee  
    SET emp_key = new_id, email = new_mail, first_name = new_name, last_name = new_ln, area = new_area
    WHERE emp_key = id_staff;  
    RETURN found;
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION addNotiEmployee(id decimal(10), noti_id decimal(10), emp_key EmployeeKey, area AreaCode) RETURNS BOOLEAN AS 
$$   
  BEGIN
    INSERT INTO NotiEmployee VALUES(id, noti_id, emp_key, area);
    RETURN found;  
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION updateNotiEmployee(noti_id decimal(10), emp_key EmployeeKey) RETURNS BOOLEAN AS 
$$   
  BEGIN
 	UPDATE NotiEmployee  
    SET last_notification = noti_id, employee = emp_key
    WHERE employee = emp_key; 
    RETURN found;  
  END;
$$ LANGUAGE 'plpgsql';

"""