# ----------------------------------------------------------------------
# Gufo Traceroute: tests
# ----------------------------------------------------------------------
# Copyright (C) 2022, Gufo Labs
# See LICENSE.md for details
# ----------------------------------------------------------------------

# Python modules
import asyncio

# Third-party modules
import pytest

# Gufo Labs modules
from gufo.traceroute import Traceroute


def test_traceroute_ipv4():
    async def inner():
        hops = []
        async with Traceroute() as tr:
            async for hop in tr.traceroute("127.0.0.1", tries=3):
                hops.append(hop)
        return hops

    r = asyncio.run(inner())
    assert len(r) == 1
    assert r[0].ttl == 1
    assert len(r[0].hops) == 3
    for hop in r[0].hops:
        assert hop.addr == "127.0.0.1"


def test_traceroute_ipv6():
    async def inner():
        hops = []
        async with Traceroute() as tr:
            async for hop in tr.traceroute("::1", tries=3):
                hops.append(hop)
        return hops

    with pytest.raises(NotImplementedError):
        asyncio.run(inner())


def test_tos():
    async def inner():
        async with Traceroute(tos=1) as tr:
            async for _ in tr.traceroute("127.0.0.1", tries=3):
                break

    asyncio.run(inner())
