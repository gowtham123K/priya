def new_user(name,password,retype):
    if len(password)<8:
        return "password should be min 8 char long"

    if retype==password:
        return "login successfully"
    else:
        return "password not same"


if __name__=="__main__":
    print(new_user("ancy","12345678","12345678"))