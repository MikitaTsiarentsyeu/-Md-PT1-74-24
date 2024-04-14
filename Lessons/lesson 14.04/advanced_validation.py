def validate_number(control_value):

    while True:

        x = input(f"Enter your value higher than {control_value}\n")

        try:

            x = float(x)

            if x <= control_value:
                raise RuntimeError("the value is very low")
            
            return x

        except ValueError:
            print("it was not a number, please try again")
            continue
        except RuntimeError as e:
            print(e)
            continue


print(validate_number(77))