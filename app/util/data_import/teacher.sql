LOAD DATA INFILE '/var/lib/mysql-files/teacher_108.csv'
IGNORE INTO TABLE teacher CHARACTER SET UTF8
FIELDS
    TERMINATED BY ','
    ENCLOSED by '"'
LINES
    TERMINATED BY '\r\n'
IGNORE 1 ROWS
(real_id, name);