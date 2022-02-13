class User:
    def __init__(self, role, user_id, first, last, age, height, weight):
        self.role = role
        self.user_id = user_id
        self.first = first
        self.last = last
        self.age = age
        self.height = height
        self.weight = weight

class Device:
    def __init__(self, dev_id, dev_type, pat_id, data):
        self.dev_id = dev_id
        self.dev_type = dev_type
        self.pat_id = pat_id
        self.data = data
