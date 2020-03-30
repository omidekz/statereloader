import inspect


class StateReloader(object):
    STOP_STATE = StateReloader(-1, None)
    def __init__(self, entry, states: dict):
        self._state = entry
        self._states = states
    
    def reload(self, *args, **kwargs):
        if self._state == StateReloader.STOP_STATE:
            return
        state = self._states.get(self._state)
        if state is None:
            raise Exception("State {} not found".format(self._state))
        if not callable(state):
            raise Exception("{} is not callable".format(state.__name__))
        if len(inspect.getfullargspec(state).args) != 0:
            state_result = state(*args, **kwargs)
        else:
            state_result = state()
        if state_result is None:
            raise Exception("{} return None. None can't be an state".format(state.__name__))
        self._state = state_result
