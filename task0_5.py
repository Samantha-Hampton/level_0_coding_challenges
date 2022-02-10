def triangle_area(s1, s2, s3):  # takes in the lengths of the 3 sides of a triangle
    sp = 0.5 * (s1 + s2 + s3)  # semiperimeter of a triangle
    area = (sp * (sp - s1) * (sp - s2) * (sp - s3)) ** (0.5)
    return area


print(triangle_area(3, 4, 5))
