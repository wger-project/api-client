from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ingredient_values import IngredientValues
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    amount: float,
    unit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["amount"] = amount

    params["unit"] = unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/ingredientinfo/{id}/get_values/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IngredientValues | None:
    if response.status_code == 200:
        response_200 = IngredientValues.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IngredientValues]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    amount: float,
    unit: int | Unset = UNSET,
) -> Response[IngredientValues]:
    """Calculates the nutritional values for current ingredient and
    the given amount and unit.

    This function basically just performs a multiplication (in the model), and
    is a candidate to be moved to pure AJAX calls, however doing it like this
    keeps the logic nicely hidden and respects the DRY principle.

    Args:
        id (int):
        amount (float):
        unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IngredientValues]
    """

    kwargs = _get_kwargs(
        id=id,
        amount=amount,
        unit=unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    amount: float,
    unit: int | Unset = UNSET,
) -> IngredientValues | None:
    """Calculates the nutritional values for current ingredient and
    the given amount and unit.

    This function basically just performs a multiplication (in the model), and
    is a candidate to be moved to pure AJAX calls, however doing it like this
    keeps the logic nicely hidden and respects the DRY principle.

    Args:
        id (int):
        amount (float):
        unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IngredientValues
    """

    return sync_detailed(
        id=id,
        client=client,
        amount=amount,
        unit=unit,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    amount: float,
    unit: int | Unset = UNSET,
) -> Response[IngredientValues]:
    """Calculates the nutritional values for current ingredient and
    the given amount and unit.

    This function basically just performs a multiplication (in the model), and
    is a candidate to be moved to pure AJAX calls, however doing it like this
    keeps the logic nicely hidden and respects the DRY principle.

    Args:
        id (int):
        amount (float):
        unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IngredientValues]
    """

    kwargs = _get_kwargs(
        id=id,
        amount=amount,
        unit=unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    amount: float,
    unit: int | Unset = UNSET,
) -> IngredientValues | None:
    """Calculates the nutritional values for current ingredient and
    the given amount and unit.

    This function basically just performs a multiplication (in the model), and
    is a candidate to be moved to pure AJAX calls, however doing it like this
    keeps the logic nicely hidden and respects the DRY principle.

    Args:
        id (int):
        amount (float):
        unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IngredientValues
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            amount=amount,
            unit=unit,
        )
    ).parsed
