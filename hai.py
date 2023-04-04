def check_scope():
    def do_local():
        test="local"

    def do_non_local():
        nonlocal test
        test="non local"

    def do_global():
        global test
        test="global"


    test="default"
    do_local()
    print("value after do local: "+test)
    do_non_local()
    print("value after non local: "+test)
    do_global()

check_scope()
print("test value after main: "+test)



