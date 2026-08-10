from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_meal_item_list import PaginatedMealItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    amount: float | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    meal: UUID | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["amount"] = amount

    params["ingredient"] = ingredient

    params["limit"] = limit

    json_meal: str | Unset = UNSET
    if not isinstance(meal, Unset):
        json_meal = str(meal)
    params["meal"] = json_meal

    params["offset"] = offset

    params["order"] = order

    params["ordering"] = ordering

    params["weight_unit"] = weight_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/mealitem/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedMealItemList | None:
    if response.status_code == 200:
        response_200 = PaginatedMealItemList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedMealItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    meal: UUID | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> Response[PaginatedMealItemList]:
    """API endpoint for meal item objects

    Args:
        amount (float | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        meal (UUID | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMealItemList]
    """

    kwargs = _get_kwargs(
        amount=amount,
        ingredient=ingredient,
        limit=limit,
        meal=meal,
        offset=offset,
        order=order,
        ordering=ordering,
        weight_unit=weight_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    meal: UUID | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> PaginatedMealItemList | None:
    """API endpoint for meal item objects

    Args:
        amount (float | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        meal (UUID | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMealItemList
    """

    return sync_detailed(
        client=client,
        amount=amount,
        ingredient=ingredient,
        limit=limit,
        meal=meal,
        offset=offset,
        order=order,
        ordering=ordering,
        weight_unit=weight_unit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    meal: UUID | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> Response[PaginatedMealItemList]:
    """API endpoint for meal item objects

    Args:
        amount (float | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        meal (UUID | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMealItemList]
    """

    kwargs = _get_kwargs(
        amount=amount,
        ingredient=ingredient,
        limit=limit,
        meal=meal,
        offset=offset,
        order=order,
        ordering=ordering,
        weight_unit=weight_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    amount: float | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    meal: UUID | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> PaginatedMealItemList | None:
    """API endpoint for meal item objects

    Args:
        amount (float | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        meal (UUID | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMealItemList
    """

    return (
        await asyncio_detailed(
            client=client,
            amount=amount,
            ingredient=ingredient,
            limit=limit,
            meal=meal,
            offset=offset,
            order=order,
            ordering=ordering,
            weight_unit=weight_unit,
        )
    ).parsed
