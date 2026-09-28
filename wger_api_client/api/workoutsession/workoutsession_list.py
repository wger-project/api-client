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
    datetime_end: datetime.datetime | Unset = UNSET,
    datetime_end_date: datetime.date | Unset = UNSET,
    datetime_end_gt: datetime.datetime | Unset = UNSET,
    datetime_end_gte: datetime.datetime | Unset = UNSET,
    datetime_end_lt: datetime.datetime | Unset = UNSET,
    datetime_end_lte: datetime.datetime | Unset = UNSET,
    datetime_start: datetime.datetime | Unset = UNSET,
    datetime_start_date: datetime.date | Unset = UNSET,
    datetime_start_gt: datetime.datetime | Unset = UNSET,
    datetime_start_gte: datetime.datetime | Unset = UNSET,
    datetime_start_lt: datetime.datetime | Unset = UNSET,
    datetime_start_lte: datetime.datetime | Unset = UNSET,
    day: int | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_datetime_end: str | Unset = UNSET
    if not isinstance(datetime_end, Unset):
        json_datetime_end = datetime_end.isoformat()
    params["datetime_end"] = json_datetime_end

    json_datetime_end_date: str | Unset = UNSET
    if not isinstance(datetime_end_date, Unset):
        json_datetime_end_date = datetime_end_date.isoformat()
    params["datetime_end__date"] = json_datetime_end_date

    json_datetime_end_gt: str | Unset = UNSET
    if not isinstance(datetime_end_gt, Unset):
        json_datetime_end_gt = datetime_end_gt.isoformat()
    params["datetime_end__gt"] = json_datetime_end_gt

    json_datetime_end_gte: str | Unset = UNSET
    if not isinstance(datetime_end_gte, Unset):
        json_datetime_end_gte = datetime_end_gte.isoformat()
    params["datetime_end__gte"] = json_datetime_end_gte

    json_datetime_end_lt: str | Unset = UNSET
    if not isinstance(datetime_end_lt, Unset):
        json_datetime_end_lt = datetime_end_lt.isoformat()
    params["datetime_end__lt"] = json_datetime_end_lt

    json_datetime_end_lte: str | Unset = UNSET
    if not isinstance(datetime_end_lte, Unset):
        json_datetime_end_lte = datetime_end_lte.isoformat()
    params["datetime_end__lte"] = json_datetime_end_lte

    json_datetime_start: str | Unset = UNSET
    if not isinstance(datetime_start, Unset):
        json_datetime_start = datetime_start.isoformat()
    params["datetime_start"] = json_datetime_start

    json_datetime_start_date: str | Unset = UNSET
    if not isinstance(datetime_start_date, Unset):
        json_datetime_start_date = datetime_start_date.isoformat()
    params["datetime_start__date"] = json_datetime_start_date

    json_datetime_start_gt: str | Unset = UNSET
    if not isinstance(datetime_start_gt, Unset):
        json_datetime_start_gt = datetime_start_gt.isoformat()
    params["datetime_start__gt"] = json_datetime_start_gt

    json_datetime_start_gte: str | Unset = UNSET
    if not isinstance(datetime_start_gte, Unset):
        json_datetime_start_gte = datetime_start_gte.isoformat()
    params["datetime_start__gte"] = json_datetime_start_gte

    json_datetime_start_lt: str | Unset = UNSET
    if not isinstance(datetime_start_lt, Unset):
        json_datetime_start_lt = datetime_start_lt.isoformat()
    params["datetime_start__lt"] = json_datetime_start_lt

    json_datetime_start_lte: str | Unset = UNSET
    if not isinstance(datetime_start_lte, Unset):
        json_datetime_start_lte = datetime_start_lte.isoformat()
    params["datetime_start__lte"] = json_datetime_start_lte

    params["day"] = day

    json_impression: str | Unset = UNSET
    if not isinstance(impression, Unset):
        json_impression = impression

    params["impression"] = json_impression

    params["limit"] = limit

    params["notes"] = notes

    params["offset"] = offset

    params["ordering"] = ordering

    params["routine"] = routine

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
    datetime_end: datetime.datetime | Unset = UNSET,
    datetime_end_date: datetime.date | Unset = UNSET,
    datetime_end_gt: datetime.datetime | Unset = UNSET,
    datetime_end_gte: datetime.datetime | Unset = UNSET,
    datetime_end_lt: datetime.datetime | Unset = UNSET,
    datetime_end_lte: datetime.datetime | Unset = UNSET,
    datetime_start: datetime.datetime | Unset = UNSET,
    datetime_start_date: datetime.date | Unset = UNSET,
    datetime_start_gt: datetime.datetime | Unset = UNSET,
    datetime_start_gte: datetime.datetime | Unset = UNSET,
    datetime_start_lt: datetime.datetime | Unset = UNSET,
    datetime_start_lte: datetime.datetime | Unset = UNSET,
    day: int | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> Response[PaginatedWorkoutSessionList]:
    """API endpoint for workout sessions objects

    Args:
        datetime_end (datetime.datetime | Unset):
        datetime_end_date (datetime.date | Unset):
        datetime_end_gt (datetime.datetime | Unset):
        datetime_end_gte (datetime.datetime | Unset):
        datetime_end_lt (datetime.datetime | Unset):
        datetime_end_lte (datetime.datetime | Unset):
        datetime_start (datetime.datetime | Unset):
        datetime_start_date (datetime.date | Unset):
        datetime_start_gt (datetime.datetime | Unset):
        datetime_start_gte (datetime.datetime | Unset):
        datetime_start_lt (datetime.datetime | Unset):
        datetime_start_lte (datetime.datetime | Unset):
        day (int | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkoutSessionList]
    """

    kwargs = _get_kwargs(
        datetime_end=datetime_end,
        datetime_end_date=datetime_end_date,
        datetime_end_gt=datetime_end_gt,
        datetime_end_gte=datetime_end_gte,
        datetime_end_lt=datetime_end_lt,
        datetime_end_lte=datetime_end_lte,
        datetime_start=datetime_start,
        datetime_start_date=datetime_start_date,
        datetime_start_gt=datetime_start_gt,
        datetime_start_gte=datetime_start_gte,
        datetime_start_lt=datetime_start_lt,
        datetime_start_lte=datetime_start_lte,
        day=day,
        impression=impression,
        limit=limit,
        notes=notes,
        offset=offset,
        ordering=ordering,
        routine=routine,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    datetime_end: datetime.datetime | Unset = UNSET,
    datetime_end_date: datetime.date | Unset = UNSET,
    datetime_end_gt: datetime.datetime | Unset = UNSET,
    datetime_end_gte: datetime.datetime | Unset = UNSET,
    datetime_end_lt: datetime.datetime | Unset = UNSET,
    datetime_end_lte: datetime.datetime | Unset = UNSET,
    datetime_start: datetime.datetime | Unset = UNSET,
    datetime_start_date: datetime.date | Unset = UNSET,
    datetime_start_gt: datetime.datetime | Unset = UNSET,
    datetime_start_gte: datetime.datetime | Unset = UNSET,
    datetime_start_lt: datetime.datetime | Unset = UNSET,
    datetime_start_lte: datetime.datetime | Unset = UNSET,
    day: int | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> PaginatedWorkoutSessionList | None:
    """API endpoint for workout sessions objects

    Args:
        datetime_end (datetime.datetime | Unset):
        datetime_end_date (datetime.date | Unset):
        datetime_end_gt (datetime.datetime | Unset):
        datetime_end_gte (datetime.datetime | Unset):
        datetime_end_lt (datetime.datetime | Unset):
        datetime_end_lte (datetime.datetime | Unset):
        datetime_start (datetime.datetime | Unset):
        datetime_start_date (datetime.date | Unset):
        datetime_start_gt (datetime.datetime | Unset):
        datetime_start_gte (datetime.datetime | Unset):
        datetime_start_lt (datetime.datetime | Unset):
        datetime_start_lte (datetime.datetime | Unset):
        day (int | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkoutSessionList
    """

    return sync_detailed(
        client=client,
        datetime_end=datetime_end,
        datetime_end_date=datetime_end_date,
        datetime_end_gt=datetime_end_gt,
        datetime_end_gte=datetime_end_gte,
        datetime_end_lt=datetime_end_lt,
        datetime_end_lte=datetime_end_lte,
        datetime_start=datetime_start,
        datetime_start_date=datetime_start_date,
        datetime_start_gt=datetime_start_gt,
        datetime_start_gte=datetime_start_gte,
        datetime_start_lt=datetime_start_lt,
        datetime_start_lte=datetime_start_lte,
        day=day,
        impression=impression,
        limit=limit,
        notes=notes,
        offset=offset,
        ordering=ordering,
        routine=routine,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    datetime_end: datetime.datetime | Unset = UNSET,
    datetime_end_date: datetime.date | Unset = UNSET,
    datetime_end_gt: datetime.datetime | Unset = UNSET,
    datetime_end_gte: datetime.datetime | Unset = UNSET,
    datetime_end_lt: datetime.datetime | Unset = UNSET,
    datetime_end_lte: datetime.datetime | Unset = UNSET,
    datetime_start: datetime.datetime | Unset = UNSET,
    datetime_start_date: datetime.date | Unset = UNSET,
    datetime_start_gt: datetime.datetime | Unset = UNSET,
    datetime_start_gte: datetime.datetime | Unset = UNSET,
    datetime_start_lt: datetime.datetime | Unset = UNSET,
    datetime_start_lte: datetime.datetime | Unset = UNSET,
    day: int | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> Response[PaginatedWorkoutSessionList]:
    """API endpoint for workout sessions objects

    Args:
        datetime_end (datetime.datetime | Unset):
        datetime_end_date (datetime.date | Unset):
        datetime_end_gt (datetime.datetime | Unset):
        datetime_end_gte (datetime.datetime | Unset):
        datetime_end_lt (datetime.datetime | Unset):
        datetime_end_lte (datetime.datetime | Unset):
        datetime_start (datetime.datetime | Unset):
        datetime_start_date (datetime.date | Unset):
        datetime_start_gt (datetime.datetime | Unset):
        datetime_start_gte (datetime.datetime | Unset):
        datetime_start_lt (datetime.datetime | Unset):
        datetime_start_lte (datetime.datetime | Unset):
        day (int | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkoutSessionList]
    """

    kwargs = _get_kwargs(
        datetime_end=datetime_end,
        datetime_end_date=datetime_end_date,
        datetime_end_gt=datetime_end_gt,
        datetime_end_gte=datetime_end_gte,
        datetime_end_lt=datetime_end_lt,
        datetime_end_lte=datetime_end_lte,
        datetime_start=datetime_start,
        datetime_start_date=datetime_start_date,
        datetime_start_gt=datetime_start_gt,
        datetime_start_gte=datetime_start_gte,
        datetime_start_lt=datetime_start_lt,
        datetime_start_lte=datetime_start_lte,
        day=day,
        impression=impression,
        limit=limit,
        notes=notes,
        offset=offset,
        ordering=ordering,
        routine=routine,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    datetime_end: datetime.datetime | Unset = UNSET,
    datetime_end_date: datetime.date | Unset = UNSET,
    datetime_end_gt: datetime.datetime | Unset = UNSET,
    datetime_end_gte: datetime.datetime | Unset = UNSET,
    datetime_end_lt: datetime.datetime | Unset = UNSET,
    datetime_end_lte: datetime.datetime | Unset = UNSET,
    datetime_start: datetime.datetime | Unset = UNSET,
    datetime_start_date: datetime.date | Unset = UNSET,
    datetime_start_gt: datetime.datetime | Unset = UNSET,
    datetime_start_gte: datetime.datetime | Unset = UNSET,
    datetime_start_lt: datetime.datetime | Unset = UNSET,
    datetime_start_lte: datetime.datetime | Unset = UNSET,
    day: int | Unset = UNSET,
    impression: WorkoutsessionListGeneralImpression | Unset = UNSET,
    limit: int | Unset = UNSET,
    notes: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> PaginatedWorkoutSessionList | None:
    """API endpoint for workout sessions objects

    Args:
        datetime_end (datetime.datetime | Unset):
        datetime_end_date (datetime.date | Unset):
        datetime_end_gt (datetime.datetime | Unset):
        datetime_end_gte (datetime.datetime | Unset):
        datetime_end_lt (datetime.datetime | Unset):
        datetime_end_lte (datetime.datetime | Unset):
        datetime_start (datetime.datetime | Unset):
        datetime_start_date (datetime.date | Unset):
        datetime_start_gt (datetime.datetime | Unset):
        datetime_start_gte (datetime.datetime | Unset):
        datetime_start_lt (datetime.datetime | Unset):
        datetime_start_lte (datetime.datetime | Unset):
        day (int | Unset):
        impression (WorkoutsessionListGeneralImpression | Unset):
        limit (int | Unset):
        notes (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkoutSessionList
    """

    return (
        await asyncio_detailed(
            client=client,
            datetime_end=datetime_end,
            datetime_end_date=datetime_end_date,
            datetime_end_gt=datetime_end_gt,
            datetime_end_gte=datetime_end_gte,
            datetime_end_lt=datetime_end_lt,
            datetime_end_lte=datetime_end_lte,
            datetime_start=datetime_start,
            datetime_start_date=datetime_start_date,
            datetime_start_gt=datetime_start_gt,
            datetime_start_gte=datetime_start_gte,
            datetime_start_lt=datetime_start_lt,
            datetime_start_lte=datetime_start_lte,
            day=day,
            impression=impression,
            limit=limit,
            notes=notes,
            offset=offset,
            ordering=ordering,
            routine=routine,
        )
    ).parsed
