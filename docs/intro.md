# Introduction

This package is a python client of RMLab services for data uploading, data fetching, and operations triggering (simulation and revenue optimization).

## Basic program structure

*Client - Server* interaction requires a `API` asynchronous context manager.

A basic program schema:

```py
import asyncio
from rmlab import API

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

# Script entry point
if __name__ == "__main__":

  # async main function must be run in a `asyncio` context
  asyncio.run(main())
```

Note that `await` keyword need to preceed API commands sent to remote server.

As it is exposed in the Code Reference, there are four APIs available for users:

* **Upload API:** To upload user data to the server for processing.

* **Fetch API:** To fetch remote data from the server.

* **Remove API:** To remove remote data from the server.

* **Operations API:** To trigger long running operations (for simulation and revenue optimization) on the server.

## Authentication

In the previous case, user credentials were assumed to be set in following environment variables:

* RMLAB_WORKGROUP
* RMLAB_USERNAME
* RMLAB_PASSWORD

Users can also pass the credentials explicitly:

```py
from rmlab import API

async def main():
  async with API(workgroup="myworkgroup", username="myusername", password="mypassword") as api:
    pass
```

## Workgroups and users

Server resources (both compute and storage) are isolated at workgroup level.

All users belonging to a workgroup view the same data. Each workgroup has specific **services** enabled depending on the subscription plan.

* **Simulation services** to trigger big-scale simulations.

* **Optimization services** to process real data for revenue optimization.

* **Web services** for web-based visualization of the results of previous services.


## AsyncIO

This package uses python asynchronous utilities of **[AsyncIO](https://docs.python.org/3.9/library/asyncio.html)** to enable 
concurrency by overlapping multiple asynchronous operations triggered 
on the server by the client. In particular, users benefit from concurrency when they are

* uploading several big files to server

* triggering several long-running operations in parallel in the server

* fetching results from server
