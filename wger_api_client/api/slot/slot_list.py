from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_slot_list import PaginatedSlotList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    comment: str | Unset = UNSET,
    day: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["comment"] = comment

    params["day"] = day

    params["limit"] = limit

    params["offset"] = offset

    params["order"] = order

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/slot/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedSlotList | None:
    if response.status_code == 200:
        response_200 = PaginatedSlotList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedSlotList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    day: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedSlotList]:
    """API endpoint for routine slot objects

    Args:
        comment (str | Unset):
        day (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSlotList]
    """

    kwargs = _get_kwargs(
        comment=comment,
        day=day,
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    day: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedSlotList | None:
    """API endpoint for routine slot objects

    Args:
        comment (str | Unset):
        day (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSlotList
    """

    return sync_detailed(
        client=client,
        comment=comment,
        day=day,
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    day: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedSlotList]:
    """API endpoint for routine slot objects

    Args:
        comment (str | Unset):
        day (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSlotList]
    """

    kwargs = _get_kwargs(
        comment=comment,
        day=day,
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    day: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedSlotList | None:
    """API endpoint for routine slot objects

    Args:
        comment (str | Unset):
        day (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSlotList
    """

    return (
        await asyncio_detailed(
            client=client,
            comment=comment,
            day=day,
            limit=limit,
            offset=offset,
            order=order,
            ordering=ordering,
        )
    ).parsed
