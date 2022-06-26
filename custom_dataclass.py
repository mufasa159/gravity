from dataclasses import dataclass


@dataclass(frozen=True)
class MFCount:
    active: int
    onsite: int
    remote: int


@dataclass(frozen=True)
class Person:
    name: str
    location: str


@dataclass(frozen=True)
class Worksite:
    name: str
    occupants: list[str]
    mf_capacity: int


@dataclass(frozen=True)
class DailyActive:
    day: int
    workplace: list[str]
    mf_active: int
    mf_onsite: int
    mf_remote: int


