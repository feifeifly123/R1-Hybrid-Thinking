# 🧠 R1-Hybrid-Thinking

**R1-Hybrid-Thinking** enhances DeepSeek R1 models with hybrid inference, enabling instant switching between rapid and deep reasoning modes—using just one line of code. This allows users to easily optimize the model’s thinking depth based on task complexity, maximizing performance and efficiency.

## 🔑 Key Features

- **One-Line Hybrid Reasoning Activation**: Easily toggle between fast and deep thinking modes with a single line of code, streamlining the deployment process.

- **Seamless Integration**: Compatible with Hugging Face Transformers and vLLM frameworks, facilitating straightforward deployment across various platforms.

- **Comprehensive Benchmarking**: Includes tools to evaluate the impact of different reasoning modes on performance and accuracy, aiding in informed decision-making.

- **User-Friendly Interface**: Offers intuitive controls to switch between thinking modes, either through API parameters or in-prompt commands, enhancing usability.

## ⚙️ How It Works

**R1-Hybrid-Thinking** leverages ChatML formatting to explicitly control the reasoning mode:

- Wrapping prompts with `<think>\n\n</think>` tags instructs the model to bypass slow, deep reasoning (System 2) and switch immediately to rapid, intuitive reasoning (System 1).
- This provides instant responses to simple questions, optimizing inference speed without unnecessary computational overhead.

## 🚀 Quick Start

Activate the fast reasoning mode in your code with just one line:

```python
disable_thinking_input = tokenizer.apply_chat_template(
    messages,
    tokenize=False,  # Don't tokenize yet
    add_generation_prompt=True,  # Add the prompt for generation
    chat_template=disable_thinking_template  # Apply the \"disable thinking\" template
)
```

## 📌 Example

**Question:**
```
1+1=
```

**Enable Thinking Response:**
```
I need to calculate the sum of 1 and 1.

Adding these two numbers together gives me 2.
```

```
Sure, let's solve the addition problem step by step.

**Problem:**
1 + 1 =

**Solution:**
To find the sum of 1 and 1, we can add the numbers together.

1 + 1 = 2

**Answer:**
2
```

**Disable Thinking Response:**
```
1 + 1 = 2
```

## 🗺️ Roadmap

| Status | No. | Feature                                                  |
|--------|-----|----------------------------------------------------------|
| ✅      | 1   | **Prompt-based Hybrid-Thinking**                         |
| ⏳      | 2   | **Token-decoding-based Hybrid-Thinking** *(Coming soon)* |
| ⏳      | 3   | **Hugging Face Usage Tutorial** *(Coming soon)*          |
| ⏳      | 4   | **vLLM Integration and Usage Tutorial** *(Coming soon)*  |
| 📌      | 5   | **Dataset Benchmarking of Hybrid-Thinking Approaches** *(To do)* |

## 📧 Contact

If you have any questions or issues, please feel free to contact us.
kchen24@m.fudan.edu.cn
