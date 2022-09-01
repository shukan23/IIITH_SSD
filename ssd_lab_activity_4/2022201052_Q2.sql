use CUSTOMER_DB;


DELIMITER $$
CREATE PROCEDURE `GetCityNames` ( IN `cityname` VARCHAR(35))
BEGIN
select CUST_NAME from customer where WORKING_AREA=cityname;
END$$
DELIMITER ;
Call GetCityNames("Bangalore");

drop procedure GetCityNames;