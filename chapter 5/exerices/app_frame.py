
def app_frame(function,**kwargs):
    can_continue = 'y'

    while can_continue != 'q':
        for key in kwargs.keys():
            kwargs[key] = input("Enter "+str(key)+" value : ")

        function(**kwargs)
        can_continue = input("Continue? press q to quit or anything to continue : ")
        can_continue = can_continue[0].lower()