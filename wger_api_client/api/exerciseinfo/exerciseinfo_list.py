from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_exercise_info_list import PaginatedExerciseInfoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: int | Unset = UNSET,
    category_in: list[int] | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    equipment_in: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    language_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_in: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    muscles_secondary_in: list[int] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
    variation_group: UUID | Unset = UNSET,
    variation_group_in: list[UUID] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["category"] = category

    json_category_in: list[int] | Unset = UNSET
    if not isinstance(category_in, Unset):
        json_category_in = category_in

    params["category__in"] = json_category_in

    json_equipment: list[int] | Unset = UNSET
    if not isinstance(equipment, Unset):
        json_equipment = equipment

    params["equipment"] = json_equipment

    json_equipment_in: list[int] | Unset = UNSET
    if not isinstance(equipment_in, Unset):
        json_equipment_in = equipment_in

    params["equipment__in"] = json_equipment_in

    params["id"] = id

    json_id_in: list[int] | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = id_in

    params["id__in"] = json_id_in

    params["language__code"] = language_code

    params["limit"] = limit

    json_muscles: list[int] | Unset = UNSET
    if not isinstance(muscles, Unset):
        json_muscles = muscles

    params["muscles"] = json_muscles

    json_muscles_in: list[int] | Unset = UNSET
    if not isinstance(muscles_in, Unset):
        json_muscles_in = muscles_in

    params["muscles__in"] = json_muscles_in

    json_muscles_secondary: list[int] | Unset = UNSET
    if not isinstance(muscles_secondary, Unset):
        json_muscles_secondary = muscles_secondary

    params["muscles_secondary"] = json_muscles_secondary

    json_muscles_secondary_in: list[int] | Unset = UNSET
    if not isinstance(muscles_secondary_in, Unset):
        json_muscles_secondary_in = muscles_secondary_in

    params["muscles_secondary__in"] = json_muscles_secondary_in

    params["name__exact"] = name_exact

    params["name__search"] = name_search

    params["offset"] = offset

    params["ordering"] = ordering

    json_uuid: str | Unset = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)
    params["uuid"] = json_uuid

    json_variation_group: str | Unset = UNSET
    if not isinstance(variation_group, Unset):
        json_variation_group = str(variation_group)
    params["variation_group"] = json_variation_group

    json_variation_group_in: list[str] | Unset = UNSET
    if not isinstance(variation_group_in, Unset):
        json_variation_group_in = []
        for variation_group_in_item_data in variation_group_in:
            variation_group_in_item = str(variation_group_in_item_data)
            json_variation_group_in.append(variation_group_in_item)

    params["variation_group__in"] = json_variation_group_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/exerciseinfo/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedExerciseInfoList | None:
    if response.status_code == 200:
        response_200 = PaginatedExerciseInfoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedExerciseInfoList]:
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
    category_in: list[int] | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    equipment_in: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    language_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_in: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    muscles_secondary_in: list[int] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
    variation_group: UUID | Unset = UNSET,
    variation_group_in: list[UUID] | Unset = UNSET,
) -> Response[PaginatedExerciseInfoList]:
    """Serve the list from the per-exercise cache, hitting the DB only for misses.

    Args:
        category (int | Unset):
        category_in (list[int] | Unset):
        equipment (list[int] | Unset):
        equipment_in (list[int] | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        language_code (str | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_in (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        muscles_secondary_in (list[int] | Unset):
        name_exact (str | Unset):
        name_search (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):
        variation_group (UUID | Unset):
        variation_group_in (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseInfoList]
    """

    kwargs = _get_kwargs(
        category=category,
        category_in=category_in,
        equipment=equipment,
        equipment_in=equipment_in,
        id=id,
        id_in=id_in,
        language_code=language_code,
        limit=limit,
        muscles=muscles,
        muscles_in=muscles_in,
        muscles_secondary=muscles_secondary,
        muscles_secondary_in=muscles_secondary_in,
        name_exact=name_exact,
        name_search=name_search,
        offset=offset,
        ordering=ordering,
        uuid=uuid,
        variation_group=variation_group,
        variation_group_in=variation_group_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category: int | Unset = UNSET,
    category_in: list[int] | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    equipment_in: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    language_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_in: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    muscles_secondary_in: list[int] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
    variation_group: UUID | Unset = UNSET,
    variation_group_in: list[UUID] | Unset = UNSET,
) -> PaginatedExerciseInfoList | None:
    """Serve the list from the per-exercise cache, hitting the DB only for misses.

    Args:
        category (int | Unset):
        category_in (list[int] | Unset):
        equipment (list[int] | Unset):
        equipment_in (list[int] | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        language_code (str | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_in (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        muscles_secondary_in (list[int] | Unset):
        name_exact (str | Unset):
        name_search (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):
        variation_group (UUID | Unset):
        variation_group_in (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseInfoList
    """

    return sync_detailed(
        client=client,
        category=category,
        category_in=category_in,
        equipment=equipment,
        equipment_in=equipment_in,
        id=id,
        id_in=id_in,
        language_code=language_code,
        limit=limit,
        muscles=muscles,
        muscles_in=muscles_in,
        muscles_secondary=muscles_secondary,
        muscles_secondary_in=muscles_secondary_in,
        name_exact=name_exact,
        name_search=name_search,
        offset=offset,
        ordering=ordering,
        uuid=uuid,
        variation_group=variation_group,
        variation_group_in=variation_group_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: int | Unset = UNSET,
    category_in: list[int] | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    equipment_in: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    language_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_in: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    muscles_secondary_in: list[int] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
    variation_group: UUID | Unset = UNSET,
    variation_group_in: list[UUID] | Unset = UNSET,
) -> Response[PaginatedExerciseInfoList]:
    """Serve the list from the per-exercise cache, hitting the DB only for misses.

    Args:
        category (int | Unset):
        category_in (list[int] | Unset):
        equipment (list[int] | Unset):
        equipment_in (list[int] | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        language_code (str | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_in (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        muscles_secondary_in (list[int] | Unset):
        name_exact (str | Unset):
        name_search (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):
        variation_group (UUID | Unset):
        variation_group_in (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExerciseInfoList]
    """

    kwargs = _get_kwargs(
        category=category,
        category_in=category_in,
        equipment=equipment,
        equipment_in=equipment_in,
        id=id,
        id_in=id_in,
        language_code=language_code,
        limit=limit,
        muscles=muscles,
        muscles_in=muscles_in,
        muscles_secondary=muscles_secondary,
        muscles_secondary_in=muscles_secondary_in,
        name_exact=name_exact,
        name_search=name_search,
        offset=offset,
        ordering=ordering,
        uuid=uuid,
        variation_group=variation_group,
        variation_group_in=variation_group_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category: int | Unset = UNSET,
    category_in: list[int] | Unset = UNSET,
    equipment: list[int] | Unset = UNSET,
    equipment_in: list[int] | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    language_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    muscles: list[int] | Unset = UNSET,
    muscles_in: list[int] | Unset = UNSET,
    muscles_secondary: list[int] | Unset = UNSET,
    muscles_secondary_in: list[int] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
    variation_group: UUID | Unset = UNSET,
    variation_group_in: list[UUID] | Unset = UNSET,
) -> PaginatedExerciseInfoList | None:
    """Serve the list from the per-exercise cache, hitting the DB only for misses.

    Args:
        category (int | Unset):
        category_in (list[int] | Unset):
        equipment (list[int] | Unset):
        equipment_in (list[int] | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        language_code (str | Unset):
        limit (int | Unset):
        muscles (list[int] | Unset):
        muscles_in (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        muscles_secondary_in (list[int] | Unset):
        name_exact (str | Unset):
        name_search (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        uuid (UUID | Unset):
        variation_group (UUID | Unset):
        variation_group_in (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExerciseInfoList
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            category_in=category_in,
            equipment=equipment,
            equipment_in=equipment_in,
            id=id,
            id_in=id_in,
            language_code=language_code,
            limit=limit,
            muscles=muscles,
            muscles_in=muscles_in,
            muscles_secondary=muscles_secondary,
            muscles_secondary_in=muscles_secondary_in,
            name_exact=name_exact,
            name_search=name_search,
            offset=offset,
            ordering=ordering,
            uuid=uuid,
            variation_group=variation_group,
            variation_group_in=variation_group_in,
        )
    ).parsed
