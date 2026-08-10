from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_exercise_video_list import PaginatedExerciseVideoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    exercise: int | Unset = UNSET,
    is_main: bool | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["exercise"] = exercise

    params["is_main"] = is_main

    params["license"] = license_

    params["license_author"] = license_author

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/video/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedExerciseVideoList | None:
    if response.status_code == 200:
        response_200 = PaginatedExerciseVideoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedExerciseVideoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    exercise: int | Unset = UNSET,
    is_main: bool | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedExerciseVideoList]:
    """API endpoint for exercise video objects

    Args:
        exercise (int | Unset):
        is_main (bool | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseVideoList]
    """

    kwargs = _get_kwargs(
        exercise=exercise,
        is_main=is_main,
        license_=license_,
        license_author=license_author,
        limit=limit,
        offset=offset,
        ordering=ordering,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    exercise: int | Unset = UNSET,
    is_main: bool | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedExerciseVideoList | None:
    """API endpoint for exercise video objects

    Args:
        exercise (int | Unset):
        is_main (bool | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseVideoList
    """

    return sync_detailed(
        client=client,
        exercise=exercise,
        is_main=is_main,
        license_=license_,
        license_author=license_author,
        limit=limit,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    exercise: int | Unset = UNSET,
    is_main: bool | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedExerciseVideoList]:
    """API endpoint for exercise video objects

    Args:
        exercise (int | Unset):
        is_main (bool | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseVideoList]
    """

    kwargs = _get_kwargs(
        exercise=exercise,
        is_main=is_main,
        license_=license_,
        license_author=license_author,
        limit=limit,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    exercise: int | Unset = UNSET,
    is_main: bool | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedExerciseVideoList | None:
    """API endpoint for exercise video objects

    Args:
        exercise (int | Unset):
        is_main (bool | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseVideoList
    """

    return (
        await asyncio_detailed(
            client=client,
            exercise=exercise,
            is_main=is_main,
            license_=license_,
            license_author=license_author,
            limit=limit,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
