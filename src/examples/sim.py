import asyncio, os, pathlib
import pandas as pd
from pprint import pprint

from rmlab import API

_DataSamplesPath = str(pathlib.Path(os.path.realpath(__file__)).parent.parent) + '/data_samples/'

async def main():

    # ---- Create an API context manager. 
    # Will read  environment variables: RMLAB_WORKGROUP, RMLAB_USERNAME, RMLAB_PASSWORD
    async with API() as api:

        # ---- Print which scenarios we can access
        print(f"Available scenarios: {api.scenarios}")

        # ---- We'll work on the first scenario
        scen_id = api.scenarios[0]

        # ---- Remove any previous data, so we are sure that we work on a clean scenario
        await api.remove_data_full(scen_id)

        # ---- Upload customers models to server
        await api.upload_batch_customers_models(
            scen_id,
            request_models_fns=[_DataSamplesPath + "/basic/customers_request.poisson_bl1.json"],
            choice_models_fns=[_DataSamplesPath + "/basic/customers_choice.mnlmultiple_bl1.json"],
        )

        # ---- Upload pricing models to server
        await api.upload_batch_pricing_models(
            scen_id,
            range_models_fns=[_DataSamplesPath + "/basic/pricing_range.sample.json"],
            behavior_models_fns=[_DataSamplesPath + "/basic/pricing_behavior.sample.json"],
            optimizer_models_fns=[_DataSamplesPath + "/basic/pricing_optimizer.sample.json"],
        )

        # ---- Upload parametric filters to bind previous models
        await api.upload_parametric_filters(scen_id, _DataSamplesPath + "/basic/table.pfilter.json")

        # ---- Upload core items to server
        await api.upload_batch_core(
            scen_id,
            aircraft_items_fn=_DataSamplesPath + "/basic/table.aircraft.csv",
            airline_items_fn=_DataSamplesPath + "/basic/table.airline.csv",
            airport_items_fn=_DataSamplesPath + "/basic/table.airport.csv",
            city_items_fn=_DataSamplesPath + "/basic/table.city.csv",
            country_items_fn=_DataSamplesPath + "/basic/table.country.csv",
            schedule_items_fn=_DataSamplesPath + "/basic/table.schedule.csv",
        )

        # ---- Print the status after loading data
        scen_dates, scen_items_count, scen_schedules_count, scen_flights_count = await api.fetch_info(scen_id)
        print(f"DATES {scen_dates}")
        print(f"ITEMS COUNT {scen_items_count}")
        print(f"SCHEDULES COUNT {scen_schedules_count}")
        print(f"FLIGHTS COUNT {scen_flights_count}")

        # ---- Start running the simulation on our scenario
        print("Running simulation...")
        await api.trigger_simulation(scen_id)
        print("Simulation finished")

        # ---- Analyze the results of simulation on a specific citysector

        # ---- Fetch all the citysectors of the simulation
        csc_items = await api.fetch_citysectors(scen_id)

        # ---- We'll focus on the first citysector
        csc = csc_items[0]
        print(f"Looking at citysector {csc}")

        # ---- Fetch all flights ids of that citysector
        flights_ids = await api.fetch_flights_ids(scen_id, citysector_id=csc.id)

        # ---- Fetch the books of the first three flights
        some_flights_ids = flights_ids[0:3]
        print(f"Fetching data of flights {some_flights_ids}")

        flights_data = await api.fetch_flights_data_historic(
            scen_id, some_flights_ids, citysector_id=csc.id
        )

        # Once we don't need to interact with API anymore
        # we can get out of the indented context

    # ---- We'll analyze the results of the first flight
    flight_books = flights_data[0]
    print(f"Looking at books of flight {flight_books.id}")

    occupation_x = flight_books.timestamps_array
    occupation_y = flight_books.cumulated_seats_array
    occupation_data = pd.DataFrame(
        data={"Time": occupation_x, "Cumulated occupation": occupation_y}
    ).set_index("Time")
    print(f"Occupation data: {occupation_data}")

    revenue_x = flight_books.timestamps_array
    revenue_y = flight_books.cumulated_revenue_array
    revenue_data = pd.DataFrame(
        data={"Time": revenue_x, "Cumulated revenue": revenue_y}
    ).set_index("Time")
    print(f"Revenue data: {revenue_data}")


if __name__ == "__main__":
    asyncio.run(main())
