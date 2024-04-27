# R2D2OpenAILlama3
Can you use your existing OpenAI code with a local Llama3 instance?  Yes!
It's super easy with Ollama (instructions on how to install Ollama below).

R2D2OpenAILlama uses the exact same code as my R2D2ChatGpt https://github.com/rcorvus/R2D2ChatGpt,
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

## How to install Ollama

1. Download Ollama from here (it works on Linux, Mac, and Windows):  https://ollama.com/download
2. Install it.
3. In Powershell/cmd, run ```ollama pull llama3```, which pulls the "small" 8B LLM, or ```ollama pull llama3:70b``` to pull the giant 70B LLM.  The 8b downloads pretty quickly but the 70b took several hours because it's 40GB and the connection kept crashing requiring me to keep restarting the pull.
4. Start the ollama service on your computer by running ```ollama serve```
5.  Verify the ollama service is running on your computer.  Here it is running on my laptop in systray: