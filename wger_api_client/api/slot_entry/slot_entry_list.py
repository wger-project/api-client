from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_slot_entry_list import PaginatedSlotEntryList
from ...models.slot_entry_list_type import SlotEntryListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    comment: str | Unset = UNSET,
    exercise: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetition_rounding: float | Unset = UNSET,
    repetition_unit: int | Unset = UNSET,
    slot: int | Unset = UNSET,
    type_: SlotEntryListType | Unset = UNSET,
    weight_rounding: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["comment"] = comment

    params["exercise"] = exercise

    params["limit"] = limit

    params["offset"] = offset

    params["order"] = order

    params["ordering"] = ordering

    params["repetition_rounding"] = repetition_rounding

    params["repetition_unit"] = repetition_unit

    params["slot"] = slot

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["weight_rounding"] = weight_rounding

    params["weight_unit"] = weight_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/slot-entry/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedSlotEntryList | None:
    if response.status_code == 200:
        response_200 = PaginatedSlotEntryList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedSlotEntryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    exercise: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetition_rounding: float | Unset = UNSET,
    repetition_unit: int | Unset = UNSET,
    slot: int | Unset = UNSET,
    type_: SlotEntryListType | Unset = UNSET,
    weight_rounding: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> Response[PaginatedSlotEntryList]:
    """API endpoint for routine slot entry objects

    Args:
        comment (str | Unset):
        exercise (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        repetition_rounding (float | Unset):
        repetition_unit (int | Unset):
        slot (int | Unset):
        type_ (SlotEntryListType | Unset):
        weight_rounding (float | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSlotEntryList]
    """

    kwargs = _get_kwargs(
        comment=comment,
        exercise=exercise,
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
        repetition_rounding=repetition_rounding,
        repetition_unit=repetition_unit,
        slot=slot,
        type_=type_,
        weight_rounding=weight_rounding,
        weight_unit=weight_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    exercise: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetition_rounding: float | Unset = UNSET,
    repetition_unit: int | Unset = UNSET,
    slot: int | Unset = UNSET,
    type_: SlotEntryListType | Unset = UNSET,
    weight_rounding: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> PaginatedSlotEntryList | None:
    """API endpoint for routine slot entry objects

    Args:
        comment (str | Unset):
        exercise (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        repetition_rounding (float | Unset):
        repetition_unit (int | Unset):
        slot (int | Unset):
        type_ (SlotEntryListType | Unset):
        weight_rounding (float | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSlotEntryList
    """

    return sync_detailed(
        client=client,
        comment=comment,
        exercise=exercise,
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
        repetition_rounding=repetition_rounding,
        repetition_unit=repetition_unit,
        slot=slot,
        type_=type_,
        weight_rounding=weight_rounding,
        weight_unit=weight_unit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    exercise: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetition_rounding: float | Unset = UNSET,
    repetition_unit: int | Unset = UNSET,
    slot: int | Unset = UNSET,
    type_: SlotEntryListType | Unset = UNSET,
    weight_rounding: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> Response[PaginatedSlotEntryList]:
    """API endpoint for routine slot entry objects

    Args:
        comment (str | Unset):
        exercise (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        repetition_rounding (float | Unset):
        repetition_unit (int | Unset):
        slot (int | Unset):
        type_ (SlotEntryListType | Unset):
        weight_rounding (float | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSlotEntryList]
    """

    kwargs = _get_kwargs(
        comment=comment,
        exercise=exercise,
        limit=limit,
        offset=offset,
        order=order,
        ordering=ordering,
        repetition_rounding=repetition_rounding,
        repetition_unit=repetition_unit,
        slot=slot,
        type_=type_,
        weight_rounding=weight_rounding,
        weight_unit=weight_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    comment: str | Unset = UNSET,
    exercise: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetition_rounding: float | Unset = UNSET,
    repetition_unit: int | Unset = UNSET,
    slot: int | Unset = UNSET,
    type_: SlotEntryListType | Unset = UNSET,
    weight_rounding: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
) -> PaginatedSlotEntryList | None:
    """API endpoint for routine slot entry objects

    Args:
        comment (str | Unset):
        exercise (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        order (int | Unset):
        ordering (str | Unset):
        repetition_rounding (float | Unset):
        repetition_unit (int | Unset):
        slot (int | Unset):
        type_ (SlotEntryListType | Unset):
        weight_rounding (float | Unset):
        weight_unit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSlotEntryList
    """

    return (
        await asyncio_detailed(
            client=client,
            comment=comment,
            exercise=exercise,
            limit=limit,
            offset=offset,
            order=order,
            ordering=ordering,
            repetition_rounding=repetition_rounding,
            repetition_unit=repetition_unit,
            slot=slot,
            type_=type_,
            weight_rounding=weight_rounding,
            weight_unit=weight_unit,
        )
    ).parsed
