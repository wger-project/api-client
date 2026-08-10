import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_nutrition_plan_info_list import PaginatedNutritionPlanInfoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    creation_date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    has_goal_calories: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_creation_date: str | Unset = UNSET
    if not isinstance(creation_date, Unset):
        json_creation_date = creation_date.isoformat()
    params["creation_date"] = json_creation_date

    params["description"] = description

    params["has_goal_calories"] = has_goal_calories

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/nutritionplaninfo/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedNutritionPlanInfoList | None:
    if response.status_code == 200:
        response_200 = PaginatedNutritionPlanInfoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedNutritionPlanInfoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    creation_date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    has_goal_calories: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedNutritionPlanInfoList]:
    """Read-only info API endpoint for nutrition plan objects. Returns nested data
    structures for more easy parsing.

    Args:
        creation_date (datetime.date | Unset):
        description (str | Unset):
        has_goal_calories (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNutritionPlanInfoList]
    """

    kwargs = _get_kwargs(
        creation_date=creation_date,
        description=description,
        has_goal_calories=has_goal_calories,
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
    creation_date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    has_goal_calories: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedNutritionPlanInfoList | None:
    """Read-only info API endpoint for nutrition plan objects. Returns nested data
    structures for more easy parsing.

    Args:
        creation_date (datetime.date | Unset):
        description (str | Unset):
        has_goal_calories (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNutritionPlanInfoList
    """

    return sync_detailed(
        client=client,
        creation_date=creation_date,
        description=description,
        has_goal_calories=has_goal_calories,
        limit=limit,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    creation_date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    has_goal_calories: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedNutritionPlanInfoList]:
    """Read-only info API endpoint for nutrition plan objects. Returns nested data
    structures for more easy parsing.

    Args:
        creation_date (datetime.date | Unset):
        description (str | Unset):
        has_goal_calories (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNutritionPlanInfoList]
    """

    kwargs = _get_kwargs(
        creation_date=creation_date,
        description=description,
        has_goal_calories=has_goal_calories,
        limit=limit,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    creation_date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    has_goal_calories: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedNutritionPlanInfoList | None:
    """Read-only info API endpoint for nutrition plan objects. Returns nested data
    structures for more easy parsing.

    Args:
        creation_date (datetime.date | Unset):
        description (str | Unset):
        has_goal_calories (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNutritionPlanInfoList
    """

    return (
        await asyncio_detailed(
            client=client,
            creation_date=creation_date,
            description=description,
            has_goal_calories=has_goal_calories,
            limit=limit,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
