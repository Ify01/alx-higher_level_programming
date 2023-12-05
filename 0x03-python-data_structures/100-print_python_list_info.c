#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about python list
 * @p: python object
 **/

void print_python_list_info(PyObject *p)
{
    long int size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", allocated);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %li: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
