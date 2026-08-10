import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_weight_entry_list import PaginatedWeightEntryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_date_gt: str | Unset = UNSET
    if not isinstance(date_gt, Unset):
        json_date_gt = date_gt.isoformat()
    params["date__gt"] = json_date_gt

    json_date_gte: str | Unset = UNSET
    if not isinstance(date_gte, Unset):
        json_date_gte = date_gte.isoformat()
    params["date__gte"] = json_date_gte

    json_date_lt: str | Unset = UNSET
    if not isinstance(date_lt, Unset):
        json_date_lt = date_lt.isoformat()
    params["date__lt"] = json_date_lt

    json_date_lte: str | Unset = UNSET
    if not isinstance(date_lte, Unset):
        json_date_lte = date_lte.isoformat()
    params["date__lte"] = json_date_lte

    params["id"] = id

    json_id_in: list[int] | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = id_in

    params["id__in"] = json_id_in

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["weight"] = weight

    params["weight__gt"] = weight_gt

    params["weight__gte"] = weight_gte

    params["weight__lt"] = weight_lt

    params["weight__lte"] = weight_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/weightentry/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedWeightEntryList | None:
    if response.status_code == 200:
        response_200 = PaginatedWeightEntryList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedWeightEntryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
) -> Response[PaginatedWeightEntryList]:
    """API endpoint for nutrition plan objects

    Args:
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWeightEntryList]
    """

    kwargs = _get_kwargs(
        date=date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        id=id,
        id_in=id_in,
        limit=limit,
        offset=offset,
        ordering=ordering,
        weight=weight,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
) -> PaginatedWeightEntryList | None:
    """API endpoint for nutrition plan objects

    Args:
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWeightEntryList
    """

    return sync_detailed(
        client=client,
        date=date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        id=id,
        id_in=id_in,
        limit=limit,
        offset=offset,
        ordering=ordering,
        weight=weight,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
) -> Response[PaginatedWeightEntryList]:
    """API endpoint for nutrition plan objects

    Args:
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWeightEntryList]
    """

    kwargs = _get_kwargs(
        date=date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        id=id,
        id_in=id_in,
        limit=limit,
        offset=offset,
        ordering=ordering,
        weight=weight,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
) -> PaginatedWeightEntryList | None:
    """API endpoint for nutrition plan objects

    Args:
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWeightEntryList
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            id=id,
            id_in=id_in,
            limit=limit,
            offset=offset,
            ordering=ordering,
            weight=weight,
            weight_gt=weight_gt,
            weight_gte=weight_gte,
            weight_lt=weight_lt,
            weight_lte=weight_lte,
        )
    ).parsed
