# Data model

Data in server can be classified in several categories

## Core static data

Directly uploaded by the user, assumed to remain unaltered once uploaded. New items can always be appended, but existing items are not meant to be modified.

* Airlines: carriers managing flights.
* Aircraft models: referenced by flights.
* Airports: endpoints of flights, associated to a city.
* Cities: regions associated to a country, possibly referenced by multiple *airports*.
* Countries: regions associated to a currency, possibly referenced by multiple *cities*.

## Flights schedules

Directly uploaded by the user. Schedules are templates from which a set of flights with common characteristics are generated. Uploading flights schedules is the fastest way to upload an arbitrary number of flights into the server.

## Route-like items

They are implicitly derived in the server from uploaded flights schedules.

* Sectors: Pairs of origin-destination airports
* CitySectors: Pairs of origin-destination cities
* Routes: Pairs of airports with unspecified direction
* CityRoutes: Pairs of cities with unspecified direction

## Flight items

Represent *static* flight information, such as origin, destination, departure time, aircraft, etc. Flight *items* are generally generated from *flights schedules*, but can be explicitly uploaded by the user.

## Flight data

Represent *dynamic* flight data generated as the seats of on-sale and not-departed flights are booked by customers during its selling period.

## Parametric data

Data structures directly uploaded by the user, used for simulation and revenue optimization.

We can distinguish between *customers models*, *pricing models*, and *parametric filters*.

### Customers models

Their purpose is to model the customers behavior (ie: how *demand* behaves), so their are used just in simulation contexts.

They are categorized into *request* and *choice* models.

**Request models** model the rate of booking requests on flights. 

**Choice models** emulate the customers decision process while choosing a flight over other competing flight.


#### Flight competition criteria

In simulation contexts, the competition criteria for two flights is rooted at the *CitySector* and *date* level.
That is, two flights will compete if they cover the same citysector and depart on the same date.
This means that virtual customers will be offered as many booking offers per request as competing flights with available seats.

### Pricing models

Their purpose is to define the pricing strategies of carriers (ie: how *supply* behaves), and their use is applied on both simulation and real contexts.

They are divided into *range*, *behavior*, and *optimizer* models.

**Ranges** specify parameters to define the pricing range and fare granularity.

**Behaviors** specify the underlying pricing strategy to allocate seats to fares depending on the day before departure.

**Optimizers** specify the operations that are run in order to maximize the revenue given historic and real-time data.

### Parametric filters

Their purpose is to associate parametric models with specific items. In particular:

**Customers models** can be associated to the following *route-like* elements:

* **CitySectors**, if user wants to simulate travel demand patterns between a origin city and a destination city.
* **CityRoutes**, if user wants to simulate round trip demand patterns between a pair of cities.

**Pricing models** need to be associated to flights, either directly to *Flight* items, or indirectly to a group of flights sharing specific attributes. For instance, each pricing model can be associated to:

* all flights generated from the same *flight schedule*
* all flights covering a specific *CityRoute* 
* all flights covering a specific *Route*
* all flights covering a specific *Sector*
* all flights of a specific *Airline*
* all flights with a specific *Flight number*
* all flights departing on a specific *date range period*
* all flights associated to a combination of previous conditions.

