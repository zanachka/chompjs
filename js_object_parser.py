import json

from hello import parse

def parse_js_object(string, initial_stack_size=10):
    return json.loads(parse(string, initial_stack_size))
