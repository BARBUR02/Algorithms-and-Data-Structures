def f(v):
    if v.f!=-1:
        return v.f
    f1=g(v)
    f2=f.fun
    for u in v.emp:
        f2+=g(u)
    v.f=max(f1,f2)
    return v.f
def g(v):
    if v.g!=-1:
        return v.g
    v.g=0
    for u in v.emp:
        v.g +=f(u)
    return v.g
