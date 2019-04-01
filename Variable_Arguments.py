def variable_arguments(a, *b):
    print(a)
    for i in b:
        print(i)

variable_arguments(1,2,'a',5)

def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')