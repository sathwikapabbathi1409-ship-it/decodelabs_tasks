"""
DecodeLabs · Rule-Based AI Chatbot
Project 1 — Pure if-else logic, no ML
"""

import re
import random
from datetime import datetime

# ─────────────────────────────────────────────
#  RULE-BASED RESPONSE ENGINE
# ─────────────────────────────────────────────

rules = [
    {
        "pattern": r"^(hi|hello|hey|howdy|greetings|good\s?(morning|afternoon|evening)|sup|yo)\b",
        "responses": [
            "Hello! 👋 I'm RuleBot, your DecodeLabs AI assistant. How can I help?",
            "Hey there! Welcome to DecodeLabs. I run on if-else logic — ask me anything!",
            "Greetings, engineer! RuleBot is online and ready. What would you like to explore?",
        ],
    },
    {
        "pattern": r"how are you|how('s| is) it going|you doing|how do you feel",
        "responses": [
            "Running at 100% efficiency — no bugs, no exceptions! How about you?",
            "Feeling logical as ever. My if-else chains are in perfect shape! 😄",
            "All systems operational. How can I assist you?",
        ],
    },
    {
        "pattern": r"what('s| is) your name|who are you|introduce yourself",
        "responses": [
            "I'm RuleBot 🤖 — a rule-based AI chatbot built for DecodeLabs Project 1!",
            "The name's RuleBot. Engineered at DecodeLabs using control flow, not neural networks.",
        ],
    },
    {
        "pattern": r"who (made|built|created|programmed) you|your (creator|maker|developer)",
        "responses": [
            "A DecodeLabs intern built me as part of Project 1 — the Rule-Based AI Chatbot milestone! 🛡",
            "A budding AI engineer at DecodeLabs created me. This project is their first step toward mastering AI!",
        ],
    },
    {
        "pattern": r"what can you do|your (skills|capabilities|features)|help me|what do you know",
        "responses": [
            (
                "Here's what I can do:\n"
                "  • Respond to greetings & farewells\n"
                "  • Answer questions about AI & DecodeLabs\n"
                "  • Tell jokes & fun facts\n"
                "  • Explain how I work (if-else logic!)\n"
                "  • Basic math: try '5 + 3'\n"
                "  • Type 'help' for all commands"
            ),
        ],
    },
    {
        "pattern": r"what is (ai|artificial intelligence)|define ai|explain ai",
        "responses": [
            "Artificial Intelligence (AI) is the simulation of human intelligence by machines. "
            "I'm a simple form — a rule-based system using if-else logic instead of learning from data!",
            "AI is a broad field where machines perform tasks that require human thinking. "
            "I'm at the foundation: explicit rules, no learning yet. That's your next milestone! 🚀",
        ],
    },
    {
        "pattern": r"how (do you work|are you built|were you made)|rule.based|if.?else|control flow",
        "responses": [
            (
                "Great question! I work using if-else control flow:\n"
                "  1. You send a message\n"
                "  2. I check it against predefined regex patterns\n"
                "  3. If a rule matches → I respond\n"
                "  4. Loop continues until you say 'bye'\n"
                "No machine learning — pure logic! 💡"
            ),
        ],
    },
    {
        "pattern": r"joke|funny|make me laugh|humor",
        "responses": [
            "Why do programmers prefer dark mode? 🌑\nBecause light attracts bugs! 🐛",
            "How many programmers does it take to change a light bulb? 💡\nNone — it's a hardware problem!",
            "Why did the if-else break up with the loop?\nToo many conditions! 💔",
            "I told my AI a joke about recursion.\nIt laughed, then told it to itself, then to itself... 😅",
        ],
    },
    {
        "pattern": r"fun fact|interesting fact|did you know|tell me something",
        "responses": [
            "Fun fact: The term 'Artificial Intelligence' was coined by John McCarthy in 1956! 🧠",
            "Did you know? The first chatbot was ELIZA (1966) — it used rule-based pattern matching, just like me! 🤖",
            "Fun fact: Rule-based systems dominated AI in the 1980s as 'Expert Systems'. Still used in medicine and law today!",
        ],
    },
    {
        "pattern": r"decodelabs|decode labs|this project|project 1",
        "responses": [
            "DecodeLabs is where AI engineers are forged! 🔥 Project 1 is the foundation — master if-else before ML.",
            "Project 1 teaches you: before any model 'learns', a human defines the rules. That's AI engineering! 🛡",
        ],
    },
    {
        "pattern": r"what (time|day|date) is it|current time|today",
        "responses": [
            f"It's {datetime.now().strftime('%A, %d %B %Y — %I:%M %p')} 🕐",
        ],
    },
    {
        "pattern": r"thank(s| you)|thx|ty\b",
        "responses": [
            "You're welcome! Happy to help 😊",
            "Anytime! That's what rule-based logic is for! 🤖",
            "Glad I could help! Keep building, engineer! 🚀",
        ],
    },
    {
        "pattern": r"^help$|^\/help$",
        "responses": [
            (
                "Available commands & topics:\n"
                "  • 'hello'           → greet me\n"
                "  • 'what is AI?'     → AI definition\n"
                "  • 'how do you work' → my architecture\n"
                "  • 'tell me a joke'  → laughs\n"
                "  • 'fun fact'        → learn something\n"
                "  • '5 + 3'           → basic math\n"
                "  • 'bye'             → exit the loop"
            ),
        ],
    },
    {
        "pattern": r"\b(bye|goodbye|exit|quit|see you|later|cya|farewell|take care)\b",
        "responses": [
            "Goodbye, engineer! 👋 You've taken the first step toward AI mastery. Badge incoming 🛡",
            "See you next time! Keep coding and experimenting. DecodeLabs is proud of you! 🚀",
            "Farewell! Every expert system started with one if-else rule. Keep building! ✨",
        ],
        "exit": True,
    },
]

fallbacks = [
    "Hmm, that doesn't match any of my rules. Try 'help' to see what I can do!",
    "My if-else logic didn't find a match. Type 'help' to explore my commands!",
    "No matching pattern found — rule-based bots only know what their creator programs! 💡",
    "Interesting input! But I'm rule-based. Ask me about AI, jokes, or say 'hello'!",
]


# ─────────────────────────────────────────────
#  ENGINE: match input → find response
# ─────────────────────────────────────────────

def get_response(user_input: str) -> tuple[str, bool]:
    """
    Match user input against rules using regex (if-else logic).
    Returns (response_text, should_exit).
    """
    for rule in rules:
        match = re.search(rule["pattern"], user_input, re.IGNORECASE)
        if match:
            response = random.choice(rule["responses"])
            should_exit = rule.get("exit", False)
            return response, should_exit

    # No rule matched → fallback
    return random.choice(fallbacks), False


def handle_math(user_input: str) -> str | None:
    """Handle basic arithmetic expressions."""
    # Addition
    m = re.search(r"(\d+)\s*\+\s*(\d+)", user_input)
    if m:
        result = int(m.group(1)) + int(m.group(2))
        return f"{m.group(1)} + {m.group(2)} = {result} ✓"

    # Subtraction
    m = re.search(r"(\d+)\s*-\s*(\d+)", user_input)
    if m:
        result = int(m.group(1)) - int(m.group(2))
        return f"{m.group(1)} - {m.group(2)} = {result} ✓"

    # Multiplication
    m = re.search(r"(\d+)\s*[\*x]\s*(\d+)", user_input)
    if m:
        result = int(m.group(1)) * int(m.group(2))
        return f"{m.group(1)} × {m.group(2)} = {result} ✓"

    # Division
    m = re.search(r"(\d+)\s*/\s*(\d+)", user_input)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        if b == 0:
            return "Division by zero? Even I know that's undefined! 😄"
        return f"{a} ÷ {b} = {a / b:.4g} ✓"

    return None  # No math found


# ─────────────────────────────────────────────
#  CONTINUOUS LOOP — the chatbot runs here
# ─────────────────────────────────────────────

def main():
    print("\n" + "=" * 55)
    print("  DecodeLabs · RuleBot v1.0 · Project 1")
    print("=" * 55)
    print("  Welcome! I'm a rule-based AI chatbot.")
    print("  I use if-else logic — no machine learning!")
    print("  Type 'help' for commands. Say 'bye' to exit.")
    print("=" * 55 + "\n")

    # ── Continuous loop ──
    while True:
        try:
            user_input = input("You  : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot  : Session interrupted. Goodbye! 👋")
            break

        if not user_input:
            print("Bot  : (Say something! Type 'help' if you're stuck.)\n")
            continue

        # Check math first (before rule matching)
        math_result = handle_math(user_input)
        if math_result:
            print(f"Bot  : {math_result}\n")
            continue

        # Match against rules (if-else control flow)
        response, should_exit = get_response(user_input)

        print(f"Bot  : {response}\n")

        # Exit condition — breaks the loop
        if should_exit:
            print("=" * 55)
            print("  🛡  Badge Unlocked: Rule-Based AI Chatbot")
            print("      Project 1 complete! Proceed to Project 2.")
            print("=" * 55 + "\n")
            break


if __name__ == "__main__":
    main()
