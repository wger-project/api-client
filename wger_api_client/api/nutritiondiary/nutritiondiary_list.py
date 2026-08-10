import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_log_item_list import PaginatedLogItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    amount: float | Unset = UNSET,
    datetime_: datetime.datetime | Unset = UNSET,
    datetime_date: datetime.date | Unset = UNSET,
    datetime_gt: datetime.datetime | Unset = UNSET,
    datetime_gte: datetime.datetime | Unset = UNSET,
    datetime_lt: datetime.datetime | Unset = UNSET,
    datetime_lte: datetime.datetime | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["amount"] = amount

    json_datetime_: str | Unset = UNSET
    if not isinstance(datetime_, Unset):
        json_datetime_ = datetime_.isoformat()
    params["datetime"] = json_datetime_

    json_datetime_date: str | Unset = UNSET
    if not isinstance(datetime_date, Unset):
        json_datetime_date = datetime_date.isoformat()
    params["datetime__date"] = json_datetime_date

    json_datetime_gt: str | Unset = UNSET
    if not isinstance(datetime_gt, Unset):
        json_datetime_gt = datetime_gt.isoformat()
    params["datetime__gt"] = json_datetime_gt

    json_datetime_gte: str | Unset = UNSET
    if not isinstance(datetime_gte, Unset):
        json_datetime_gte = datetime_gte.isoformat()
    params["datetime__gte"] = json_datetime_gte

    json_datetime_lt: str | Unset = UNSET
    if not isinstance(datetime_lt, Unset):
        json_datetime_lt = datetime_lt.isoformat()
    params["datetime__lt"] = json_datetime_lt

    json_datetime_lte: str | Unset = UNSET
    if not isinstance(datetime_lte, Unset):
        json_datetime_lte = datetime_lte.isoformat()
    params["datetime__lte"] = json_datetime_lte

    params["ingredient"] = ingredient

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    json_plan: str | Unset = UNSET
    if not isinstance(plan, Unset):
        json_plan = str(plan)
    params["plan"] = json_plan

    params["weight_unit"] = weight_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/nutritiondiary/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedLogItemList | None:
    if response.status_code == 200:
        response_200 = PaginatedLogItemList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedLogItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    datetime_: datetime.datetime | Unset = UNSET,
    datetime_date: datetime.date | Unset = UNSET,
    datetime_gt: datetime.datetime | Unset = UNSET,
    datetime_gte: datetime.datetime | Unset = UNSET,
    datetime_lt: datetime.datetime | Unset = UNSET,
    datetime_lte: datetime.datetime | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> Response[PaginatedLogItemList]:
    """API endpoint for a meal log item

    Args:
        amount (float | Unset):
        datetime_ (datetime.datetime | Unset):
        datetime_date (datetime.date | Unset):
        datetime_gt (datetime.datetime | Unset):
        datetime_gte (datetime.datetime | Unset):
        datetime_lt (datetime.datetime | Unset):
        datetime_lte (datetime.datetime | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLogItemList]
    """

    kwargs = _get_kwargs(
        amount=amount,
        datetime_=datetime_,
        datetime_date=datetime_date,
        datetime_gt=datetime_gt,
        datetime_gte=datetime_gte,
        datetime_lt=datetime_lt,
        datetime_lte=datetime_lte,
        ingredient=ingredient,
        limit=limit,
        offset=offset,
        ordering=ordering,
        plan=plan,
        weight_unit=weight_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    datetime_: datetime.datetime | Unset = UNSET,
    datetime_date: datetime.date | Unset = UNSET,
    datetime_gt: datetime.datetime | Unset = UNSET,
    datetime_gte: datetime.datetime | Unset = UNSET,
    datetime_lt: datetime.datetime | Unset = UNSET,
    datetime_lte: datetime.datetime | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> PaginatedLogItemList | None:
    """API endpoint for a meal log item

    Args:
        amount (float | Unset):
        datetime_ (datetime.datetime | Unset):
        datetime_date (datetime.date | Unset):
        datetime_gt (datetime.datetime | Unset):
        datetime_gte (datetime.datetime | Unset):
        datetime_lt (datetime.datetime | Unset):
        datetime_lte (datetime.datetime | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLogItemList
    """

    return sync_detailed(
        client=client,
        amount=amount,
        datetime_=datetime_,
        datetime_date=datetime_date,
        datetime_gt=datetime_gt,
        datetime_gte=datetime_gte,
        datetime_lt=datetime_lt,
        datetime_lte=datetime_lte,
        ingredient=ingredient,
        limit=limit,
        offset=offset,
        ordering=ordering,
        plan=plan,
        weight_unit=weight_unit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    datetime_: datetime.datetime | Unset = UNSET,
    datetime_date: datetime.date | Unset = UNSET,
    datetime_gt: datetime.datetime | Unset = UNSET,
    datetime_gte: datetime.datetime | Unset = UNSET,
    datetime_lt: datetime.datetime | Unset = UNSET,
    datetime_lte: datetime.datetime | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> Response[PaginatedLogItemList]:
    """API endpoint for a meal log item

    Args:
        amount (float | Unset):
        datetime_ (datetime.datetime | Unset):
        datetime_date (datetime.date | Unset):
        datetime_gt (datetime.datetime | Unset):
        datetime_gte (datetime.datetime | Unset):
        datetime_lt (datetime.datetime | Unset):
        datetime_lte (datetime.datetime | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLogItemList]
    """

    kwargs = _get_kwargs(
        amount=amount,
        datetime_=datetime_,
        datetime_date=datetime_date,
        datetime_gt=datetime_gt,
        datetime_gte=datetime_gte,
        datetime_lt=datetime_lt,
        datetime_lte=datetime_lte,
        ingredient=ingredient,
        limit=limit,
        offset=offset,
        ordering=ordering,
        plan=plan,
        weight_unit=weight_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    datetime_: datetime.datetime | Unset = UNSET,
    datetime_date: datetime.date | Unset = UNSET,
    datetime_gt: datetime.datetime | Unset = UNSET,
    datetime_gte: datetime.datetime | Unset = UNSET,
    datetime_lt: datetime.datetime | Unset = UNSET,
    datetime_lte: datetime.datetime | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> PaginatedLogItemList | None:
    """API endpoint for a meal log item

    Args:
        amount (float | Unset):
        datetime_ (datetime.datetime | Unset):
        datetime_date (datetime.date | Unset):
        datetime_gt (datetime.datetime | Unset):
        datetime_gte (datetime.datetime | Unset):
        datetime_lt (datetime.datetime | Unset):
        datetime_lte (datetime.datetime | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLogItemList
    """

    return (
        await asyncio_detailed(
            client=client,
            amount=amount,
            datetime_=datetime_,
            datetime_date=datetime_date,
            datetime_gt=datetime_gt,
            datetime_gte=datetime_gte,
            datetime_lt=datetime_lt,
            datetime_lte=datetime_lte,
            ingredient=ingredient,
            limit=limit,
            offset=offset,
            ordering=ordering,
            plan=plan,
            weight_unit=weight_unit,
        )
    ).parsed
