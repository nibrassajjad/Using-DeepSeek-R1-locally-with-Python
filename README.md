# Using-DeepSeek-offline-with-Python
This guide walks you through setting up and running DeepSeek-R1 locally on Windows 10/11 using LM Studio and Python. No expensive cloud APIs required!

# 1. Install LM Studio
LM Studio allows you to run LLM models locally on your computer.

🔗 Download LM Studio: 👉 https://lmstudio.ai/

✅ Installation Steps:

1. Download and install LM Studio for Windows. (Currently available version: 0.3.9 as of 31 Jan, 2025)
2. Open LM Studio and go to the Discover tab.
3. Search for DeepSeek-R1-Distill-Qwen-7B-GGUF or DeepSeek-R1-Distill-Llama-8B-GGUF and download the model. 
4. Load up the model from "Select a model to load" tab or press Ctrl+L and then load the downloaded model.
5. Go to the Developer tab and start the local API server (default: http://localhost:1234/v1).

<em>(In LM Studio 0.3.8 it appears as a Status button. Change it from "Stopped" to "Running")</em>


![image](https://github.com/user-attachments/assets/451bdc42-63b0-436a-9b2e-f4c202f44df8)

# 2. Install Python & Dependencies

1. Check if you have Python installed by running following in Command Prompt (cmd):

   python --version

   <em>(The version of Python I ran this program on is 3.10.11)</em>

2. If you don't have python installed in your system, download from Python.org and check "Add Python to PATH" during installation. Verify installation by following previous step and then proceed to next step.
3. Once you have python installed. Write this in Command Prompt (cmd):
   
   pip install openai

   <em>(We install the OpenAI package to communicate with LM Studio's local API, allowing us to send prompts and receive responses from offline LLM models using Python.)</em>

5. Verify OpenAI package installation by writing this in Command Prompt (cmd):

   pip show openai

   If installed, you'll see Name: openai and a version number along with some more details.
   <em>(The version of OpenAI I ran this program on is 0.28.0)</em>

   


