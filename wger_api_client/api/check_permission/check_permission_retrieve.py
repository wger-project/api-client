from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.permission_response import PermissionResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    permission: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["permission"] = permission

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/check-permission/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PermissionResponse | None:
    if response.status_code == 200:
        response_200 = PermissionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PermissionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    permission: str,
) -> Response[Any | PermissionResponse]:
    """Checks whether the user has a django permission

    Args:
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionResponse]
    """

    kwargs = _get_kwargs(
        permission=permission,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    permission: str,
) -> Any | PermissionResponse | None:
    """Checks whether the user has a django permission

    Args:
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionResponse
    """

    return sync_detailed(
        client=client,
        permission=permission,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    permission: str,
) -> Response[Any | PermissionResponse]:
    """Checks whether the user has a django permission

    Args:
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionResponse]
    """

    kwargs = _get_kwargs(
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    permission: str,
) -> Any | PermissionResponse | None:
    """Checks whether the user has a django permission

    Args:
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            permission=permission,
        )
    ).parsed
