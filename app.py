from aijson import Flow
import asyncio
import whisper

    
async def main():
    flow = Flow.from_file('meeting_review.ai.yaml')
    flow = flow.set_vars(audiopath='Recording (5).m4a')
    result = await flow.run()
    print(result)


if __name__ == '__main__':
    asyncio.run(main())