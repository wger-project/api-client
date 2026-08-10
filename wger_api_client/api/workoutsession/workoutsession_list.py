import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_workout_session_list import PaginatedWorkoutSessionList
from ...models.workoutsession_list_general_impression import (
    WorkoutsessionListGeneralImpression,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_impression: str | Unset = UNSET
    if not isinstance(impression, Unset):
        json_impression = impression.value

    params["impression"] = json_impression

    params["limit"] = limit

    params["notes"] = notes

    params["offset"] = offset

    params["ordering"] = ordering

    params["routine"] = routine

    params["time_end"] = time_end

    params["time_start"] = time_start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/workoutsession/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedWorkoutSessionList | None:
    if response.status_code == 200:
        response_200 = PaginatedWorkoutSessionList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedWorkoutSessionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> Response[PaginatedWorkoutSessionList]:
    """API endpoint for workout sessions objects

    Args:
        date (datetime.date | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkoutSessionList]
    """

    kwargs = _get_kwargs(
        date=date,
        impression=impression,
        limit=limit,
        notes=notes,
        offset=offset,
        ordering=ordering,
        routine=routine,
        time_end=time_end,
        time_start=time_start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> PaginatedWorkoutSessionList | None:
    """API endpoint for workout sessions objects

    Args:
        date (datetime.date | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkoutSessionList
    """

    return sync_detailed(
        client=client,
        date=date,
        impression=impression,
        limit=limit,
        notes=notes,
        offset=offset,
        ordering=ordering,
        routine=routine,
        time_end=time_end,
        time_start=time_start,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> Response[PaginatedWorkoutSessionList]:
    """API endpoint for workout sessions objects

    Args:
        date (datetime.date | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkoutSessionList]
    """

    kwargs = _get_kwargs(
        date=date,
        impression=impression,
        limit=limit,
        notes=notes,
        offset=offset,
        ordering=ordering,
        routine=routine,
        time_end=time_end,
        time_start=time_start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
    time_end: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
) -> PaginatedWorkoutSessionList | None:
    """API endpoint for workout sessions objects

    Args:
        date (datetime.date | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):
        time_end (str | Unset):
        time_start (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkoutSessionList
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            impression=impression,
            limit=limit,
            notes=notes,
            offset=offset,
            ordering=ordering,
            routine=routine,
            time_end=time_end,
            time_start=time_start,
        )
    ).parsed
