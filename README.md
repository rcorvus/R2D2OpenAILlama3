# R2D2OpenAILlama3
## Can you use your existing OpenAI code with a local Llama3 instance?  Yes!  
It's super easy with Ollama.  The instructions below explain the code change needed in your OpenAI code and how to install Ollama.  

## How well does it work?
Llama3-8b running on my laptop answers questions a little slower than calling the OpenAI ChatGPT service, but the *quality* of the answers are much better than from chatgpt3.5-turbo. Compare the responses below to the answers I received in my chatgpt3.5-turbo:  

![image](https://github.com/rcorvus/R2D2OpenAILlama3/assets/5025458/79d854bd-6461-4ad8-9c69-f4e5ac3b1bba)  

I tried the Llama3-70b model too, but responses took a VERY long time to execute running on my laptop.  My laptop is no slacker either, it's a brand new G-Series with 32GB RAM, i9 CPU, and NVIDIA GeForce RTX 4060.

## Changes needed to your OpenAI code
R2D2OpenAILlama uses the exact same code as my [R2D2ChatGpt](https://github.com/rcorvus/R2D2ChatGpt),
except we just need to replace this line of code in chatgpt.py:

```
        client = OpenAI(api_key=api_key)
```
With this:
```
        client = OpenAI(
            base_url = 'http://localhost:11434/v1', # ollama service always runs on this local port
            api_key='ollama', # required, but unused
            )
```

Since you no longer need to store your secret OpenAI api key, you can remove the code for that.

## How to install Ollama

1. Download Ollama from [here](https://ollama.com/download) (it works on Linux, Mac, and Windows)  
2. Install it.
3. In Powershell/cmd, run ```ollama pull llama3```, which pulls the "small" 8B LLM, or ```ollama pull llama3:70b``` to pull the giant 70B LLM.  The 8b downloads pretty quickly but the 70b took several hours because it's 40GB and the connection kept crashing requiring me to keep restarting the pull.
4. Start the ollama service on your computer by running ```ollama serve```
5.  Verify the ollama service is running on your computer.  Here it is running on my laptop in systray:  
![image](https://github.com/rcorvus/R2D2OpenAILlama3/assets/5025458/6e5e3906-86eb-42b0-b450-4cb8dbb8a2e7)

