import readline
import json
import re


class Completer(object):
    def __init__(self):
        with open('command/base.json', 'r') as f:
            self.commands_base=json.loads(f.read())
            self.RE_SPACE = re.compile('.*\s+$', re.M)
        
        
    def complete_test1(self, args, cmd):
    
        if args is None:
            return COMMANDS_test1
        
        results=[None]
        if len(args) == 1:
            results = [c for c in COMMANDS_test1 if c.startswith(args[0])] + [None]
        
        return results
    
    def complete(self, text, state):
        
        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()
        # show all commands
        if not line:
            return [c + ' ' for c in self.commands_base][state]
        
        if self.RE_SPACE.match(buffer):
            line.append('')
        
        cmd = line[0].strip()
        if cmd in self.commands_base:
            #impl = getattr(self, 'complete_%s' % cmd)
            #args = line[1:]
            #return (impl(args,cmd) + [None])[state]
            return [None][state]
            
        results = [c + ' ' for c in self.commands_base if c.startswith(cmd)] + [None]
        return results[state]


