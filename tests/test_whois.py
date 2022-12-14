# ----------------------------------------------------------------------
# Gufo Traceroute: whois tests
# ----------------------------------------------------------------------
# Copyright (C) 2022, Gufo Labs
# See LICENSE.md for details
# ----------------------------------------------------------------------

# Python modules
import asyncio

# Third-party modules
import pytest

# Gufo Labs modules
from gufo.traceroute.whois import WhoisClient, WhoisError, WhoisConnectionError

WHOIS = "whois.radb.net"


@pytest.mark.parametrize("addr,exp", [("8.8.8.8", 15169)])
def test_resolve_as(addr: str, exp: int):
    async def inner():
        client = WhoisClient(WHOIS)
        return await client.resolve_as(addr)

    r = asyncio.run(inner())
    assert r == exp


def test_failure():
    async def inner():
        client = WhoisClient(WHOIS)
        return await client.resolve_as("127.0.0.1")

    with pytest.raises(WhoisError):
        asyncio.run(inner())


def test_conn_refused():
    async def inner():
        client = WhoisClient("127.0.0.1")
        return await client.resolve_as("8.8.8.8")

    with pytest.raises(WhoisConnectionError):
        asyncio.run(inner())
