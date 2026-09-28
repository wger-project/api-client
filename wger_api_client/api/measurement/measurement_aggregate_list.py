import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bucket import Bucket
from ...models.measurement_aggregate_list_bucket import (
    MeasurementAggregateListBucket,
)
from ...models.measurement_aggregate_list_source import (
    MeasurementAggregateListSource,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bucket: MeasurementAggregateListBucket | Unset = UNSET,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    max_points: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    source: MeasurementAggregateListSource | Unset = UNSET,
    tz: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket

    params["bucket"] = json_bucket

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = str(category)
    params["category"] = json_category

    json_category_in: str | Unset = UNSET
    if not isinstance(category_in, Unset):
        json_category_in = ",".join(str(v) for v in category_in)

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

    json_id_in: str | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = ",".join(str(v) for v in id_in)

    params["id__in"] = json_id_in

    params["max_points"] = max_points

    params["ordering"] = ordering

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source

    params["source"] = json_source

    params["tz"] = tz

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/measurement/aggregate/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[Bucket] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Bucket.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[Bucket]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    bucket: MeasurementAggregateListBucket | Unset = UNSET,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    max_points: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    source: MeasurementAggregateListSource | Unset = UNSET,
    tz: str | Unset = UNSET,
) -> Response[list[Bucket]]:
    """Read the entries condensed into chart points

     The entries condensed into what a chart draws: one row per category,
    calendar bucket and stored unit.

    Takes the filters of the list endpoint (`category`, `category__in`,
    `date__gte`, ...) plus `bucket` (`auto`, the default, or one of hour,
    day, week, month), `tz` and `max_points`. A separate route rather than
    a mode of the list, because a bucket is not a measurement: it has no
    id, and nothing that reads measurements should have to tell them apart.

    Args:
        bucket (MeasurementAggregateListBucket | Unset):
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        max_points (int | Unset):
        ordering (str | Unset):
        source (MeasurementAggregateListSource | Unset):
        tz (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Bucket]]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        category=category,
        category_in=category_in,
        date=date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        id=id,
        id_in=id_in,
        max_points=max_points,
        ordering=ordering,
        source=source,
        tz=tz,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    bucket: MeasurementAggregateListBucket | Unset = UNSET,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    max_points: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    source: MeasurementAggregateListSource | Unset = UNSET,
    tz: str | Unset = UNSET,
) -> list[Bucket] | None:
    """Read the entries condensed into chart points

     The entries condensed into what a chart draws: one row per category,
    calendar bucket and stored unit.

    Takes the filters of the list endpoint (`category`, `category__in`,
    `date__gte`, ...) plus `bucket` (`auto`, the default, or one of hour,
    day, week, month), `tz` and `max_points`. A separate route rather than
    a mode of the list, because a bucket is not a measurement: it has no
    id, and nothing that reads measurements should have to tell them apart.

    Args:
        bucket (MeasurementAggregateListBucket | Unset):
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        max_points (int | Unset):
        ordering (str | Unset):
        source (MeasurementAggregateListSource | Unset):
        tz (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Bucket]
    """

    return sync_detailed(
        client=client,
        bucket=bucket,
        category=category,
        category_in=category_in,
        date=date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        id=id,
        id_in=id_in,
        max_points=max_points,
        ordering=ordering,
        source=source,
        tz=tz,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    bucket: MeasurementAggregateListBucket | Unset = UNSET,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    max_points: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    source: MeasurementAggregateListSource | Unset = UNSET,
    tz: str | Unset = UNSET,
) -> Response[list[Bucket]]:
    """Read the entries condensed into chart points

     The entries condensed into what a chart draws: one row per category,
    calendar bucket and stored unit.

    Takes the filters of the list endpoint (`category`, `category__in`,
    `date__gte`, ...) plus `bucket` (`auto`, the default, or one of hour,
    day, week, month), `tz` and `max_points`. A separate route rather than
    a mode of the list, because a bucket is not a measurement: it has no
    id, and nothing that reads measurements should have to tell them apart.

    Args:
        bucket (MeasurementAggregateListBucket | Unset):
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        max_points (int | Unset):
        ordering (str | Unset):
        source (MeasurementAggregateListSource | Unset):
        tz (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Bucket]]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        category=category,
        category_in=category_in,
        date=date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        id=id,
        id_in=id_in,
        max_points=max_points,
        ordering=ordering,
        source=source,
        tz=tz,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    bucket: MeasurementAggregateListBucket | Unset = UNSET,
    category: UUID | Unset = UNSET,
    category_in: list[UUID] | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    id: UUID | Unset = UNSET,
    id_in: list[UUID] | Unset = UNSET,
    max_points: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    source: MeasurementAggregateListSource | Unset = UNSET,
    tz: str | Unset = UNSET,
) -> list[Bucket] | None:
    """Read the entries condensed into chart points

     The entries condensed into what a chart draws: one row per category,
    calendar bucket and stored unit.

    Takes the filters of the list endpoint (`category`, `category__in`,
    `date__gte`, ...) plus `bucket` (`auto`, the default, or one of hour,
    day, week, month), `tz` and `max_points`. A separate route rather than
    a mode of the list, because a bucket is not a measurement: it has no
    id, and nothing that reads measurements should have to tell them apart.

    Args:
        bucket (MeasurementAggregateListBucket | Unset):
        category (UUID | Unset):
        category_in (list[UUID] | Unset):
        date (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        id (UUID | Unset):
        id_in (list[UUID] | Unset):
        max_points (int | Unset):
        ordering (str | Unset):
        source (MeasurementAggregateListSource | Unset):
        tz (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Bucket]
    """

    return (
        await asyncio_detailed(
            client=client,
            bucket=bucket,
            category=category,
            category_in=category_in,
            date=date,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            id=id,
            id_in=id_in,
            max_points=max_points,
            ordering=ordering,
            source=source,
            tz=tz,
        )
    ).parsed
