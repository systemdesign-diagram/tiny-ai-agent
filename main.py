"""Entry point for the tiny AI agent scaffold."""

from agent.llm import generate_response


def main() -> None:
    print("Tiny AI Agent")
    print("Type 'exit' to quit.")

    while True:
        try:
            user_message = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_message.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not user_message:
            continue

        try:
            reply = generate_response(user_message)
        except Exception as exc:
            print(f"Agent error: {exc}")
            continue

        print(f"Agent: {reply}")


if __name__ == "__main__":
    main()
