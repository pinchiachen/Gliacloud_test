def anonymous (x):
    return x**2 + 1

def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        #area_min < area < area_max¡AI set area = (area_min + area_max) / 2 
        area += (anonymous(intercept - step) * step + anonymous(intercept) * step ) / 2
    return area

print(integrate(anonymous, 0, 10))