from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_exercise_list import PaginatedExerciseList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: int | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["category"] = category

    json_equipment: list[int] | Unset = UNSET
    if not isinstance(equipment, Unset):
        json_equipment = equipment

    params["equipment"] = json_equipment

    params["limit"] = limit

    json_muscles: list[int] | Unset = UNSET
    if not isinstance(muscles, Unset):
        json_muscles = muscles

    params["muscles"] = json_muscles

    json_muscles_secondary: list[int] | Unset = UNSET
    if not isinstance(muscles_secondary, Unset):
        json_muscles_secondary = muscles_secondary

    params["muscles_secondary"] = json_muscles_secondary

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/exercise/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedExerciseList | None:
    if response.status_code == 200:
        response_200 = PaginatedExerciseList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedExerciseList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category: int | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedExerciseList]:
    """API endpoint for exercise objects.

    For a read-only endpoint with all the information of an exercise, see /api/v2/exerciseinfo/

    Args:
        category (int | Unset):
        equipment (list[int] | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseList]
    """

    kwargs = _get_kwargs(
        category=category,
        equipment=equipment,
        limit=limit,
        muscles=muscles,
        muscles_secondary=muscles_secondary,
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
    category: int | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedExerciseList | None:
    """API endpoint for exercise objects.

    For a read-only endpoint with all the information of an exercise, see /api/v2/exerciseinfo/

    Args:
        category (int | Unset):
        equipment (list[int] | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseList
    """

    return sync_detailed(
        client=client,
        category=category,
        equipment=equipment,
        limit=limit,
        muscles=muscles,
        muscles_secondary=muscles_secondary,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: int | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedExerciseList]:
    """API endpoint for exercise objects.

    For a read-only endpoint with all the information of an exercise, see /api/v2/exerciseinfo/

    Args:
        category (int | Unset):
        equipment (list[int] | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseList]
    """

    kwargs = _get_kwargs(
        category=category,
        equipment=equipment,
        limit=limit,
        muscles=muscles,
        muscles_secondary=muscles_secondary,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category: int | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedExerciseList | None:
    """API endpoint for exercise objects.

    For a read-only endpoint with all the information of an exercise, see /api/v2/exerciseinfo/

    Args:
        category (int | Unset):
        equipment (list[int] | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseList
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            equipment=equipment,
            limit=limit,
            muscles=muscles,
            muscles_secondary=muscles_secondary,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
