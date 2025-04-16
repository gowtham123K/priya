from login import new_user
def testing():
    assert(new_user("ancy","12345678","12345678")) == "login successfully"
    assert(new_user("ancy","12345678","123456789")) == "password not same"

if __name__=="__main__":
    print(testing())
    print("testing successful")
