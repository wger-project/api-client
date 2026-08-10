from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_ingredient_image_list import PaginatedIngredientImageList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ingredient_uuid: UUID | Unset = UNSET,
    ingredient_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ingredient_uuid: str | Unset = UNSET
    if not isinstance(ingredient_uuid, Unset):
        json_ingredient_uuid = str(ingredient_uuid)
    params["ingredient__uuid"] = json_ingredient_uuid

    params["ingredient_id"] = ingredient_id

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    json_uuid: str | Unset = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)
    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/ingredient-image/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedIngredientImageList | None:
    if response.status_code == 200:
        response_200 = PaginatedIngredientImageList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedIngredientImageList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ingredient_uuid: UUID | Unset = UNSET,
    ingredient_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> Response[PaginatedIngredientImageList]:
    """API endpoint for ingredient images

    Args:
        ingredient_uuid (UUID | Unset):
        ingredient_id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIngredientImageList]
    """

    kwargs = _get_kwargs(
        ingredient_uuid=ingredient_uuid,
        ingredient_id=ingredient_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ingredient_uuid: UUID | Unset = UNSET,
    ingredient_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> PaginatedIngredientImageList | None:
    """API endpoint for ingredient images

    Args:
        ingredient_uuid (UUID | Unset):
        ingredient_id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIngredientImageList
    """

    return sync_detailed(
        client=client,
        ingredient_uuid=ingredient_uuid,
        ingredient_id=ingredient_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ingredient_uuid: UUID | Unset = UNSET,
    ingredient_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> Response[PaginatedIngredientImageList]:
    """API endpoint for ingredient images

    Args:
        ingredient_uuid (UUID | Unset):
        ingredient_id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIngredientImageList]
    """

    kwargs = _get_kwargs(
        ingredient_uuid=ingredient_uuid,
        ingredient_id=ingredient_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ingredient_uuid: UUID | Unset = UNSET,
    ingredient_id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> PaginatedIngredientImageList | None:
    """API endpoint for ingredient images

    Args:
        ingredient_uuid (UUID | Unset):
        ingredient_id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIngredientImageList
    """

    return (
        await asyncio_detailed(
            client=client,
            ingredient_uuid=ingredient_uuid,
            ingredient_id=ingredient_id,
            limit=limit,
            offset=offset,
            ordering=ordering,
            uuid=uuid,
        )
    ).parsed
