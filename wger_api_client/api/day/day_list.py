from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_day_list import PaginatedDayList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_rest: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    need_logs_to_advance: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["description"] = description

    params["id"] = id

    params["is_rest"] = is_rest

    params["limit"] = limit

    params["name"] = name

    params["need_logs_to_advance"] = need_logs_to_advance

    params["offset"] = offset

    params["order"] = order

    params["ordering"] = ordering

    params["routine"] = routine

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/day/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedDayList | None:
    if response.status_code == 200:
        response_200 = PaginatedDayList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedDayList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_rest: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    need_logs_to_advance: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> Response[PaginatedDayList]:
    """API endpoint for routine day objects

    Args:
        description (str | Unset):
        id (int | Unset):
        is_rest (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        need_logs_to_advance (bool | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDayList]
    """

    kwargs = _get_kwargs(
        description=description,
        id=id,
        is_rest=is_rest,
        limit=limit,
        name=name,
        need_logs_to_advance=need_logs_to_advance,
        offset=offset,
        order=order,
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
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_rest: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    need_logs_to_advance: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> PaginatedDayList | None:
    """API endpoint for routine day objects

    Args:
        description (str | Unset):
        id (int | Unset):
        is_rest (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        need_logs_to_advance (bool | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDayList
    """

    return sync_detailed(
        client=client,
        description=description,
        id=id,
        is_rest=is_rest,
        limit=limit,
        name=name,
        need_logs_to_advance=need_logs_to_advance,
        offset=offset,
        order=order,
        ordering=ordering,
        routine=routine,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_rest: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    need_logs_to_advance: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> Response[PaginatedDayList]:
    """API endpoint for routine day objects

    Args:
        description (str | Unset):
        id (int | Unset):
        is_rest (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        need_logs_to_advance (bool | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDayList]
    """

    kwargs = _get_kwargs(
        description=description,
        id=id,
        is_rest=is_rest,
        limit=limit,
        name=name,
        need_logs_to_advance=need_logs_to_advance,
        offset=offset,
        order=order,
        ordering=ordering,
        routine=routine,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_rest: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    need_logs_to_advance: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    routine: int | Unset = UNSET,
) -> PaginatedDayList | None:
    """API endpoint for routine day objects

    Args:
        description (str | Unset):
        id (int | Unset):
        is_rest (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        need_logs_to_advance (bool | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        routine (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDayList
    """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
            id=id,
            is_rest=is_rest,
            limit=limit,
            name=name,
            need_logs_to_advance=need_logs_to_advance,
            offset=offset,
            order=order,
            ordering=ordering,
            routine=routine,
        )
    ).parsed
