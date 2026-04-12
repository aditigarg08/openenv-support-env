import os
from openai import OpenAI

from env import SupportEnv
from models import Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def main():
    env = SupportEnv()

    print(f"[START] task=support env=openenv model={MODEL_NAME}")

    obs = env.reset()
    done = False
    step = 0
    rewards = []

    while not done:
        step += 1

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
