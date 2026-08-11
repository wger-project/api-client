from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exercise_alias import ExerciseAlias
from ...models.exercise_alias_request import ExerciseAliasRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ExerciseAliasRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/exercisealias/",
    }

    if isinstance(body, ExerciseAliasRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ExerciseAliasRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ExerciseAliasRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExerciseAlias | None:
    if response.status_code == 201:
        response_201 = ExerciseAlias.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExerciseAlias]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExerciseAliasRequest | Unset = UNSET,
) -> Response[ExerciseAlias]:
    """API endpoint for exercise aliases objects

    Args:
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseAlias]
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
    body: ExerciseAliasRequest | Unset = UNSET,
) -> ExerciseAlias | None:
    """API endpoint for exercise aliases objects

    Args:
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseAlias
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExerciseAliasRequest | Unset = UNSET,
) -> Response[ExerciseAlias]:
    """API endpoint for exercise aliases objects

    Args:
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseAlias]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ExerciseAliasRequest | Unset = UNSET,
) -> ExerciseAlias | None:
    """API endpoint for exercise aliases objects

    Args:
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer
        body (ExerciseAliasRequest): ExerciseAlias serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseAlias
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
