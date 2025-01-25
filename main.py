import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


GREEN = "\033[92m"
WHITE = "\033[97m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


BOX_HORIZONTAL = "━"
BOX_VERTICAL = "┃"
BOX_TOP_LEFT = "┏"
BOX_TOP_RIGHT = "┓"
BOX_BOTTOM_LEFT = "┗"
BOX_BOTTOM_RIGHT = "┛"
BOX_LEFT_MIDDLE = "┣"
BOX_RIGHT_MIDDLE = "┫"

def create_banner(text):
    width = 60
    padding = (width - len(text) - 2) // 2
    return f"{CYAN}{BOLD}{'='* width}\n{' ' * padding}{text}\n{'=' * width}{RESET}"

def create_box(text, title="", width=60, color=""):
    lines = text.split('\n')
    wrapped_lines = []
    for line in lines:
        while len(line) > width - 4:
            wrapped_lines.append(line[:width-4])
            line = line[width-4:]
        wrapped_lines.append(line)
    
    box_top = f"{BOX_TOP_LEFT}{BOX_HORIZONTAL * (width-1)}{BOX_TOP_RIGHT}"
    if title:
        title_line = f"{BOX_LEFT_MIDDLE} {BOLD}{title}{RESET} {BOX_HORIZONTAL * (width - len(title) - 4)}{BOX_RIGHT_MIDDLE}"
    else:
        title_line = ""
    box_content = [f"{BOX_VERTICAL} {color}{line:<{width-3}}{RESET}{BOX_VERTICAL}" for line in wrapped_lines]
    box_bottom = f"{BOX_BOTTOM_LEFT}{BOX_HORIZONTAL * (width-1)}{BOX_BOTTOM_RIGHT}"
    
    return "\n".join(filter(None, [box_top, title_line] + box_content + [box_bottom]))


print("\033[2J\033[H", end="")


print(create_banner("🤖 Reasoning is all you need 🤖"))
print()


print(f"{YELLOW}┌── Question{RESET}")
user_question = input(f"{YELLOW}└─→{RESET} ")


print(f"\n{YELLOW}Select Model:{RESET}")
print(f"1. GPT 3.5")
print(f"2. Llama 3.2 1B")
model_choice = input(f"{YELLOW}Enter choice (1/2):{RESET} ")

# Round 1 - DeepSeek Reasoning
client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
messages = [{"role": "user", "content": user_question}]
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    max_tokens=1000,
)

reasoning_content = response.choices[0].message.reasoning_content

print("\n")
print(f"{create_box(reasoning_content, '💭 Thinking Process', color=GREEN)}")

# Round 2 - smaller model processing
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)


selected_model = "openai/gpt-3.5-turbo-1106" if model_choice == "1" else "meta-llama/llama-3.2-1b-instruct"

completion = client.chat.completions.create(
    model=selected_model,
    messages=[
        {
            "role": "user",
            "content": f"use this following thought process as reference and answer the user question. Do not try to reason through the thought process. THOUGHT PROCESS:{reasoning_content}\n QUESTION: {user_question}"
        }
    ]
)


model_title = "🎯 GPT 3.5" if model_choice == "1" else "🎯 Llama 3.2 1B"
print(f"\n{BLUE}{create_box(completion.choices[0].message.content, model_title)}{RESET}\n")