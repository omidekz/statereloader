from statreloader import StateReloader


START, WELCOME, GOODBYE = range(3)
def start(name, lname):
    if not (name or lname):
        print('start not passed')
        return START
    print('start passed')
    return WELCOME

def welcome():
    print('welcom')
    return GOODBYE

def gb(name):
    print('byeeeee', name, '.')
    return START


statr = StateReloader(START, {START: start, GOODBYE: gb, WELCOME: welcome})
statr.reload('omid', 'karimzade')
statr.reload()
statr.reload('omid')
