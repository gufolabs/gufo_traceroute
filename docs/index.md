---
template: index.html
hide:
    - navigation
    - toc
hero:
    title: Gufo Traceroute
    subtitle: The Python asyncio IPv4 traceroute implementation
    install_button: Getting Started
    source_button: Source Code
---
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

## Features

* Clean async API.
* IPv4 support.
* Built-in whois client for AS number resolution.
* High-performance.
* Full Python typing support.
* Editor completion.
* Well-tested, battle-proven code.

## On Gufo Stack

This product is a part of [Gufo Stack][Gufo Stack] - the collaborative effort 
led by [Gufo Labs][Gufo Labs]. Our goal is to create a robust and flexible 
set of tools to create network management software and automate 
routine administration tasks.

To do this, we extract the key technologies that have proven themselves 
in the [NOC][NOC] and bring them as separate packages. Then we work on API,
performance tuning, documentation, and testing. The [NOC][NOC] uses the final result
as the external dependencies.

[Gufo Stack][Gufo Stack] makes the [NOC][NOC] better, and this is our primary task. But other products
can benefit from [Gufo Stack][Gufo Stack] too. So we believe that our effort will make 
the other network management products better.

[Gufo Labs]: https://gufolabs.com/
[Gufo Stack]: https://gufolabs.com/products/gufo-stack/
[NOC]: https://getnoc.com/