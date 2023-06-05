-- SQL-команды для создания таблиц
В командной строке:
    psql -U postgres
    CREATE DATABASE north;

В pgAdmin4:
CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
    title text,
	birth_date date,
	notes text
);
CREATE TABLE customers
(
	customers_id char(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100)
);
CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customers_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_sity varchar(30) NOT NULL
);

