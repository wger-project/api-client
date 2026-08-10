from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.log_item import LogItem
from ...models.log_item_request import LogItemRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: LogItemRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/nutritiondiary/",
    }

    if isinstance(body, LogItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, LogItemRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, LogItemRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LogItem | None:
    if response.status_code == 201:
        response_201 = LogItem.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LogItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LogItemRequest | Unset = UNSET,
) -> Response[LogItem]:
    """API endpoint for a meal log item

    Args:
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogItem]
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
    body: LogItemRequest | Unset = UNSET,
) -> LogItem | None:
    """API endpoint for a meal log item

    Args:
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogItem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LogItemRequest | Unset = UNSET,
) -> Response[LogItem]:
    """API endpoint for a meal log item

    Args:
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogItem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LogItemRequest | Unset = UNSET,
) -> LogItem | None:
    """API endpoint for a meal log item

    Args:
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer
        body (LogItemRequest): LogItem serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogItem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
