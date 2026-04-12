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
