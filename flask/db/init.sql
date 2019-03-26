CREATE DATABASE db_poll;
use db_poll;

CREATE TABLE tbl_people (
  name VARCHAR(20),
  color VARCHAR(10),
  pet VARCHAR(20),
  PRIMARY KEY (name)
);

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_newPeople`(
    IN input_name VARCHAR(20),
    IN input_color VARCHAR(10),
    IN input_pet VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_people where name = input_name) ) THEN
        select 'Error: Name exists !';
    ELSE
        insert into tbl_people
        (
            name,
            color,
            pet
        )
        values
        (
            input_name,
            input_color,
            input_pet
        );
    END IF;
END$$
DELIMITER ;

INSERT INTO tbl_people
  (name, color, pet)
VALUES
  ('Daniel', 'blue', 'dogs'),
  ('Julia', 'yellow', 'cats');
