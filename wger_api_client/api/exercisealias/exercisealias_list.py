from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_exercise_alias_list import PaginatedExerciseAliasList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    translation: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["alias"] = alias

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["translation"] = translation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/exercisealias/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedExerciseAliasList | None:
    if response.status_code == 200:
        response_200 = PaginatedExerciseAliasList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedExerciseAliasList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    translation: int | Unset = UNSET,
) -> Response[PaginatedExerciseAliasList]:
    """API endpoint for exercise aliases objects

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        translation (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseAliasList]
    """

    kwargs = _get_kwargs(
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        translation=translation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    translation: int | Unset = UNSET,
) -> PaginatedExerciseAliasList | None:
    """API endpoint for exercise aliases objects

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        translation (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseAliasList
    """

    return sync_detailed(
        client=client,
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        translation=translation,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    translation: int | Unset = UNSET,
) -> Response[PaginatedExerciseAliasList]:
    """API endpoint for exercise aliases objects

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        translation (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseAliasList]
    """

    kwargs = _get_kwargs(
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        translation=translation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    translation: int | Unset = UNSET,
) -> PaginatedExerciseAliasList | None:
    """API endpoint for exercise aliases objects

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        translation (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseAliasList
    """

    return (
        await asyncio_detailed(
            client=client,
            alias=alias,
            limit=limit,
            offset=offset,
            ordering=ordering,
            translation=translation,
        )
    ).parsed
