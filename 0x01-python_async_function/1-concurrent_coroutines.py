import asyncio
from typing import List# Replace 'previous_file' with the actual file name
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    # Spawn wait_random n times with the specified max_delay
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Wait for all spawned tasks to finish and collect delays
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    # The delays will already be in ascending order because 'as_completed' returns them as they finish
    return delays
