from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category import Category
from ...models.category_request import CategoryRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CategoryRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/measurement-category/",
    }

    if isinstance(body, CategoryRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CategoryRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CategoryRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Category | None:
    if response.status_code == 201:
        response_201 = Category.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Category]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CategoryRequest | Unset = UNSET,
) -> Response[Category]:
    """API endpoint for measurement units

    Args:
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Category]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CategoryRequest | Unset = UNSET,
) -> Category | None:
    """API endpoint for measurement units

    Args:
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Category
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CategoryRequest | Unset = UNSET,
) -> Response[Category]:
    """API endpoint for measurement units

    Args:
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Category]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CategoryRequest | Unset = UNSET,
) -> Category | None:
    """API endpoint for measurement units

    Args:
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer
        body (CategoryRequest): Measurement category serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Category
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
