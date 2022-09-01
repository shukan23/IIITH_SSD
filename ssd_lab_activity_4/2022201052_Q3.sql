use CUSTOMER_DB;


DELIMITER $$
CREATE PROCEDURE `CustomersWithHighTransfer` ()
BEGIN
select CUST_NAME,GRADE from customer where CUST_CODE in 
(select CUST_CODE from customer group by CUST_CODE having SUM(OPENING_AMT+RECEIVE_AMT)>10000);
END$$
DELIMITER ;

Call CustomersWithHighTransfer();

drop procedure GetCityNames;