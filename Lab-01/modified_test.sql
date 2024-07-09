












CREATE DATABASE 




DROP TABLE IF EXISTS demo_table;


CREATE TABLE demo_table (
  id int NOT NULL SERIAL,
  name varchar(100) NOT NULL,
  created_at timestamp NULL DEFAULT NOW(),
  PRIMARY KEY (id)
) ;









DROP TABLE IF EXISTS employees;


CREATE TABLE employees (
  id int NOT NULL SERIAL,
  name varchar(100) NOT NULL,
  salary decimal(10,2) NOT NULL,
  is_active tinyint(1) NOT NULL,
  start_date date DEFAULT NULL,
  start_time time DEFAULT NULL,
  created_at timestamp NULL DEFAULT NOW(),
  PRIMARY KEY (id)
) ;

















