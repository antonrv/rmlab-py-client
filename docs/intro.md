# Introduction

This package works as a client for RMLab services for data upload and fetching, and triggering operations for simulation and revenue optimization.

## Basic program structure

Client - Server interaction requires a `API` asynchronous context manager:

```py
import asyncio
from rmlab.api import API


async def main():

  local_data = "some_data_on_disk.csv"

  # Open a context for server interaction:
  async with API() as api:

    # Upload local data to server
    await api.some_upload_data_function(local_data)

    # Trigger some operation on the server
    await api.some_trigger_operation_function(...)

    # Get operation results
    results = await api.some_fetch_data_function(...)

  # Do whatever with `results` (outside api context manager)

if __name__ == '__main__':

  # Run main function from asyncio context
  asyncio.run(main())
```

Note that `await` keyword need to preceed API commands sent to remote server.

## Authentication

In the previous case, user credentials are assumed to be set in environment variables:

* RMLAB_WORKGROUP
* RMLAB_USERNAME
* RMLAB_PASSWORD

User can also pass the credentials explicitly:

```py
async with API(workgroup="myworkgroup", username="myusername", password="mypassword") as api:
  # Some api commands
  pass
```

## AsyncIO

This package uses python asynchronous utilities of **[AsyncIO](https://docs.python.org/3.9/library/asyncio.html)** to enable 
concurrency by overlapping multiple asynchronous operations triggered 
on the server by the client. In particular, users benefit from concurrency when

* uploading several files to server

* triggering several long-running operations in parallel in the server.

* fetching results from server
