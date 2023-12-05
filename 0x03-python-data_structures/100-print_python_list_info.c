#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python list
 * @p: Python object
 **/
void print_python_list_info(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;

    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid argument: Not a Python list\n");
        return;
    }

    printf("[*] Size of the Python List = %li\n", size);

    if (PyListObject_Check(p)) {
        PyListObject *obj = (PyListObject *)p;
        printf("[*] Allocated = %li\n", obj->allocated);

        for (i = 0; i < size; i++) {
            printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
        }
    }
}