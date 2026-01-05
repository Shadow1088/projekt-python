from simpleeval import simple_eval
count = simple_eval(input("how many cats do you want to generate?"))
if int(count) > 10**9:
    print("We are terribly sorry, we are unable to generate {} cats".format(count))
else:
    print(f"We got your order of {count} cats")
