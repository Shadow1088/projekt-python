from datetime import datetime
from time import sleep

class Timestamp():
    def __init__(self, dt:str, text:str=""):
        self.dt = dt if dt != "" else str(datetime.now())
        self.text = text
    def __sub__(self:object, other:object):
        return f'{datetime.strptime(self.dt, "%Y-%m-%d %H:%M:%S.%f") - datetime.strptime(other.dt, "%Y-%m-%d %H:%M:%S.%f")}'


class LogEntry(Timestamp):
    main_log_types = {"EMPTY":0, "INFO":2, "WARN":4, "CRIT":10, "DEBUG":1, "ERROR":9}
    main_log_tags = ["ACCESS","HEALTH", "MISC"]

    def __init__(self, log_type:str, log_tags:list=[], dt:str="", text:str="", notes:str="", priority:int=1):
        super().__init__(dt, text)
        self.log_type = log_type if log_type.upper() in list(LogEntry.main_log_types.keys()) else ("CUSTOM:"+log_type)
        self.log_tags = log_tags
        self.notes = notes
        self.priority = LogEntry.main_log_types[log_type] if log_type in list(LogEntry.main_log_types.keys()) else priority

    def __str__(self) -> str:
        return f'({self.log_type}, {self.log_tags}, {self.dt}, {self.text}, {self.notes}, {self.priority})'

    def __gt__(self:object, other:object):
        return self.dt > other.dt

    def __eq__(self:object, other:object):
        return self.dt == other.dt and self.notes == other.notes and self.priority == other.priority

    @classmethod
    def print_info(cls):
        for k,v in cls.main_log_types.items():
            print(f"\"{k}\" has priority: {v}")

    @classmethod
    def generate_empty_log(cls):
        return cls("EMPTY")

    def edit_notes(self, new_notes:str=""):
        self.notes = new_notes

    def edit_text(self, new_text:str=""):
        self.text = new_text


test_log0 = LogEntry("TEST")
test_log0_copy = test_log0

print(test_log0.__str__())

sleep(1)
test_log1 = LogEntry("INFO")

print(f"The {test_log1.text} is newer than {test_log0.text}: {test_log1.__gt__(test_log0)}")

print(f"The {test_log0_copy.text} is SAME AS {test_log0.text}: {test_log0_copy.__eq__(test_log0)}")

print(f"The difference between {test_log1.text} and {test_log0.text} is: {test_log1.__sub__(test_log0)}")

LogEntry.print_info()

print(LogEntry.generate_empty_log().dt)
