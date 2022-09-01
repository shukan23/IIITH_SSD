DELIMITER $$
CREATE PROCEDURE `AddNumbers`(
IN `operand1` INT,
IN `operand2` INT,
OUT `sum` INT
)
BEGIN
Set sum = operand1 + operand2;
END$$
DELIMITER ;

Call AddNumbers(1,5,@answer);
SELECT @answer;
