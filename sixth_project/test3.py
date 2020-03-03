points = [(1, 3,),
          (5, 1),
          (10, 10)
          ]


def sqrDist(p):
    return p[0] ** 2 + p[1] ** 2
points.sort(key=sqrDist)
print(*points)
