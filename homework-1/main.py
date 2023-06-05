"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os


class InstantiateCSVError(Exception):
    pass


with open(os.path.join('north_data', 'customers_data.csv'), 'r', encoding="utf-8") as file:
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="pecheneg762") as conn:
        with conn.cursor() as cur:
            file = csv.DictReader(file)
            for i in file:
                if len(i) != 3:
                    raise InstantiateCSVError('InstantiateCSVError: Файл customers_date.csv поврежден')
                else:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (i['customer_id'],
                                 i['company_name'],
                                 i['contact_name']))
    conn.close()

with open(os.path.join('north_data', 'employees_data.csv'), 'r', encoding="utf-8") as file:
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="pecheneg762") as conn:
        with conn.cursor() as cur:
            file = csv.DictReader(file)
            for i in file:
                if len(i) != 6:
                    raise InstantiateCSVError('InstantiateCSVError: Файл customers_date.csv поврежден')
                else:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (i['employee_id'],
                                 i['first_name'],
                                 i['last_name'],
                                 i['title'],
                                 i['birth_date'],
                                 i['notes']))
    conn.close()

with open(os.path.join('north_data', 'orders_data.csv'), 'r', encoding="utf-8") as file:
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="pecheneg762") as conn:
        with conn.cursor() as cur:
            file = csv.DictReader(file)
            for i in file:
                if len(i) != 5:
                    raise InstantiateCSVError('InstantiateCSVError: Файл customers_date.csv поврежден')
                else:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (i['order_id'],
                                 i['customer_id'],
                                 i['employee_id'],
                                 i['order_date'],
                                 i['ship_city']))
    conn.close()
