from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.refresh_token_response import RefreshTokenResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/issue-refresh-token",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RefreshTokenResponse | None:
    if response.status_code == 200:
        response_200 = RefreshTokenResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RefreshTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RefreshTokenResponse]:
    """Temporary endpoint for issuing refresh tokens for authenticated users.

    This endpoint is used to allow users of the mobile app to seamlessly move from
    permanent tokens to JWT ones.

    TODO: remove one version after the iniial offline-mode release

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshTokenResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> RefreshTokenResponse | None:
    """Temporary endpoint for issuing refresh tokens for authenticated users.

    This endpoint is used to allow users of the mobile app to seamlessly move from
    permanent tokens to JWT ones.

    TODO: remove one version after the iniial offline-mode release

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshTokenResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RefreshTokenResponse]:
    """Temporary endpoint for issuing refresh tokens for authenticated users.

    This endpoint is used to allow users of the mobile app to seamlessly move from
    permanent tokens to JWT ones.

    TODO: remove one version after the iniial offline-mode release

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshTokenResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> RefreshTokenResponse | None:
    """Temporary endpoint for issuing refresh tokens for authenticated users.

    This endpoint is used to allow users of the mobile app to seamlessly move from
    permanent tokens to JWT ones.

    TODO: remove one version after the iniial offline-mode release

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
