#  LICENSE RESERVED BY PROJECT LETHAL UB
#  APACHE LICENSED APPLICATION
#  JOIN @LETHAL_OT FOR SUPPORT
#  LETHAL RAIDERS ON FIRE
import os 
import subprocess
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger("Helper")
os.system("git clone https://github.com/LETHAL-ARMY/LETHAL-USERBOT LETHAL")
os.chdir("LETHAL")
process = subprocess.Popen(
        ["python3", "-m", "userbot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    LOGS.warning(er.decode())
print("::::::::::::::")
if out:
    LOGS.info(out.decode())
