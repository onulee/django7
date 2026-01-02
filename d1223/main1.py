from environ import Env
import os
env = Env()
env.read_env(overwrite=True)

key = os.environ['OPENAI_API_KEY']
print(key)