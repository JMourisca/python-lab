def gradingStudents(grades):
    result = []
    for g in grades:
        if g >= 38:            
            nextMult5 = (g//5 + 1) * 5
            if nextMult5 - g < 3:
                g = nextMult5
        result.append(g)
    return result



gs = [73,67,38,33]
print(gradingStudents(gs))