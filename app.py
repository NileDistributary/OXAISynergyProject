from aijson import Flow
import asyncio


    
async def main():
    # load the flow
    flow = Flow.from_file('C:/Users/niler/Desktop/OXAISynergyProject/flow.ai.yaml')

    # set any variables
    flow = flow.set_vars(thing='pizza')

    # run it
    result = await flow.run()
    print(result)

    # alternatively, INSTEAD of running it, stream it
    async for result in flow.stream():
        print(result)

if __name__ == '__main__':
    asyncio.run(main())