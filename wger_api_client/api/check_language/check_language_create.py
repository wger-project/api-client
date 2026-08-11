from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.language_check_request import LanguageCheckRequest
from ...models.language_check_response import LanguageCheckResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LanguageCheckRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/check-language/",
    }

    if isinstance(body, LanguageCheckRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, LanguageCheckRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, LanguageCheckRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LanguageCheckResponse | None:
    if response.status_code == 200:
        response_200 = LanguageCheckResponse.from_dict(response.json())

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
) -> Response[Any | LanguageCheckResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LanguageCheckRequest | Unset = UNSET,
) -> Response[Any | LanguageCheckResponse]:
    """Checks the language of a string

    Args:
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LanguageCheckResponse]
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
    body: LanguageCheckRequest | Unset = UNSET,
) -> Any | LanguageCheckResponse | None:
    """Checks the language of a string

    Args:
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LanguageCheckResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LanguageCheckRequest | Unset = UNSET,
) -> Response[Any | LanguageCheckResponse]:
    """Checks the language of a string

    Args:
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LanguageCheckResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LanguageCheckRequest | Unset = UNSET,
) -> Any | LanguageCheckResponse | None:
    """Checks the language of a string

    Args:
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check
        body (LanguageCheckRequest): Serializer for language check

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LanguageCheckResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
