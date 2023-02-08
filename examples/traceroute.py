import asyncio
import sys

from gufo.traceroute import Traceroute


async def main(addr: str) -> None:
    async with Traceroute() as tr:
        async for info in tr.traceroute(addr, tries=3):
            print(info)


asyncio.run(main(sys.argv[1]))
