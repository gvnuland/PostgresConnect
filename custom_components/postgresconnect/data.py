"""Custom types for integration_blueprint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import PostgresConnectApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type PostgresConnectConfigEntry = ConfigEntry[PostgresConnectData]


@dataclass
class PostgresConnectData:
    """Data for the Blueprint integration."""

    client: PostgresConnectApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
