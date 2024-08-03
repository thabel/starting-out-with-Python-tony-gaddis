# WIFI DIAGNOSTICS
print("WIFI troubleshooting flowxhart")
print('Reboot the computer and try to connect')
ans = input("Did that fix the problem? <yes> <no>: ")
if(ans=='no'):
    print('Reboot the router and try to connect')
    ans = input("Did that fix the problem? <yes> <no>: ")
if(ans=='no'):
    print('Make sure the cables between the router and modem are plugged in firmly.')
    ans = input("Did that fix the problem? <yes> <no>: ")
if(ans=='no'):
        print('Move the router to a new location.')
        ans = input("Did that fix the problem? <yes> <no>: ")
if(ans=='no'):
        print('Get a New router.')
        
