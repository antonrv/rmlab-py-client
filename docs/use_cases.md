# Use cases

This package is built for two main purposes: *simulation* and *revenue management*.

Each case typically correspond to different types of users:

* In simulation contexts, researchers evaluate new algorithms aiming at better pricing strategies given specific demand patterns.

* In production contexts, historic and real-time data is periodically uploaded to servers where it is processed for optimization.


## Simulation

The typical simulation worfklow consists on the following steps:

1. Create and upload to server customers models to emulate customers behavior.

2. Create and upload to server pricing models to evaluate carriers pricing strategies.

3. Create core static items and schedules, possibly with multiple carriers competing for the same routes.

4. Create parametric filters to associate previous models with previous static items.

5. Upload parametric filters to server.

6. Upload core static items and schedules to server.

7. Trigger simulation, possibly stopping at specific dates of interest before its full termination.

8. Fetch flight data from server to analyze results

Following script is a fully working example that loads local data, triggers a simulation and fetches the results.

```python
--8<-- "src/samples/sim.py"
```


## Supervised revenue management in production

To validate the performance of **rmlab** algorithms in production, these steps can be followed:

1. Select a few test flights.

2. Upload their historic and daily data to server.

3. Specify pricing models that proved to work well on simulation scenarios.

4. Manually trigger optimization passes at the end of each day for the test flights.

5. Supervise optimizers outcome for each flight, manually committing to Navitaire proposed changes (eg: modify fare prices, fare thresholds, ...)

6. After all test flights departed, compare the performance with respect other flights (eg: a control group of flights with similar characteristics to the group of test flights)


## Automated revenue management in production

1. Upload historic data of multiple flights.

2. Establish a optimization schedule to periodically upload daily data on a daily basis to servers.

3. Establish a optimization schedule to periodically trigger nightly optimization runs.

4. Automatically commit optimization results to Navitaire.
