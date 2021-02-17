#!/usr/bin/env python
# encoding utf-8
# Test for company MET GROUP 2020
# Point No 1
# Deimer Andres Morales Herrera
import handle_matrix as hm

if __name__ == '__main__':

    # Subjects to do tests.
    a = [1,2]
    b = [[1,2],[2,4]]
    c = [[1,2],[2,4],[2,4]]
    d = [[[3,4],[6,5]]]
    e = [[[1,2,3]],[[5,6,7],[5,4,3]],[[3,5,6],[4,8,3],[2,3]]]
    f = [[[1,2,3],[2,3,4]],[[5,6,7],[5,4,3]],[[3,5,6],[4,8,3]]]

    # Here I'm making instances from MyMatrix's objects.

    o = hm.MyMatrix(c)
    o.dimension()
    o.straight()
    o.compute()
