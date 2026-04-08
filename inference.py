from env import SupportEnv
from models import Action

def main():
    env = SupportEnv()

    print("[START] task=support env=custom model=baseline")

    obs = env.reset()
    done = False
    step = 0
    rewards = []

    while not done:
        step += 1

        # Simple baseline: always predict "high"
        action = Action(
            action_type="classify",
            ticket_id=step,
            predicted_priority="high"
        )

        result = env.step(action)

        reward = result["reward"]
        done = result["done"]

        rewards.append(reward)

        print(f"[STEP] step={step} action=classify reward={reward:.2f} done={str(done).lower()} error=null")

    score = sum(rewards) / len(rewards)
    success = score > 0.5

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(f"[END] success={str(success).lower()} steps={step} score={score:.2f} rewards={rewards_str}")


if __name__ == "__main__":
    main()