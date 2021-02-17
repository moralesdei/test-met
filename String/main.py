#!/usr/bin/env python
# encoding utf-8
# Test for company MET GROUP 2020
# Point No 1
# Deimer Andres Morales Herrera
import handle_string as hs

if __name__ == '__main__':

    # Subjects to do tests.
    a = "Hello world"
    b = "2 + 10 / 2 - 20"
    c = "(2 + 10) / 2 - 20"
    d = "(2 + 10 / 2 - 20"

    # Here I'm making instances from MyMatrix's objects.


    o = hs.MyString(d)
    o.operation()
    o.compute()
