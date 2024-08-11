from aijson import Flow
import asyncio
import whisper

    
async def main():
    flow = Flow.from_file('projectplanner.ai.yaml')
    flow = flow.set_vars(audiopath='buildahouse.m4a')
    result = await flow.run()
    print(result)
    


if __name__ == '__main__':
    asyncio.run(main())