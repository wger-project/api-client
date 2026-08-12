import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ingredientinfo_list_nutri_score import (
    IngredientinfoListNutriScore,
)
from ...models.paginated_ingredient_info_list import PaginatedIngredientInfoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    carbohydrates: float | Unset = UNSET,
    carbohydrates_sugar: float | Unset = UNSET,
    code: str | Unset = UNSET,
    created: datetime.datetime | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    energy: int | Unset = UNSET,
    fat: float | Unset = UNSET,
    fat_saturated: float | Unset = UNSET,
    fiber: float | Unset = UNSET,
    id: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    is_vegan: bool | Unset = UNSET,
    is_vegetarian: bool | Unset = UNSET,
    language: int | Unset = UNSET,
    language_code: str | Unset = UNSET,
    language_in: list[int] | Unset = UNSET,
    last_imported: datetime.datetime | Unset = UNSET,
    last_imported_gt: datetime.datetime | Unset = UNSET,
    last_imported_lt: datetime.datetime | Unset = UNSET,
    last_update: datetime.datetime | Unset = UNSET,
    last_update_gt: datetime.datetime | Unset = UNSET,
    last_update_lt: datetime.datetime | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    nutriscore: IngredientinfoListNutriScore | Unset = UNSET,
    nutriscore_gt: str | Unset = UNSET,
    nutriscore_gte: str | Unset = UNSET,
    nutriscore_in: list[str] | Unset = UNSET,
    nutriscore_lt: str | Unset = UNSET,
    nutriscore_lte: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    protein: float | Unset = UNSET,
    sodium: float | Unset = UNSET,
    source_name: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["carbohydrates"] = carbohydrates

    params["carbohydrates_sugar"] = carbohydrates_sugar

    params["code"] = code

    json_created: str | Unset = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    json_created_gt: str | Unset = UNSET
    if not isinstance(created_gt, Unset):
        json_created_gt = created_gt.isoformat()
    params["created__gt"] = json_created_gt

    json_created_lt: str | Unset = UNSET
    if not isinstance(created_lt, Unset):
        json_created_lt = created_lt.isoformat()
    params["created__lt"] = json_created_lt

    params["energy"] = energy

    params["fat"] = fat

    params["fat_saturated"] = fat_saturated

    params["fiber"] = fiber

    params["id"] = id

    params["id__gt"] = id_gt

    params["id__gte"] = id_gte

    json_id_in: list[int] | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = id_in

    params["id__in"] = json_id_in

    params["id__lt"] = id_lt

    params["id__lte"] = id_lte

    params["is_vegan"] = is_vegan

    params["is_vegetarian"] = is_vegetarian

    params["language"] = language

    params["language__code"] = language_code

    json_language_in: list[int] | Unset = UNSET
    if not isinstance(language_in, Unset):
        json_language_in = language_in

    params["language__in"] = json_language_in

    json_last_imported: str | Unset = UNSET
    if not isinstance(last_imported, Unset):
        json_last_imported = last_imported.isoformat()
    params["last_imported"] = json_last_imported

    json_last_imported_gt: str | Unset = UNSET
    if not isinstance(last_imported_gt, Unset):
        json_last_imported_gt = last_imported_gt.isoformat()
    params["last_imported__gt"] = json_last_imported_gt

    json_last_imported_lt: str | Unset = UNSET
    if not isinstance(last_imported_lt, Unset):
        json_last_imported_lt = last_imported_lt.isoformat()
    params["last_imported__lt"] = json_last_imported_lt

    json_last_update: str | Unset = UNSET
    if not isinstance(last_update, Unset):
        json_last_update = last_update.isoformat()
    params["last_update"] = json_last_update

    json_last_update_gt: str | Unset = UNSET
    if not isinstance(last_update_gt, Unset):
        json_last_update_gt = last_update_gt.isoformat()
    params["last_update__gt"] = json_last_update_gt

    json_last_update_lt: str | Unset = UNSET
    if not isinstance(last_update_lt, Unset):
        json_last_update_lt = last_update_lt.isoformat()
    params["last_update__lt"] = json_last_update_lt

    params["license"] = license_

    params["license_author"] = license_author

    params["limit"] = limit

    params["name"] = name

    params["name__search"] = name_search

    json_nutriscore: str | Unset = UNSET
    if not isinstance(nutriscore, Unset):
        json_nutriscore = nutriscore

    params["nutriscore"] = json_nutriscore

    params["nutriscore__gt"] = nutriscore_gt

    params["nutriscore__gte"] = nutriscore_gte

    json_nutriscore_in: list[str] | Unset = UNSET
    if not isinstance(nutriscore_in, Unset):
        json_nutriscore_in = nutriscore_in

    params["nutriscore__in"] = json_nutriscore_in

    params["nutriscore__lt"] = nutriscore_lt

    params["nutriscore__lte"] = nutriscore_lte

    params["offset"] = offset

    params["ordering"] = ordering

    params["protein"] = protein

    params["sodium"] = sodium

    params["source_name"] = source_name

    json_uuid: str | Unset = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)
    params["uuid"] = json_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/ingredientinfo/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedIngredientInfoList | None:
    if response.status_code == 200:
        response_200 = PaginatedIngredientInfoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedIngredientInfoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    carbohydrates: float | Unset = UNSET,
    carbohydrates_sugar: float | Unset = UNSET,
    code: str | Unset = UNSET,
    created: datetime.datetime | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    energy: int | Unset = UNSET,
    fat: float | Unset = UNSET,
    fat_saturated: float | Unset = UNSET,
    fiber: float | Unset = UNSET,
    id: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    is_vegan: bool | Unset = UNSET,
    is_vegetarian: bool | Unset = UNSET,
    language: int | Unset = UNSET,
    language_code: str | Unset = UNSET,
    language_in: list[int] | Unset = UNSET,
    last_imported: datetime.datetime | Unset = UNSET,
    last_imported_gt: datetime.datetime | Unset = UNSET,
    last_imported_lt: datetime.datetime | Unset = UNSET,
    last_update: datetime.datetime | Unset = UNSET,
    last_update_gt: datetime.datetime | Unset = UNSET,
    last_update_lt: datetime.datetime | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    nutriscore: IngredientinfoListNutriScore | Unset = UNSET,
    nutriscore_gt: str | Unset = UNSET,
    nutriscore_gte: str | Unset = UNSET,
    nutriscore_in: list[str] | Unset = UNSET,
    nutriscore_lt: str | Unset = UNSET,
    nutriscore_lte: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    protein: float | Unset = UNSET,
    sodium: float | Unset = UNSET,
    source_name: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> Response[PaginatedIngredientInfoList]:
    """Read-only info API endpoint for ingredient objects. Returns nested data
    structures for more easy parsing.

    Args:
        carbohydrates (float | Unset):
        carbohydrates_sugar (float | Unset):
        code (str | Unset):
        created (datetime.datetime | Unset):
        created_gt (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        energy (int | Unset):
        fat (float | Unset):
        fat_saturated (float | Unset):
        fiber (float | Unset):
        id (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_in (list[int] | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        is_vegan (bool | Unset):
        is_vegetarian (bool | Unset):
        language (int | Unset):
        language_code (str | Unset):
        language_in (list[int] | Unset):
        last_imported (datetime.datetime | Unset):
        last_imported_gt (datetime.datetime | Unset):
        last_imported_lt (datetime.datetime | Unset):
        last_update (datetime.datetime | Unset):
        last_update_gt (datetime.datetime | Unset):
        last_update_lt (datetime.datetime | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_search (str | Unset):
        nutriscore (IngredientinfoListNutriScore | Unset):
        nutriscore_gt (str | Unset):
        nutriscore_gte (str | Unset):
        nutriscore_in (list[str] | Unset):
        nutriscore_lt (str | Unset):
        nutriscore_lte (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        protein (float | Unset):
        sodium (float | Unset):
        source_name (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIngredientInfoList]
    """

    kwargs = _get_kwargs(
        carbohydrates=carbohydrates,
        carbohydrates_sugar=carbohydrates_sugar,
        code=code,
        created=created,
        created_gt=created_gt,
        created_lt=created_lt,
        energy=energy,
        fat=fat,
        fat_saturated=fat_saturated,
        fiber=fiber,
        id=id,
        id_gt=id_gt,
        id_gte=id_gte,
        id_in=id_in,
        id_lt=id_lt,
        id_lte=id_lte,
        is_vegan=is_vegan,
        is_vegetarian=is_vegetarian,
        language=language,
        language_code=language_code,
        language_in=language_in,
        last_imported=last_imported,
        last_imported_gt=last_imported_gt,
        last_imported_lt=last_imported_lt,
        last_update=last_update,
        last_update_gt=last_update_gt,
        last_update_lt=last_update_lt,
        license_=license_,
        license_author=license_author,
        limit=limit,
        name=name,
        name_search=name_search,
        nutriscore=nutriscore,
        nutriscore_gt=nutriscore_gt,
        nutriscore_gte=nutriscore_gte,
        nutriscore_in=nutriscore_in,
        nutriscore_lt=nutriscore_lt,
        nutriscore_lte=nutriscore_lte,
        offset=offset,
        ordering=ordering,
        protein=protein,
        sodium=sodium,
        source_name=source_name,
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    carbohydrates: float | Unset = UNSET,
    carbohydrates_sugar: float | Unset = UNSET,
    code: str | Unset = UNSET,
    created: datetime.datetime | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    energy: int | Unset = UNSET,
    fat: float | Unset = UNSET,
    fat_saturated: float | Unset = UNSET,
    fiber: float | Unset = UNSET,
    id: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    is_vegan: bool | Unset = UNSET,
    is_vegetarian: bool | Unset = UNSET,
    language: int | Unset = UNSET,
    language_code: str | Unset = UNSET,
    language_in: list[int] | Unset = UNSET,
    last_imported: datetime.datetime | Unset = UNSET,
    last_imported_gt: datetime.datetime | Unset = UNSET,
    last_imported_lt: datetime.datetime | Unset = UNSET,
    last_update: datetime.datetime | Unset = UNSET,
    last_update_gt: datetime.datetime | Unset = UNSET,
    last_update_lt: datetime.datetime | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    nutriscore: IngredientinfoListNutriScore | Unset = UNSET,
    nutriscore_gt: str | Unset = UNSET,
    nutriscore_gte: str | Unset = UNSET,
    nutriscore_in: list[str] | Unset = UNSET,
    nutriscore_lt: str | Unset = UNSET,
    nutriscore_lte: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    protein: float | Unset = UNSET,
    sodium: float | Unset = UNSET,
    source_name: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> PaginatedIngredientInfoList | None:
    """Read-only info API endpoint for ingredient objects. Returns nested data
    structures for more easy parsing.

    Args:
        carbohydrates (float | Unset):
        carbohydrates_sugar (float | Unset):
        code (str | Unset):
        created (datetime.datetime | Unset):
        created_gt (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        energy (int | Unset):
        fat (float | Unset):
        fat_saturated (float | Unset):
        fiber (float | Unset):
        id (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_in (list[int] | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        is_vegan (bool | Unset):
        is_vegetarian (bool | Unset):
        language (int | Unset):
        language_code (str | Unset):
        language_in (list[int] | Unset):
        last_imported (datetime.datetime | Unset):
        last_imported_gt (datetime.datetime | Unset):
        last_imported_lt (datetime.datetime | Unset):
        last_update (datetime.datetime | Unset):
        last_update_gt (datetime.datetime | Unset):
        last_update_lt (datetime.datetime | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_search (str | Unset):
        nutriscore (IngredientinfoListNutriScore | Unset):
        nutriscore_gt (str | Unset):
        nutriscore_gte (str | Unset):
        nutriscore_in (list[str] | Unset):
        nutriscore_lt (str | Unset):
        nutriscore_lte (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        protein (float | Unset):
        sodium (float | Unset):
        source_name (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIngredientInfoList
    """

    return sync_detailed(
        client=client,
        carbohydrates=carbohydrates,
        carbohydrates_sugar=carbohydrates_sugar,
        code=code,
        created=created,
        created_gt=created_gt,
        created_lt=created_lt,
        energy=energy,
        fat=fat,
        fat_saturated=fat_saturated,
        fiber=fiber,
        id=id,
        id_gt=id_gt,
        id_gte=id_gte,
        id_in=id_in,
        id_lt=id_lt,
        id_lte=id_lte,
        is_vegan=is_vegan,
        is_vegetarian=is_vegetarian,
        language=language,
        language_code=language_code,
        language_in=language_in,
        last_imported=last_imported,
        last_imported_gt=last_imported_gt,
        last_imported_lt=last_imported_lt,
        last_update=last_update,
        last_update_gt=last_update_gt,
        last_update_lt=last_update_lt,
        license_=license_,
        license_author=license_author,
        limit=limit,
        name=name,
        name_search=name_search,
        nutriscore=nutriscore,
        nutriscore_gt=nutriscore_gt,
        nutriscore_gte=nutriscore_gte,
        nutriscore_in=nutriscore_in,
        nutriscore_lt=nutriscore_lt,
        nutriscore_lte=nutriscore_lte,
        offset=offset,
        ordering=ordering,
        protein=protein,
        sodium=sodium,
        source_name=source_name,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    carbohydrates: float | Unset = UNSET,
    carbohydrates_sugar: float | Unset = UNSET,
    code: str | Unset = UNSET,
    created: datetime.datetime | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    energy: int | Unset = UNSET,
    fat: float | Unset = UNSET,
    fat_saturated: float | Unset = UNSET,
    fiber: float | Unset = UNSET,
    id: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    is_vegan: bool | Unset = UNSET,
    is_vegetarian: bool | Unset = UNSET,
    language: int | Unset = UNSET,
    language_code: str | Unset = UNSET,
    language_in: list[int] | Unset = UNSET,
    last_imported: datetime.datetime | Unset = UNSET,
    last_imported_gt: datetime.datetime | Unset = UNSET,
    last_imported_lt: datetime.datetime | Unset = UNSET,
    last_update: datetime.datetime | Unset = UNSET,
    last_update_gt: datetime.datetime | Unset = UNSET,
    last_update_lt: datetime.datetime | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    nutriscore: IngredientinfoListNutriScore | Unset = UNSET,
    nutriscore_gt: str | Unset = UNSET,
    nutriscore_gte: str | Unset = UNSET,
    nutriscore_in: list[str] | Unset = UNSET,
    nutriscore_lt: str | Unset = UNSET,
    nutriscore_lte: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    protein: float | Unset = UNSET,
    sodium: float | Unset = UNSET,
    source_name: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> Response[PaginatedIngredientInfoList]:
    """Read-only info API endpoint for ingredient objects. Returns nested data
    structures for more easy parsing.

    Args:
        carbohydrates (float | Unset):
        carbohydrates_sugar (float | Unset):
        code (str | Unset):
        created (datetime.datetime | Unset):
        created_gt (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        energy (int | Unset):
        fat (float | Unset):
        fat_saturated (float | Unset):
        fiber (float | Unset):
        id (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_in (list[int] | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        is_vegan (bool | Unset):
        is_vegetarian (bool | Unset):
        language (int | Unset):
        language_code (str | Unset):
        language_in (list[int] | Unset):
        last_imported (datetime.datetime | Unset):
        last_imported_gt (datetime.datetime | Unset):
        last_imported_lt (datetime.datetime | Unset):
        last_update (datetime.datetime | Unset):
        last_update_gt (datetime.datetime | Unset):
        last_update_lt (datetime.datetime | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_search (str | Unset):
        nutriscore (IngredientinfoListNutriScore | Unset):
        nutriscore_gt (str | Unset):
        nutriscore_gte (str | Unset):
        nutriscore_in (list[str] | Unset):
        nutriscore_lt (str | Unset):
        nutriscore_lte (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        protein (float | Unset):
        sodium (float | Unset):
        source_name (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIngredientInfoList]
    """

    kwargs = _get_kwargs(
        carbohydrates=carbohydrates,
        carbohydrates_sugar=carbohydrates_sugar,
        code=code,
        created=created,
        created_gt=created_gt,
        created_lt=created_lt,
        energy=energy,
        fat=fat,
        fat_saturated=fat_saturated,
        fiber=fiber,
        id=id,
        id_gt=id_gt,
        id_gte=id_gte,
        id_in=id_in,
        id_lt=id_lt,
        id_lte=id_lte,
        is_vegan=is_vegan,
        is_vegetarian=is_vegetarian,
        language=language,
        language_code=language_code,
        language_in=language_in,
        last_imported=last_imported,
        last_imported_gt=last_imported_gt,
        last_imported_lt=last_imported_lt,
        last_update=last_update,
        last_update_gt=last_update_gt,
        last_update_lt=last_update_lt,
        license_=license_,
        license_author=license_author,
        limit=limit,
        name=name,
        name_search=name_search,
        nutriscore=nutriscore,
        nutriscore_gt=nutriscore_gt,
        nutriscore_gte=nutriscore_gte,
        nutriscore_in=nutriscore_in,
        nutriscore_lt=nutriscore_lt,
        nutriscore_lte=nutriscore_lte,
        offset=offset,
        ordering=ordering,
        protein=protein,
        sodium=sodium,
        source_name=source_name,
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    carbohydrates: float | Unset = UNSET,
    carbohydrates_sugar: float | Unset = UNSET,
    code: str | Unset = UNSET,
    created: datetime.datetime | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    energy: int | Unset = UNSET,
    fat: float | Unset = UNSET,
    fat_saturated: float | Unset = UNSET,
    fiber: float | Unset = UNSET,
    id: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    is_vegan: bool | Unset = UNSET,
    is_vegetarian: bool | Unset = UNSET,
    language: int | Unset = UNSET,
    language_code: str | Unset = UNSET,
    language_in: list[int] | Unset = UNSET,
    last_imported: datetime.datetime | Unset = UNSET,
    last_imported_gt: datetime.datetime | Unset = UNSET,
    last_imported_lt: datetime.datetime | Unset = UNSET,
    last_update: datetime.datetime | Unset = UNSET,
    last_update_gt: datetime.datetime | Unset = UNSET,
    last_update_lt: datetime.datetime | Unset = UNSET,
    license_: int | Unset = UNSET,
    license_author: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_search: str | Unset = UNSET,
    nutriscore: IngredientinfoListNutriScore | Unset = UNSET,
    nutriscore_gt: str | Unset = UNSET,
    nutriscore_gte: str | Unset = UNSET,
    nutriscore_in: list[str] | Unset = UNSET,
    nutriscore_lt: str | Unset = UNSET,
    nutriscore_lte: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    protein: float | Unset = UNSET,
    sodium: float | Unset = UNSET,
    source_name: str | Unset = UNSET,
    uuid: UUID | Unset = UNSET,
) -> PaginatedIngredientInfoList | None:
    """Read-only info API endpoint for ingredient objects. Returns nested data
    structures for more easy parsing.

    Args:
        carbohydrates (float | Unset):
        carbohydrates_sugar (float | Unset):
        code (str | Unset):
        created (datetime.datetime | Unset):
        created_gt (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        energy (int | Unset):
        fat (float | Unset):
        fat_saturated (float | Unset):
        fiber (float | Unset):
        id (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_in (list[int] | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        is_vegan (bool | Unset):
        is_vegetarian (bool | Unset):
        language (int | Unset):
        language_code (str | Unset):
        language_in (list[int] | Unset):
        last_imported (datetime.datetime | Unset):
        last_imported_gt (datetime.datetime | Unset):
        last_imported_lt (datetime.datetime | Unset):
        last_update (datetime.datetime | Unset):
        last_update_gt (datetime.datetime | Unset):
        last_update_lt (datetime.datetime | Unset):
        license_ (int | Unset):
        license_author (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_search (str | Unset):
        nutriscore (IngredientinfoListNutriScore | Unset):
        nutriscore_gt (str | Unset):
        nutriscore_gte (str | Unset):
        nutriscore_in (list[str] | Unset):
        nutriscore_lt (str | Unset):
        nutriscore_lte (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        protein (float | Unset):
        sodium (float | Unset):
        source_name (str | Unset):
        uuid (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIngredientInfoList
    """

    return (
        await asyncio_detailed(
            client=client,
            carbohydrates=carbohydrates,
            carbohydrates_sugar=carbohydrates_sugar,
            code=code,
            created=created,
            created_gt=created_gt,
            created_lt=created_lt,
            energy=energy,
            fat=fat,
            fat_saturated=fat_saturated,
            fiber=fiber,
            id=id,
            id_gt=id_gt,
            id_gte=id_gte,
            id_in=id_in,
            id_lt=id_lt,
            id_lte=id_lte,
            is_vegan=is_vegan,
            is_vegetarian=is_vegetarian,
            language=language,
            language_code=language_code,
            language_in=language_in,
            last_imported=last_imported,
            last_imported_gt=last_imported_gt,
            last_imported_lt=last_imported_lt,
            last_update=last_update,
            last_update_gt=last_update_gt,
            last_update_lt=last_update_lt,
            license_=license_,
            license_author=license_author,
            limit=limit,
            name=name,
            name_search=name_search,
            nutriscore=nutriscore,
            nutriscore_gt=nutriscore_gt,
            nutriscore_gte=nutriscore_gte,
            nutriscore_in=nutriscore_in,
            nutriscore_lt=nutriscore_lt,
            nutriscore_lte=nutriscore_lte,
            offset=offset,
            ordering=ordering,
            protein=protein,
            sodium=sodium,
            source_name=source_name,
            uuid=uuid,
        )
    ).parsed
