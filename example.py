from transformers import AutoTokenizer, AutoModelForCausalLM
import os

# Set the GPU device (make sure to use the correct device ID)
os.environ['CUDA_VISIBLE_DEVICES'] = '3'

# ANSI color codes for terminal output
GREEN = "\033[32m"
RED   = "\033[31m"
RESET = "\033[0m"


# 1. Load model and tokenizer
model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# 2. Read custom templates for enabling and disabling thinking mode
disable_thinking_template, enable_thinking_template = [
    open(f, encoding="utf-8").read()
    for f in ("disable_thinking_r1.jinja", "enable_thinking_r1.jinja")
]

# 3. Define initial conversation history
query= "1+1="
messages = [
    {"role": "user", "content": "1+1="}
]
print(f"Question:\n {query}")

# 4. Format the conversation input using the custom templates
# Apply the "enable thinking" template
enable_thinking_input = tokenizer.apply_chat_template(
    messages,
    tokenize=False,  # Don't tokenize yet
    add_generation_prompt=True,  # Add the prompt for generation
    chat_template=enable_thinking_template  # <<< Apply the custom "enable thinking" template
)

# Apply the "disable thinking" template
disable_thinking_input = tokenizer.apply_chat_template(
    messages,
    tokenize=False,  # Don't tokenize yet
    add_generation_prompt=True,  # Add the prompt for generation
    chat_template=disable_thinking_template  # <<< Apply the custom "disable thinking" template
)

# 5. Convert the formatted inputs into token IDs
input_ids = tokenizer([enable_thinking_input, disable_thinking_input], return_tensors="pt", padding=True).input_ids.to(model.device)

# 6. Generate outputs using the model
outputs = model.generate(input_ids)

# 7. Decode and print the generated responses
# Output for "enable thinking"
print(f"{GREEN}\nEnable Thinking Response:")
generated_text_enable = tokenizer.decode(outputs[0][len(input_ids[0]):], skip_special_tokens=True)
print(f"{generated_text_enable}{RESET}")

# Output for "disable thinking"
print(f"{RED}\nDisable Thinking Response:")
generated_text_disable = tokenizer.decode(outputs[1][len(input_ids[1]):], skip_special_tokens=True)
print(f"{generated_text_disable}{RESET}")
