from viewOptions import *
from zoneMutators import *
from gameMutators import *
import re

def funcExec(funcArr, gNum):
    func = db.prepare("SELECT code, args FROM funcs WHERE id = $1::integer;")(funcArr[0])

    if not func:
        return -1
    
    func = func[0]

    if len(funcArr) <= func["args"]:
        return -2

    fstr = re.sub(r"\$0", str(gNum), func["code"])

    for i in range(1, func["args"]+1):
        fstr = re.sub(r"\$"+str(i), str(funcArr[i]), fstr)

    exec(fstr)

    return func["args"]
