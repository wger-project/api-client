from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.max_repetitions_config import MaxRepetitionsConfig
from ...models.max_repetitions_config_request import MaxRepetitionsConfigRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: MaxRepetitionsConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/max-repetitions-config/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MaxRepetitionsConfig | None:
    if response.status_code == 200:
        response_200 = MaxRepetitionsConfig.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MaxRepetitionsConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: MaxRepetitionsConfigRequest,
) -> Response[MaxRepetitionsConfig]:
    """API endpoint for max reps config objects

    Args:
        id (int):
        body (MaxRepetitionsConfigRequest): Max Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaxRepetitionsConfig]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: MaxRepetitionsConfigRequest,
) -> MaxRepetitionsConfig | None:
    """API endpoint for max reps config objects

    Args:
        id (int):
        body (MaxRepetitionsConfigRequest): Max Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaxRepetitionsConfig
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: MaxRepetitionsConfigRequest,
) -> Response[MaxRepetitionsConfig]:
    """API endpoint for max reps config objects

    Args:
        id (int):
        body (MaxRepetitionsConfigRequest): Max Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaxRepetitionsConfig]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: MaxRepetitionsConfigRequest,
) -> MaxRepetitionsConfig | None:
    """API endpoint for max reps config objects

    Args:
        id (int):
        body (MaxRepetitionsConfigRequest): Max Repetition Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaxRepetitionsConfig
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
