import os
from openai import AzureOpenAI
from aijson import register_action #AI JSON Element

@register_action
def whisper(audiopath: str):

    client = AzureOpenAI(
        api_key=os.getenv("AZURE_API_KEY"),  
        api_version=os.getenv("AZURE_API_VERSION"),
        azure_endpoint = os.getenv("AZURE_API_BASE")
    )

    deployment_id = "whisper" #This will correspond to the custom name you chose for your deployment when you deployed a model."
    audio_test_file = audiopath

    result = client.audio.transcriptions.create(
        file=open(audio_test_file, "rb"),            
        model=deployment_id
    )
    print(result)
    return result