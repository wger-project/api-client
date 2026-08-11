from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.repetitions_config import RepetitionsConfig
from ...models.repetitions_config_request import RepetitionsConfigRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RepetitionsConfigRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/repetitions-config/",
    }

    if isinstance(body, RepetitionsConfigRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RepetitionsConfigRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RepetitionsConfigRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RepetitionsConfig | None:
    if response.status_code == 201:
        response_201 = RepetitionsConfig.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RepetitionsConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RepetitionsConfigRequest | Unset = UNSET,
) -> Response[RepetitionsConfig]:
    """API endpoint for reps config objects

    Args:
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepetitionsConfig]
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
    body: RepetitionsConfigRequest | Unset = UNSET,
) -> RepetitionsConfig | None:
    """API endpoint for reps config objects

    Args:
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepetitionsConfig
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RepetitionsConfigRequest | Unset = UNSET,
) -> Response[RepetitionsConfig]:
    """API endpoint for reps config objects

    Args:
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepetitionsConfig]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RepetitionsConfigRequest | Unset = UNSET,
) -> RepetitionsConfig | None:
    """API endpoint for reps config objects

    Args:
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer
        body (RepetitionsConfigRequest): Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepetitionsConfig
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
