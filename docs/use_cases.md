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
--8<-- "src/examples/sim.py"
```

This script and the input data files used are hosted on **[Github](https://github.com/antonrv/rmlab-py-client)**.


## Assessing optimization in production

It's good to be scientific in order to assess the performance of the optimization algorithms in production, so we may want to take the following steps:

1. Design an experiment by separating flights in two groups ("*test*" and "*control*") with similar characteristics. For instance, looking at flights in separate markets (so they don't *interact*) but with similar demand and competition patterns):

    * Flights in *test group* will be applied **rmlab** algorithms.

    * Flights in *control group* will behave as normal.

    * The experiment period ends when the last flight departs.

2. Regarding flights in *test group*, upload their historic data (ie: equivalent flights in previous years). Better discard COVID-19 data.

3. Assign pricing models to flights of *test group* that proved to work well on equivalent simulation scenarios (with demand models reflecting real patterns, and competition scenarios).

4. Do once every day until experiment ends:

    4a. At each day, manually trigger (or schedule) optimization passes at the end of each day for the *test group*.

    4b. Gather the results of daily optimization passes and commit proposed changes to Navitaire (eg: modify fare prices, fare thresholds, ...).

5. After all *test* and *control* flights departed, compare the average revenues of both groups under some measure of statistical significance.

**NOTE**: The greater the number of flights of the groups, the more reliable will be the results.

**NOTE**: Experimenters can take step 4b manually, so that they are more confident that nothing horribly wrong is being committed to Navitaire. 
However, steps 4 can be automated in single python program using ``rmlab.API`` commands running in the background without requiring any intervention from the experimenter.


## Automated revenue management in production

Once the performance of optimization algorithms has been validated, following steps could be taken:

1. Upload historic data of multiple flights. This would be done once, at the beginning, using our **Upload API**.

2. Establish a optimization schedule to periodically upload daily data on a daily basis to our servers. This could be done in a background program that periodically uses our **Upload API** once or several times every day.

3. Use our **Operations API** in a program that runs once every night, so that fresh daily data previously loaded is processed for optimization.

4. Fetch the results (using our **Fetch API**) of the optimization runs, optionally committing them to Navitaire after verification.
