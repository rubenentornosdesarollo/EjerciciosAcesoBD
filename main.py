from turtle import title
import mysql.connector
from mysql.connector import errorcode
import conexion

def query1():

    cnx = conexion.connect_db()
    cursor = cnx.cursor()

    query = ("SELECT * FROM employees")

    cursor.execute(query)

    # Por cada dato en el resultado de la query, hacemos que los valores se guarden en los brackets y con el format decimos 
    # que brackets tiene que informacion(tienen que estar organizados de igual manera)
    for (emp_no, birth_date, first_name, last_name, gender, hire_date) in cursor:
        print("El empleado con id: {}, {} {} , que es {} nacido el dia {:%d/%m/%Y} fué contratado el {:%d/%m/%Y}".format(
            emp_no, first_name, last_name, gender, birth_date, hire_date))

    cursor.close()
    cnx.close()

def query2():

    cnx = conexion.connect_db()
    cursor = cnx.cursor()

    query = ("SELECT employees.first_name, employees.last_name, salaries.salary FROM employees, salaries WHERE employees.emp_no = salaries.emp_no")

    cursor.execute(query)

    # Por cada dato en el resultado de la query, hacemos que los valores se guarden en los brackets y con el format decimos 
    # que brackets tiene que informacion(tienen que estar organizados de igual manera)
    for (first_name, last_name, salary) in cursor:
        print("El empleado {} {}, tiene un salario de {}€".format(first_name, last_name, salary))

    cursor.close()
    cnx.close()

def query3():

    cnx = conexion.connect_db()
    cursor = cnx.cursor()

    query = ("SELECT employees.first_name, employees.last_name, dept_emp.dept_no FROM employees, dept_emp WHERE employees.emp_no = dept_emp.emp_no")

    cursor.execute(query)

    # Por cada dato en el resultado de la query, hacemos que los valores se guarden en los brackets y con el format decimos 
    # que brackets tiene que informacion(tienen que estar organizados de igual manera)
    for (first_name, last_name, dept_no) in cursor:
        print("El empleado {} {}, esta asignad@ en el departamento {}".format(first_name, last_name, dept_no))

    cursor.close()
    cnx.close()

def query4():

    cnx = conexion.connect_db()
    cursor = cnx.cursor()

    query = ("SELECT employees.first_name, employees.last_name, titles.title FROM employees, titles WHERE employees.emp_no = titles.emp_no")

    cursor.execute(query)

    # Por cada dato en el resultado de la query, hacemos que los valores se guarden en los brackets y con el format decimos 
    # que brackets tiene que informacion(tienen que estar organizados de igual manera)
    for (first_name, last_name, title) in cursor:
        print("El empleado {} {}, tiene el titulo de {}".format(first_name, last_name, title))

    cursor.close()
    cnx.close()

def query6():

    cnx = conexion.connect_db()
    cursor = cnx.cursor()

    query = ("SELECT first_name, last_name FROM employees WHERE employees.hire_date >= '1991-02-22'")

    cursor.execute(query)

    # Por cada dato en el resultado de la query, hacemos que los valores se guarden en los brackets y con el format decimos 
    # que brackets tiene que informacion(tienen que estar organizados de igual manera)
    for (first_name, last_name, title) in cursor:
        print("El empleado {} {}, fué contratad@ despues del 22 de febrero del 1991".format(first_name, last_name))

    cursor.close()
    cnx.close()

bucle = True

while bucle == True:
    print("**************************")
    print("1. Lista la información de los empleados en el que las fechas aparezcan en formato dd/mm/yyyy")
    print("2. Lista nombre, apellidos y salario de los empleados.")
    print("3. Lista nombre, apellidos y departamento al que pertenecen los empleados.")
    print("4. Lista nombre, apellidos y títulos que ostenta cada uno de los empleados.")
    print("5. Lista para cada empleado quien es su manager")
    print("6. Lista los empleados con fecha de contratación posterior a 22 de febrero de 1991.")
    print("7. Salir")
    print("**************************")

    opcion = input("Que opcion eliges: ")

    if (opcion == "1"):
        query1()
    elif (opcion == "2"):
        query2()
    elif (opcion == "3"):
        query3()
    elif (opcion == "4"):
        query4()
    elif (opcion == "5"):
        print("Opcion no implementada")
    elif (opcion == "6"):
        query6()
    elif (opcion == "7"):
            bucle=False
    else:
            print("Opción no encontrada")








#     Lista la información de los empleados en el que las fechas aparezcan en formato
# dd/mm/yyyy
# 2. Lista nombre, apellidos y salario de los empleados.
# 3. Lista nombre, apellidos y departamento al que pertenecen los empleados.
# 4. Lista nombre, apellidos y títulos que ostenta cada uno de los empleados.
# 5. Lista para cada empleado quien es su manager
# 6. Lista los empleados con fecha de contratación posterior a 22 de febrero de 1991.
# Muestra la identificación del empleado, el nombre del empleado, el salario y la fecha
# de contratación