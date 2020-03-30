# State Reloader

some times you need do tasks as a sequencial.

like when you create telegram bot

## ex

- user start and enter him/her name
- welcome to he/she and get gender
- then signup user
- ...

```python
from statereloader import StateReloader
START, GET_GENDER, SIGNUP = range(3)
def start(update, context):
    # do staff like show gender keyboard
    # and then return next stat
    return GET_GENDER

def get_gen(update, context):
    # do staff like show confirm keyboard
    return SIGNUP

def signup(update, context):
    # do staff and signup
    return StateRealoader.STOP_STATE # then we dispatch this state realoader for you

sr = StateRealoader(START, {START: start, GET_GENDER: get_gen, SIGNUP: signup})

# when income new update call:
sr.reload(update, context)  
```
