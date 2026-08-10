from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_ingredient_weight_unit_list import (
    PaginatedIngredientWeightUnitList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    gram: int | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["gram"] = gram

    params["ingredient"] = ingredient

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/ingredientweightunit/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedIngredientWeightUnitList | None:
    if response.status_code == 200:
        response_200 = PaginatedIngredientWeightUnitList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedIngredientWeightUnitList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    gram: int | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedIngredientWeightUnitList]:
    """API endpoint for ingredient weight unit objects

    Args:
        gram (int | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIngredientWeightUnitList]
    """

    kwargs = _get_kwargs(
        gram=gram,
        ingredient=ingredient,
        limit=limit,
        name=name,
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
    gram: int | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedIngredientWeightUnitList | None:
    """API endpoint for ingredient weight unit objects

    Args:
        gram (int | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIngredientWeightUnitList
    """

    return sync_detailed(
        client=client,
        gram=gram,
        ingredient=ingredient,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    gram: int | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedIngredientWeightUnitList]:
    """API endpoint for ingredient weight unit objects

    Args:
        gram (int | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIngredientWeightUnitList]
    """

    kwargs = _get_kwargs(
        gram=gram,
        ingredient=ingredient,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    gram: int | Unset = UNSET,
    ingredient: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedIngredientWeightUnitList | None:
    """API endpoint for ingredient weight unit objects

    Args:
        gram (int | Unset):
        ingredient (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIngredientWeightUnitList
    """

    return (
        await asyncio_detailed(
            client=client,
            gram=gram,
            ingredient=ingredient,
            limit=limit,
            name=name,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
