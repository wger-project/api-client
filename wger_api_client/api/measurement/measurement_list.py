import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_measurement_list import PaginatedMeasurementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = str(category)
    params["category"] = json_category

    json_category_in: list[str] | Unset = UNSET
    if not isinstance(category_in, Unset):
        json_category_in = []
        for category_in_item_data in category_in:
            category_in_item = str(category_in_item_data)
            json_category_in.append(category_in_item)

    params["category__in"] = json_category_in

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

    json_id: str | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = str(id)
    params["id"] = json_id

    json_id_in: list[str] | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = []
        for id_in_item_data in id_in:
            id_in_item = str(id_in_item_data)
            json_id_in.append(id_in_item)

    params["id__in"] = json_id_in

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/measurement/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedMeasurementList | None:
    if response.status_code == 200:
        response_200 = PaginatedMeasurementList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedMeasurementList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedMeasurementList]:
    """API endpoint for measurements

    Args:
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMeasurementList]
    """

    kwargs = _get_kwargs(
        category=category,
        category_in=category_in,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedMeasurementList | None:
    """API endpoint for measurements

    Args:
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMeasurementList
    """

    return sync_detailed(
        client=client,
        category=category,
        category_in=category_in,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedMeasurementList]:
    """API endpoint for measurements

    Args:
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMeasurementList]
    """

    kwargs = _get_kwargs(
        category=category,
        category_in=category_in,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedMeasurementList | None:
    """API endpoint for measurements

    Args:
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMeasurementList
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            category_in=category_in,
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
        )
    ).parsed
