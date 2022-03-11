"""Script exposing enumeration types and values to add a type/value-safe 
layer for correctness."""

from enum import Enum


class DataRemoveKind(Enum):
    COMPLETE = "full"
    HISTORIC = "restart"


class FileExtensions(Enum):
    """All possible extensions of uploadable files"""

    JSON = ".json"
    CSV = ".csv"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class ParametricModelKind(Enum):
    """All possible enumerations for types of parametric models"""

    CUSTOMERS = "customers"
    PRICING = "pricing"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class CustomersModelKind(Enum):
    """All possible enumerations for types of customers models"""

    REQUEST = "request"
    CHOICE = "choice"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class PricingModelKind(Enum):
    """All possible enumerations for types of pricing models"""

    RANGE = "range"
    BEHAVIOR = "behavior"
    OPTIMIZER = "optimizer"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class DayOfWeek(Enum):
    """Days of week enumeration"""

    MONDAY = 1
    TUESTDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def int_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v]


class ScenarioDayStatus(Enum):
    """All possible enumerations of daily status"""

    EMPTY = "empty"
    STARTED = "started"
    ENDED = "ended"
    IN_PROGRESS = "inprogress"
    READY = "ready"
    PAUSED = "paused"
    SIMULATED = "simulated"
    OPTIMIZED = "optimized"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class ScenarioState(Enum):
    """All possible enumerations of scenario states"""

    EMPTY = "empty"
    IN_PROGRESS = "inprogress"
    PAUSED = "paused"
    FINISHED = "finished"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class FlightDataKind(Enum):
    """All possible enumerations for types of flight data"""

    ACTUAL_BOOKS = "actual-books"
    EXPECTED_BOOKS = "expected-books"
    DYNAMIC_BOOKS = "dynamic-books"
    THRESHOLDS_SETTINGS = "thresholds-settings"
    PRICE_PER_SEAT_SETTINGS = "pps-settings"
    EVENTS = "events"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class FlightEvent(Enum):
    """All possible enumerations for flight events"""

    FLIGHT_LOADED = "flight-loaded"
    FLIGHT_DEPARTED = "flight-departed"
    FLIGHT_SOLD_OUT = "flight-sold-out"
    SCHEDULED_OPT_PASS = "scheduled-rms-pass"
    DONE_OPT_PASS = "done-rms-pass"
    COMMIT_OPT_PASS = "commit-rms-pass"
    LOADED_INITIAL_THRESHOLDS = "loaded-initial-thresholds"
    OPERATOR_EDIT_THRESHOLDS = "operator-edit-thresholds"
    OPERATOR_DYNAMIC_TO_EXPECTED = "operator-dynamic-to-expected"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class OptimizationSelectorFilterKind(Enum):
    """All possible enumerations for optimization selector kinds."""

    DAY_OF_WEEK = "day-of-week"
    HOUR_SLOT = "hour-slot"
    SECTOR = "sector"
    SCHEDULE = "schedule"
    FLIGHT_NUMBER = "flight-number"
    SEAT_CAPACITY = "seat-capacity"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class TimeUnit(Enum):
    """Enumerations for time units in optimization selector."""
    
    DAY = "day"
    MONTH = "month"
    YEAR = "year"

    @classmethod
    def str_to_enum_value(cls, v: str):
        # Make it case-insensitive
        v = v.lower()
        if v[-1] == "s":  # Make it singular
            v = v[0:-1]
        return cls.__dict__["_value2member_map_"][v]


class OptimizationForecasterKind(Enum):
    """All implemented forecaster kinds."""
    
    Q_FORECAST = "q-forecast"
    BAYES = "bayes"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class OptimizationAggregatorKind(Enum):
    """All implemented ways to aggregate historic data."""
    
    UNIFORM = "uniform"
    EXPONENTIAL = "exponential"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class OptimizationMaximizerKind(Enum):
    """All implemented revenue maximization algorithms."""
    
    DP_QSD = "qsd"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class OptimizationEffectsKind(Enum):
    """All implemented post-optimization effects."""
    
    NONE = "none"
    COMMIT_THRESHOLDS = "commit"

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]

class ParametricFilterClassKind(Enum):
    """All implemented filter class kinds."""
    
    IN_PERIOD = 'in_period'
    FLIGHT_NUMBER = 'flight_number'
    AIRLINE = 'airline'
    SECTOR = 'sector'
    ROUTE = 'route'
    CITYSECTOR = 'citysector'
    CITYROUTE = 'cityroute'
    NETWORK = 'network'

    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]