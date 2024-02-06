def smart_inter(func):
    def suparate(a, b):
        print("Start")
        func(a, b)
        print("End")
    return suparate


@smart_inter
def inter_leaved(a, b):
    out = ""
    for i in range(len(a)):
        out = out + a[i]+b[i]
    print(out)