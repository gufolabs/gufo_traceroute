# Gufo Traceroute Documentation

*Gufo Traceroute is the Python asyncio IPv4 traceroute implementation.*

## Traceroute Problem

Almost every OS is packaged with the famous `traceroute` utility to check the
routing over IP networks. But what to do if you need to embed the probe
just into your Python application? Running a system's `traceroute` is rarely
an option. System's `traceroute` output formats may vary from system to
system and maintaining the application quickly became a road to hell.
Embedding a traceroute into your application may be a better choice.

Despite the apparent simplicity, it is not a trivial task. To implement the traceroute you have to master a system-dependent Raw Sockets magic. There are many pitfalls. To make things worse, when using hosts
generating and receiving large volumes of ICMP traffic, the application may become very resource-hungry.

## Gufo Traceroute

Gufo Traceroute is the Python asyncio library for IPv4 traceroute. It provides a clean Python API
which hides all raw-socket manipulation details.

``` py
async with Traceroute() as tr:
    async for hop in tr.traceroute("8.8.8.8", tries=3):
        print(hop)
```

Unlike the others traceroute implementations, Gufo Traceroute works well in noisy environments.

## Virtues

* Clean async API.
* IPv4 support.
* High-performance.
* Full Python typing support.
* Editor completion.
* Well-tested, battle-proven code.
