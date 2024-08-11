from aijson import Flow
import asyncio
import whisper
from dotenv import load_dotenv,find_dotenv

load_dotenv()
  
async def main():
    flow = Flow.from_file('projectplanner.ai.yaml')
    flow = flow.set_vars(audiopath='buildahouse.m4a')
    result = await flow.run('report')
    print(result)
    jsonresult = await flow.run('structure')
    print(jsonresult)


if __name__ == '__main__':
    asyncio.run(main())