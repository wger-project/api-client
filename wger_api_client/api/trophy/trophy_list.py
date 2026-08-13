from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_trophy_list import PaginatedTrophyList
from ...models.trophy_list_trophy_type import (
    TrophyListTrophyType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_hidden: bool | Unset = UNSET,
    is_progressive: bool | Unset = UNSET,
    is_repeatable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy_type: TrophyListTrophyType | Unset = UNSET,
    trophy_type_in: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    json_id_in: str | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = ",".join(str(v) for v in id_in)

    params["id__in"] = json_id_in

    params["is_active"] = is_active

    params["is_hidden"] = is_hidden

    params["is_progressive"] = is_progressive

    params["is_repeatable"] = is_repeatable

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    json_trophy_type: str | Unset = UNSET
    if not isinstance(trophy_type, Unset):
        json_trophy_type = trophy_type

    params["trophy_type"] = json_trophy_type

    json_trophy_type_in: str | Unset = UNSET
    if not isinstance(trophy_type_in, Unset):
        json_trophy_type_in = ",".join(str(v) for v in trophy_type_in)

    params["trophy_type__in"] = json_trophy_type_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/trophy/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedTrophyList | None:
    if response.status_code == 200:
        response_200 = PaginatedTrophyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedTrophyList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_hidden: bool | Unset = UNSET,
    is_progressive: bool | Unset = UNSET,
    is_repeatable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy_type: TrophyListTrophyType | Unset = UNSET,
    trophy_type_in: list[str] | Unset = UNSET,
) -> Response[PaginatedTrophyList]:
    """API endpoint for Trophy objects.

    Returns active trophies. Hidden trophies are excluded unless:
    - The user has earned them, or
    - The user is staff

    list:
    Return a list of active trophies

    retrieve:
    Return a specific trophy by ID

    Args:
        id (int | Unset):
        id_in (list[int] | Unset):
        is_active (bool | Unset):
        is_hidden (bool | Unset):
        is_progressive (bool | Unset):
        is_repeatable (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy_type (TrophyListTrophyType | Unset):
        trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTrophyList]
    """

    kwargs = _get_kwargs(
        id=id,
        id_in=id_in,
        is_active=is_active,
        is_hidden=is_hidden,
        is_progressive=is_progressive,
        is_repeatable=is_repeatable,
        limit=limit,
        offset=offset,
        ordering=ordering,
        trophy_type=trophy_type,
        trophy_type_in=trophy_type_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_hidden: bool | Unset = UNSET,
    is_progressive: bool | Unset = UNSET,
    is_repeatable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy_type: TrophyListTrophyType | Unset = UNSET,
    trophy_type_in: list[str] | Unset = UNSET,
) -> PaginatedTrophyList | None:
    """API endpoint for Trophy objects.

    Returns active trophies. Hidden trophies are excluded unless:
    - The user has earned them, or
    - The user is staff

    list:
    Return a list of active trophies

    retrieve:
    Return a specific trophy by ID

    Args:
        id (int | Unset):
        id_in (list[int] | Unset):
        is_active (bool | Unset):
        is_hidden (bool | Unset):
        is_progressive (bool | Unset):
        is_repeatable (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy_type (TrophyListTrophyType | Unset):
        trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTrophyList
    """

    return sync_detailed(
        client=client,
        id=id,
        id_in=id_in,
        is_active=is_active,
        is_hidden=is_hidden,
        is_progressive=is_progressive,
        is_repeatable=is_repeatable,
        limit=limit,
        offset=offset,
        ordering=ordering,
        trophy_type=trophy_type,
        trophy_type_in=trophy_type_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_hidden: bool | Unset = UNSET,
    is_progressive: bool | Unset = UNSET,
    is_repeatable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy_type: TrophyListTrophyType | Unset = UNSET,
    trophy_type_in: list[str] | Unset = UNSET,
) -> Response[PaginatedTrophyList]:
    """API endpoint for Trophy objects.

    Returns active trophies. Hidden trophies are excluded unless:
    - The user has earned them, or
    - The user is staff

    list:
    Return a list of active trophies

    retrieve:
    Return a specific trophy by ID

    Args:
        id (int | Unset):
        id_in (list[int] | Unset):
        is_active (bool | Unset):
        is_hidden (bool | Unset):
        is_progressive (bool | Unset):
        is_repeatable (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy_type (TrophyListTrophyType | Unset):
        trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTrophyList]
    """

    kwargs = _get_kwargs(
        id=id,
        id_in=id_in,
        is_active=is_active,
        is_hidden=is_hidden,
        is_progressive=is_progressive,
        is_repeatable=is_repeatable,
        limit=limit,
        offset=offset,
        ordering=ordering,
        trophy_type=trophy_type,
        trophy_type_in=trophy_type_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_hidden: bool | Unset = UNSET,
    is_progressive: bool | Unset = UNSET,
    is_repeatable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy_type: TrophyListTrophyType | Unset = UNSET,
    trophy_type_in: list[str] | Unset = UNSET,
) -> PaginatedTrophyList | None:
    """API endpoint for Trophy objects.

    Returns active trophies. Hidden trophies are excluded unless:
    - The user has earned them, or
    - The user is staff

    list:
    Return a list of active trophies

    retrieve:
    Return a specific trophy by ID

    Args:
        id (int | Unset):
        id_in (list[int] | Unset):
        is_active (bool | Unset):
        is_hidden (bool | Unset):
        is_progressive (bool | Unset):
        is_repeatable (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy_type (TrophyListTrophyType | Unset):
        trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTrophyList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            id_in=id_in,
            is_active=is_active,
            is_hidden=is_hidden,
            is_progressive=is_progressive,
            is_repeatable=is_repeatable,
            limit=limit,
            offset=offset,
            ordering=ordering,
            trophy_type=trophy_type,
            trophy_type_in=trophy_type_in,
        )
    ).parsed
