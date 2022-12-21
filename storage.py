import json

class MemoryStack:
    """Used as a storage queue."""

    def __init__(self, file_name :str) -> None:
        self.stack = []
        self.commit_to_file = True
        self.output_file = open(file_name, 'w')

    def push(self, value):
        self.stack.append(value)
        json.dump(self.stack, self.output_file)


# Singleton Object
default_output_file = 'output.json'
storage_stack = MemoryStack(default_output_file)

