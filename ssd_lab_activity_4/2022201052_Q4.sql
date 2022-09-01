USE CUSTOMER_DB;

DELIMITER $$
CREATE PROCEDURE `HELLO`()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE nam VARCHAR(40);
  DECLARE city VARCHAR(35);
  DECLARE contri VARCHAR(20);
  DECLARE grd decimal(10,0);
  DECLARE sample CURSOR FOR SELECT CUST_NAME,CUST_CITY,CUST_COUNTRY,GRADE FROM customer where AGENT_CODE Like "A00%";
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN sample;

  read_loop: LOOP
    FETCH sample INTO nam,city,contri,grd;
    IF done THEN
      LEAVE read_loop;
    END IF;
      select nam,city,contri,grd;
  END LOOP;

  CLOSE sample;
END;

call HELLO();
drop HELLO;


