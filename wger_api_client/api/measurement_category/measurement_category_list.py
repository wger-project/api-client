from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_category_list import PaginatedCategoryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    unit: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: str | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = str(id)
    params["id"] = json_id

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["ordering"] = ordering

    params["unit"] = unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/measurement-category/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedCategoryList | None:
    if response.status_code == 200:
        response_200 = PaginatedCategoryList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedCategoryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    unit: str | Unset = UNSET,
) -> Response[PaginatedCategoryList]:
    """API endpoint for measurement units

    Args:
        id (UUID | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCategoryList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        unit=unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    unit: str | Unset = UNSET,
) -> PaginatedCategoryList | None:
    """API endpoint for measurement units

    Args:
        id (UUID | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCategoryList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        unit=unit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    unit: str | Unset = UNSET,
) -> Response[PaginatedCategoryList]:
    """API endpoint for measurement units

    Args:
        id (UUID | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCategoryList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        unit=unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    unit: str | Unset = UNSET,
) -> PaginatedCategoryList | None:
    """API endpoint for measurement units

    Args:
        id (UUID | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCategoryList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            name=name,
            offset=offset,
            ordering=ordering,
            unit=unit,
        )
    ).parsed
