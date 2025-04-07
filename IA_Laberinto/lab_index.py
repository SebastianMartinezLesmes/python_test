import subprocess
import time
import os

subprocess.run(["python", "generate_lab.py"])

timeout = 3
while timeout > 0:
    if os.path.exists("myMaze.txt"):
        break
    time.sleep(1)
    timeout -= 1

if os.path.exists("myMaze.txt"):
    print("Archivo myMaze.txt encontrado. Ejecutando answer_lab.py...")
    subprocess.run(["python", "answer_lab.py", "myMaze.txt"])
else:
    print("Error: No se generó myMaze.txt en el tiempo esperado.")
