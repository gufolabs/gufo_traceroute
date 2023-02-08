# Gufo Traceroute Examples: Traceroute Script

Let's write a simple traceroute script

!!! warning

    Traceroute relies on raw sockets, which require
    additional privileges. This example must be
    run from the `root` user.


``` py title="create.py" linenums="1"
--8<-- "examples/traceroute.py"
```

The code is straightforward:

``` py title="create.py" linenums="1" hl_lines="1"
--8<-- "examples/traceroute.py"
```

We need `asyncio.run()` to run asynchronous code, so let's import the `asyncio`.

``` py title="create.py" linenums="1" hl_lines="2"
--8<-- "examples/traceroute.py"
```

Import the `sys` module to parse the CLI argument.

!!! warning

    We use `sys.argv` only for demonstration purposes. Use `argsparse` or alternatives
    in real-world applications.


``` py title="create.py" linenums="1" hl_lines="4"
--8<-- "examples/traceroute.py"
```

The [Traceroute][Traceroute] object holds all necessary API, so let's import it from
`gufo.traceroute`.

``` py title="create.py" linenums="1" hl_lines="7"
--8<-- "examples/traceroute.py"
```

Asynchronous code must be executed in the asynchronous functions or coroutines.
So we define our function as `async`. We expect an address to ping as the
`addr` argument.

``` py title="create.py" linenums="1" hl_lines="8"
--8<-- "examples/traceroute.py"
```
The [Traceroute][Traceroute] can be used as an instance or as an async
context manager. So we use `async with` to create the context.

``` py title="create.py" linenums="1" hl_lines="9"
--8<-- "examples/traceroute.py"
```
The [traceroute()][traceroute] method starts the session as an asynchronous 
yielding [HopInfo][HopInfo] objects per each TTL value.
`tries` sets the number of probes defined per each host. In our case `info`
will have exactly 3 items in `info.hops`,
each either [Hop][Hop] structure, or `None` in case of timeout.

``` py title="create.py" linenums="1" hl_lines="10"
--8<-- "examples/traceroute.py"
```
It is up to the application how to handle the [HopInfo][HopInfo]. In our case
we just print them to get the result like:
```
...
HopInfo(ttl=8, hops=[Hop(addr='62.101.124.1', rtt=0.003837245), Hop(addr='62.101.124.1', rtt=0.003250681), Hop(addr='62.101.124.1', rtt=0.0045064)])
HopInfo(ttl=9, hops=[Hop(addr='209.85.168.64', rtt=0.00286636), Hop(addr='209.85.168.64', rtt=0.002871578), Hop(addr='209.85.168.64', rtt=0.002911354)])
HopInfo(ttl=10, hops=[None, None, None])
HopInfo(ttl=11, hops=[Hop(addr='8.8.8.8', rtt=0.003503296), Hop(addr='8.8.8.8', rtt=0.002676708), Hop(addr='8.8.8.8', rtt=0.002804918)])
```

``` py title="create.py" linenums="1" hl_lines="13"
--8<-- "examples/traceroute.py"
```

Let's run our asynchronous `main()` function via `asyncio.run`
and pass the first command-line parameter as the address.

## Testing

Run example as:

```
$ sudo examples/traceroute 127.0.0.1
HopInfo(ttl=1, hops=[Hop(addr='127.0.0.1', rtt=1.5403e-05, asn=0), Hop(addr='127.0.0.1', rtt=1.0747e-05, asn=0), Hop(addr='127.0.0.1', rtt=5.0981e-05, asn=0)])
```

[Traceroute]: ../../reference/#gufo.traceroute.Traceroute
[traceroute]: ../../reference/#gufo.traceroute.traceroute.Traceroute.traceroute
[HopInfo]: ../../reference/#gufo.traceroute.HopInfo
[Hop]: ../../reference/#gufo.traceroute.Hop