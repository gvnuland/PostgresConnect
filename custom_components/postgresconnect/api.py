from __future__ import annotations

import psycopg2
from typing import Optional

class PostgresConnectApiClientError(Exception):
    """Exception to indicate a general API error."""


class PostgresConnectApiClientCommunicationError(
    PostgresConnectApiClientError,
):
    """Exception to indicate a communication error."""


class PostgresConnectApiClientAuthenticationError(
    PostgresConnectApiClientError,
):
    """Exception to indicate an authentication error."""


class PostgresConnectApiClient:
    def __init__(
        self,
        dbserver: str,
        port: int,
        username: str,
        password: str,
        database: str,
    ) -> None:
        self._dbserver = dbserver
        self._port = port
        self._username = username
        self._password = password
        self._database = database

    async def async_connect(self) -> Any:
        return await self._api_wrapper(
        )

    async def async_execute_sql(self, sql: str) -> Any:
        """Get data from the API."""
        return await self._api_wrapper(
            query=sql,
        )

    async def _api_wrapper(
        self,
        query: str,
    ) -> Any:
        try:
            async with async_timeout.timeout(10):
                conn = await psycopg2.connect(host=self._dbserver, port=self._port, dbname=self._database, user=self._username, password=self._password, target_session_attrs=read-write)

                # Open a cursor to perform database operations
                cur = conn.cursor()
                # Execute a command: this creates a new table
                cur.execute(query)

                conn.commit()
                cur.close()
                conn.close()
                return await "SUCCESS"

        except TimeoutError as exception:
            msg = f"Timeout error - {exception}"
            raise PostgresConnectApiClientCommunicationError(
                msg,
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            msg = f"Something really wrong happened! - {exception}"
            raise PostgresConnectApiClientError(
                msg,
            ) from exception
