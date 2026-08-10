import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_routine_list import PaginatedRoutineList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_created: str | Unset = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["description"] = description

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/templates/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedRoutineList | None:
    if response.status_code == 200:
        response_200 = PaginatedRoutineList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedRoutineList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedRoutineList]:
    """API endpoint for routine template objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRoutineList]
    """

    kwargs = _get_kwargs(
        created=created,
        description=description,
        limit=limit,
        name=name,
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
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedRoutineList | None:
    """API endpoint for routine template objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRoutineList
    """

    return sync_detailed(
        client=client,
        created=created,
        description=description,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedRoutineList]:
    """API endpoint for routine template objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRoutineList]
    """

    kwargs = _get_kwargs(
        created=created,
        description=description,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedRoutineList | None:
    """API endpoint for routine template objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRoutineList
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            description=description,
            limit=limit,
            name=name,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
