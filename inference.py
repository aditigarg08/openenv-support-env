from env import SupportEnv
from models import Action

def main():
    env = SupportEnv()

    print("[START] task=support env=custom model=baseline")

    result = env.reset()
    obs = result["observation"]
    done = result["done"]

    step = 0
    rewards = []

    while not done:
        step += 1

        ticket_id = min(step, len(obs.tickets))

        action = Action(
            action_type="classify",
            ticket_id=ticket_id,
            predicted_priority="high"
        )

        result = env.step(action)

        reward = result["reward"]
        done = result["done"]
        obs = result["observation"]

        rewards.append(reward)

        print(f"[STEP] step={step} action=classify reward={reward:.2f} done={str(done).lower()} error=null")

    score = sum(rewards) / len(rewards) if rewards else 0.0
    success = score > 0.3

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(f"[END] success={str(success).lower()} steps={step} score={score:.2f} rewards={rewards_str}")


if __name__ == "__main__":
    main()
