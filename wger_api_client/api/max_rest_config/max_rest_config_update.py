from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.max_rest_config import MaxRestConfig
from ...models.max_rest_config_request import MaxRestConfigRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: MaxRestConfigRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/max-rest-config/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, MaxRestConfigRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MaxRestConfigRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, MaxRestConfigRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MaxRestConfig | None:
    if response.status_code == 200:
        response_200 = MaxRestConfig.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MaxRestConfig]:
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
    body: MaxRestConfigRequest | Unset = UNSET,
) -> Response[MaxRestConfig]:
    """API endpoint for max rest config objects

    Args:
        id (int):
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaxRestConfig]
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
    body: MaxRestConfigRequest | Unset = UNSET,
) -> MaxRestConfig | None:
    """API endpoint for max rest config objects

    Args:
        id (int):
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaxRestConfig
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
    body: MaxRestConfigRequest | Unset = UNSET,
) -> Response[MaxRestConfig]:
    """API endpoint for max rest config objects

    Args:
        id (int):
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaxRestConfig]
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
    body: MaxRestConfigRequest | Unset = UNSET,
) -> MaxRestConfig | None:
    """API endpoint for max rest config objects

    Args:
        id (int):
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer
        body (MaxRestConfigRequest): Rest Config serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaxRestConfig
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
