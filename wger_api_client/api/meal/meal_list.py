from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_meal_list import PaginatedMealList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    time: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order"] = order

    params["ordering"] = ordering

    json_plan: str | Unset = UNSET
    if not isinstance(plan, Unset):
        json_plan = str(plan)
    params["plan"] = json_plan

    params["time"] = time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/meal/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedMealList | None:
    if response.status_code == 200:
        response_200 = PaginatedMealList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedMealList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    time: str | Unset = UNSET,
) -> Response[PaginatedMealList]:
    """API endpoint for meal objects

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMealList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
        plan=plan,
        time=time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    time: str | Unset = UNSET,
) -> PaginatedMealList | None:
    """API endpoint for meal objects

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMealList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
        plan=plan,
        time=time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    time: str | Unset = UNSET,
) -> Response[PaginatedMealList]:
    """API endpoint for meal objects

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMealList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
        plan=plan,
        time=time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    plan: UUID | Unset = UNSET,
    time: str | Unset = UNSET,
) -> PaginatedMealList | None:
    """API endpoint for meal objects

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        plan (UUID | Unset):
        time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMealList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order=order,
            ordering=ordering,
            plan=plan,
            time=time,
        )
    ).parsed
