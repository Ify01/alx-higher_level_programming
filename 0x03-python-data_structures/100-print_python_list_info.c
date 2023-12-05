#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about python list
 * @p: python object
 **/

void print_python_list_info(PyObject *p)
{
    long int cover, given, y;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    cover = PyList_Size(p);
    given = ((PyListObject *)p)->given;

    printf("[*] Size of the Python List = %li\n", cover);
    printf("[*] Allocated = %li\n", given);
    for (y = 0; y < cover; y++)
    {
        item = PyList_GetItem(p, y);
        printf("Element %li: %s\n", y, Py_TYPE(item)->tp_name);
    }
}
