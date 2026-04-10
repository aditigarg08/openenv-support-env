from models import Observation, Action, Ticket

class SupportEnv:

    def __init__(self):
        self.tickets = []
        self.done = False
        self.step_count = 0

    def reset(self):
        self.tickets = [
            Ticket(id=1, text="App crashes on login", priority="high"),
            Ticket(id=2, text="Need help resetting password", priority="medium"),
            Ticket(id=3, text="Feature request for dark mode", priority="low"),
        ]
        self.done = False
        self.step_count = 0

        obs = Observation(tickets=self.tickets, last_action=None)

        return {
            "observation": obs,
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    def step(self, action: Action):
        self.step_count += 1

        correct = next((t for t in self.tickets if t.id == action.ticket_id), None)

        if correct is None:
            reward = 0.0
        elif action.predicted_priority == correct.priority:
            reward = 1.0
        else:
            reward = 0.0

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
