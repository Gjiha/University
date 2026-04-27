from io import BytesIO
import helper

class Script:

    opcodes = helper.opcodes('opcodes.cfg') 

    def __init__(self, cmds: list[str]):
        self.cmds = cmds
    
    @classmethod
    def parse(cls, reader: BytesIO, script_len: int):
        cmds = []
        counter = 0
        while counter < script_len:
            first = int.from_bytes(reader.read(1))
            counter += 1
            if 1 <= first <= 75:
                cmds.append(reader.read(first))
                counter += first
            elif first == 76:
                cmds_len = int.from_bytes(reader.read(1))
                cmds.append(reader.read(cmds_len))
                counter += 1 + cmds_len
            elif first == 77:
                cmds_len = int.from_bytes(reader.read(2), byteorder='little')
                cmds.append(reader.read(cmds_len))
                counter += 2 + cmds_len
            elif first == 78:
                cmds_len = int.from_bytes(reader.read(4))
                cmds.append(reader.read(cmds_len))
                counter += 4 + cmds_len
            else:
                cmds.append(first)
        
        return cls(cmds)
    
    def __str__(self):
        return ' '.join([str(Script.opcodes[cmd]) if type(cmd) == int else cmd.hex() for cmd in self.cmds])

if __name__ == '__main__':
    script_hex = '76a9145053bc61c3abe4e2607f55f5a3ca2ce86509e1ad88ac'
    script_len = len(script_hex) // 2

    sc = Script.parse(BytesIO(bytes.fromhex(script_hex)), script_len)
    print(sc)