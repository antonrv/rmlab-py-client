"""Interface to run simulations and set simulation checkpoint dates."""

import asyncio
from re import A
from typing import Mapping

from tqdm import tqdm
from rmlab._api.fetch import APIFetchInternal


class APISimulationInternal(APIFetchInternal):
    """Exposes functions for simulation."""

    async def _periodic_trigger_progress(
        self, scen_id: int, stop_event: asyncio.Event
    ) -> None:
        """Emits progress bars in the console to track the progress of the simulation.

        Args:
            scen_id (int): Scenario ID in which the simulation is running.
            stop_event (asyncio.Event): Event to notify the stop of the simulation.
        """

        pbars: Mapping[str, tqdm] = dict()

        try:

            (
                dates,
                bounded_count,
                schedules_count,
                flights_count,
            ) = await self._fetch_info(scen_id)

            pbars = {
                "local": tqdm(
                    desc=f"Local progress (SC{scen_id})",
                    unit="day",
                    total=(dates.next - dates.current).days,
                    initial=0,
                ),
                "global": tqdm(
                    desc=f"Global progress (SC{scen_id})",
                    unit="day",
                    total=(dates.last_flight_departure - dates.first_flight_load).days,
                    initial=(dates.current - dates.first_flight_load).days,
                ),
                # "pending-schedules": tqdm(
                #     desc=f"Pending schedules (SC{scen_id})",
                #     unit="schedule",
                #     total=schedules_count.total,
                #     initial=schedules_count.pending,
                # ),
                # "live-schedules": tqdm(
                #     desc=f"Live schedules (SC{scen_id})",
                #     unit="schedule",
                #     total=schedules_count.total,
                #     initial=schedules_count.live,
                # ),
                # "past-schedules": tqdm(
                #     desc=f"Past schedules (SC{scen_id})",
                #     unit="schedule",
                #     total=schedules_count.total,
                #     initial=schedules_count.past,
                # ),
                "pending-flights": tqdm(
                    desc=f"Pending flights (SC{scen_id})",
                    unit="flight",
                    total=flights_count.total,
                    initial=flights_count.pending,
                ),
                "live-flights": tqdm(
                    desc=f"Live flights (SC{scen_id})",
                    unit="flight",
                    total=flights_count.total,
                    initial=flights_count.live,
                ),
                "past-flights": tqdm(
                    desc=f"Past flights (SC{scen_id})",
                    unit="flight",
                    total=flights_count.total,
                    initial=flights_count.past,
                ),
            }

            while not stop_event.is_set():

                await asyncio.sleep(2)

                (
                    dates,
                    bounded_count,
                    schedules_count,
                    flights_count,
                ) = await self._fetch_info(scen_id)
                
                pbars["local"].n = pbars["local"].total - (dates.next - dates.current).days
                pbars["global"].n = pbars["global"].total - (dates.last_flight_departure - dates.current).days
                # pbars["pending-schedules"].n = schedules_count.pending
                # pbars["live-schedules"].n = schedules_count.live
                # pbars["past-schedules"].n = schedules_count.past
                pbars["pending-flights"].n = flights_count.pending
                pbars["live-flights"].n = flights_count.live
                pbars["past-flights"].n = flights_count.past

                for pb in pbars.values():
                    pb.update()

        except Exception:

            raise

        finally:

            for pb in pbars.values():
                pb.close()
