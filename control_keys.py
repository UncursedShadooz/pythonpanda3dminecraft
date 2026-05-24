class InputManager:
    def __init__(self, base_app):
        self.base = base_app
        
        self.key_bindings = {
            "w": "forward",
            "arrow_up": "forward",
            "a": "left",
            "arrow_left": "left",
            "s": "backward",
            "arrow_down": "backward",
            "d": "right",
            "arrow_right": "right",
            "space": "jump",
            "mouse1": "hit"
        }