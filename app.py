from fastapi import FastAPI
from env import SupportEnv
from models import Action

app = FastAPI()
env = SupportEnv()


@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": {
            "tickets": [t.dict() for t in obs.tickets],
            "last_action": obs.last_action
        },
        "reward": 0.0,
        "done": False,
        "info": {}
    }


@app.post("/step")
def step(action: Action):
    result = env.step(action)
    obs = result["observation"]

    return {
        "observation": {
            "tickets": [t.dict() for t in obs.tickets],
            "last_action": obs.last_action
        },
        "reward": result["reward"],
        "done": result["done"],
        "info": result["info"]
    }
