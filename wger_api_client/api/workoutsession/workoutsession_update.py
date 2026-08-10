from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workout_session import WorkoutSession
from ...models.workout_session_request import WorkoutSessionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: WorkoutSessionRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/workoutsession/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, WorkoutSessionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, WorkoutSessionRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, WorkoutSessionRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WorkoutSession | None:
    if response.status_code == 200:
        response_200 = WorkoutSession.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WorkoutSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkoutSessionRequest | Unset = UNSET,
) -> Response[WorkoutSession]:
    """API endpoint for workout sessions objects

    Args:
        id (UUID):
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkoutSession]
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkoutSessionRequest | Unset = UNSET,
) -> WorkoutSession | None:
    """API endpoint for workout sessions objects

    Args:
        id (UUID):
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkoutSession
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkoutSessionRequest | Unset = UNSET,
) -> Response[WorkoutSession]:
    """API endpoint for workout sessions objects

    Args:
        id (UUID):
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkoutSession]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkoutSessionRequest | Unset = UNSET,
) -> WorkoutSession | None:
    """API endpoint for workout sessions objects

    Args:
        id (UUID):
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer
        body (WorkoutSessionRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkoutSession
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
