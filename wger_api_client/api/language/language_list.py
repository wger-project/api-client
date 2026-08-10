from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_language_list import PaginatedLanguageList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    full_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    short_name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["full_name"] = full_name

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["short_name"] = short_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/language/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedLanguageList | None:
    if response.status_code == 200:
        response_200 = PaginatedLanguageList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedLanguageList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    full_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    short_name: str | Unset = UNSET,
) -> Response[PaginatedLanguageList]:
    """API endpoint for the languages used in the application

    Args:
        full_name (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        short_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLanguageList]
    """

    kwargs = _get_kwargs(
        full_name=full_name,
        limit=limit,
        offset=offset,
        ordering=ordering,
        short_name=short_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    full_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    short_name: str | Unset = UNSET,
) -> PaginatedLanguageList | None:
    """API endpoint for the languages used in the application

    Args:
        full_name (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        short_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLanguageList
    """

    return sync_detailed(
        client=client,
        full_name=full_name,
        limit=limit,
        offset=offset,
        ordering=ordering,
        short_name=short_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    full_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    short_name: str | Unset = UNSET,
) -> Response[PaginatedLanguageList]:
    """API endpoint for the languages used in the application

    Args:
        full_name (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        short_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLanguageList]
    """

    kwargs = _get_kwargs(
        full_name=full_name,
        limit=limit,
        offset=offset,
        ordering=ordering,
        short_name=short_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    full_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    short_name: str | Unset = UNSET,
) -> PaginatedLanguageList | None:
    """API endpoint for the languages used in the application

    Args:
        full_name (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        short_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLanguageList
    """

    return (
        await asyncio_detailed(
            client=client,
            full_name=full_name,
            limit=limit,
            offset=offset,
            ordering=ordering,
            short_name=short_name,
        )
    ).parsed
