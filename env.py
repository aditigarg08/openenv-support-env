from models import Observation, Action, Ticket

class SupportEnv:

    def __init__(self):
        self.tickets = []
        self.done = False
        self.step_count = 0

    # ✅ RESET (FIXED)
    def reset(self):
        self.tickets = [
            Ticket(id=1, text="App crashes on login", priority="high"),
            Ticket(id=2, text="Need help resetting password", priority="medium"),
            Ticket(id=3, text="Feature request for dark mode", priority="low"),
        ]
        self.done = False
        self.step_count = 0

        return {
            "observation": Observation(
                tickets=self.tickets,
                last_action=None
            ),
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    # ✅ STEP (CLEAN + PARTIAL REWARD)
    def step(self, action: Action):
        self.step_count += 1

        # find correct ticket
        correct = next((t for t in self.tickets if t.id == action.ticket_id), None)

        # safe fallback
        if correct is None:
            reward = 0.0
        else:
            if action.predicted_priority == correct.priority:
                reward = 1.0
            elif correct.priority == "high" and action.predicted_priority == "medium":
                reward = 0.5   # partial reward
            else:
                reward = 0.0

        # end condition
        if self.step_count >= len(self.tickets):
            self.done = True

        return {
            "observation": Observation(
                tickets=self.tickets,
                last_action=str(action)
            ),
            "reward": reward,
            "done": self.done,
            "info": {}
        }

    # ✅ STATE (SAFE FORMAT)
    def state(self):
        return {
            "tickets": [t.dict() for t in self.tickets],
            "done": self.done,
            "step_count": self.step_count
        }
