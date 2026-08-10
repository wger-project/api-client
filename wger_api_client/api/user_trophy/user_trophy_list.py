import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_trophy_list import PaginatedUserTrophyList
from ...models.user_trophy_list_trophy_trophy_type import UserTrophyListTrophyTrophyType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    earned_at: datetime.datetime | Unset = UNSET,
    earned_at_gt: datetime.datetime | Unset = UNSET,
    earned_at_gte: datetime.datetime | Unset = UNSET,
    earned_at_lt: datetime.datetime | Unset = UNSET,
    earned_at_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_notified: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy: int | Unset = UNSET,
    trophy_in: list[int] | Unset = UNSET,
    trophy_is_active: bool | Unset = UNSET,
    trophy_is_hidden: bool | Unset = UNSET,
    trophy_is_repeatable: bool | Unset = UNSET,
    trophy_trophy_type: UserTrophyListTrophyTrophyType | Unset = UNSET,
    trophy_trophy_type_in: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_earned_at: str | Unset = UNSET
    if not isinstance(earned_at, Unset):
        json_earned_at = earned_at.isoformat()
    params["earned_at"] = json_earned_at

    json_earned_at_gt: str | Unset = UNSET
    if not isinstance(earned_at_gt, Unset):
        json_earned_at_gt = earned_at_gt.isoformat()
    params["earned_at__gt"] = json_earned_at_gt

    json_earned_at_gte: str | Unset = UNSET
    if not isinstance(earned_at_gte, Unset):
        json_earned_at_gte = earned_at_gte.isoformat()
    params["earned_at__gte"] = json_earned_at_gte

    json_earned_at_lt: str | Unset = UNSET
    if not isinstance(earned_at_lt, Unset):
        json_earned_at_lt = earned_at_lt.isoformat()
    params["earned_at__lt"] = json_earned_at_lt

    json_earned_at_lte: str | Unset = UNSET
    if not isinstance(earned_at_lte, Unset):
        json_earned_at_lte = earned_at_lte.isoformat()
    params["earned_at__lte"] = json_earned_at_lte

    params["id"] = id

    json_id_in: list[int] | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = id_in

    params["id__in"] = json_id_in

    params["is_notified"] = is_notified

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["trophy"] = trophy

    json_trophy_in: list[int] | Unset = UNSET
    if not isinstance(trophy_in, Unset):
        json_trophy_in = trophy_in

    params["trophy__in"] = json_trophy_in

    params["trophy__is_active"] = trophy_is_active

    params["trophy__is_hidden"] = trophy_is_hidden

    params["trophy__is_repeatable"] = trophy_is_repeatable

    json_trophy_trophy_type: str | Unset = UNSET
    if not isinstance(trophy_trophy_type, Unset):
        json_trophy_trophy_type = trophy_trophy_type.value

    params["trophy__trophy_type"] = json_trophy_trophy_type

    json_trophy_trophy_type_in: list[str] | Unset = UNSET
    if not isinstance(trophy_trophy_type_in, Unset):
        json_trophy_trophy_type_in = trophy_trophy_type_in

    params["trophy__trophy_type__in"] = json_trophy_trophy_type_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/user-trophy/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedUserTrophyList | None:
    if response.status_code == 200:
        response_200 = PaginatedUserTrophyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedUserTrophyList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    earned_at: datetime.datetime | Unset = UNSET,
    earned_at_gt: datetime.datetime | Unset = UNSET,
    earned_at_gte: datetime.datetime | Unset = UNSET,
    earned_at_lt: datetime.datetime | Unset = UNSET,
    earned_at_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_notified: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy: int | Unset = UNSET,
    trophy_in: list[int] | Unset = UNSET,
    trophy_is_active: bool | Unset = UNSET,
    trophy_is_hidden: bool | Unset = UNSET,
    trophy_is_repeatable: bool | Unset = UNSET,
    trophy_trophy_type: UserTrophyListTrophyTrophyType | Unset = UNSET,
    trophy_trophy_type_in: list[str] | Unset = UNSET,
) -> Response[PaginatedUserTrophyList]:
    """API endpoint for user's earned trophies.

    Returns the current user's earned trophies.

    list:
    Return all earned trophies for the current user

    retrieve:
    Return a specific user trophy by ID

    Args:
        earned_at (datetime.datetime | Unset):
        earned_at_gt (datetime.datetime | Unset):
        earned_at_gte (datetime.datetime | Unset):
        earned_at_lt (datetime.datetime | Unset):
        earned_at_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_notified (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy (int | Unset):
        trophy_in (list[int] | Unset):
        trophy_is_active (bool | Unset):
        trophy_is_hidden (bool | Unset):
        trophy_is_repeatable (bool | Unset):
        trophy_trophy_type (UserTrophyListTrophyTrophyType | Unset):
        trophy_trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserTrophyList]
    """

    kwargs = _get_kwargs(
        earned_at=earned_at,
        earned_at_gt=earned_at_gt,
        earned_at_gte=earned_at_gte,
        earned_at_lt=earned_at_lt,
        earned_at_lte=earned_at_lte,
        id=id,
        id_in=id_in,
        is_notified=is_notified,
        limit=limit,
        offset=offset,
        ordering=ordering,
        trophy=trophy,
        trophy_in=trophy_in,
        trophy_is_active=trophy_is_active,
        trophy_is_hidden=trophy_is_hidden,
        trophy_is_repeatable=trophy_is_repeatable,
        trophy_trophy_type=trophy_trophy_type,
        trophy_trophy_type_in=trophy_trophy_type_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    earned_at: datetime.datetime | Unset = UNSET,
    earned_at_gt: datetime.datetime | Unset = UNSET,
    earned_at_gte: datetime.datetime | Unset = UNSET,
    earned_at_lt: datetime.datetime | Unset = UNSET,
    earned_at_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_notified: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy: int | Unset = UNSET,
    trophy_in: list[int] | Unset = UNSET,
    trophy_is_active: bool | Unset = UNSET,
    trophy_is_hidden: bool | Unset = UNSET,
    trophy_is_repeatable: bool | Unset = UNSET,
    trophy_trophy_type: UserTrophyListTrophyTrophyType | Unset = UNSET,
    trophy_trophy_type_in: list[str] | Unset = UNSET,
) -> PaginatedUserTrophyList | None:
    """API endpoint for user's earned trophies.

    Returns the current user's earned trophies.

    list:
    Return all earned trophies for the current user

    retrieve:
    Return a specific user trophy by ID

    Args:
        earned_at (datetime.datetime | Unset):
        earned_at_gt (datetime.datetime | Unset):
        earned_at_gte (datetime.datetime | Unset):
        earned_at_lt (datetime.datetime | Unset):
        earned_at_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_notified (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy (int | Unset):
        trophy_in (list[int] | Unset):
        trophy_is_active (bool | Unset):
        trophy_is_hidden (bool | Unset):
        trophy_is_repeatable (bool | Unset):
        trophy_trophy_type (UserTrophyListTrophyTrophyType | Unset):
        trophy_trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserTrophyList
    """

    return sync_detailed(
        client=client,
        earned_at=earned_at,
        earned_at_gt=earned_at_gt,
        earned_at_gte=earned_at_gte,
        earned_at_lt=earned_at_lt,
        earned_at_lte=earned_at_lte,
        id=id,
        id_in=id_in,
        is_notified=is_notified,
        limit=limit,
        offset=offset,
        ordering=ordering,
        trophy=trophy,
        trophy_in=trophy_in,
        trophy_is_active=trophy_is_active,
        trophy_is_hidden=trophy_is_hidden,
        trophy_is_repeatable=trophy_is_repeatable,
        trophy_trophy_type=trophy_trophy_type,
        trophy_trophy_type_in=trophy_trophy_type_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    earned_at: datetime.datetime | Unset = UNSET,
    earned_at_gt: datetime.datetime | Unset = UNSET,
    earned_at_gte: datetime.datetime | Unset = UNSET,
    earned_at_lt: datetime.datetime | Unset = UNSET,
    earned_at_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_notified: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy: int | Unset = UNSET,
    trophy_in: list[int] | Unset = UNSET,
    trophy_is_active: bool | Unset = UNSET,
    trophy_is_hidden: bool | Unset = UNSET,
    trophy_is_repeatable: bool | Unset = UNSET,
    trophy_trophy_type: UserTrophyListTrophyTrophyType | Unset = UNSET,
    trophy_trophy_type_in: list[str] | Unset = UNSET,
) -> Response[PaginatedUserTrophyList]:
    """API endpoint for user's earned trophies.

    Returns the current user's earned trophies.

    list:
    Return all earned trophies for the current user

    retrieve:
    Return a specific user trophy by ID

    Args:
        earned_at (datetime.datetime | Unset):
        earned_at_gt (datetime.datetime | Unset):
        earned_at_gte (datetime.datetime | Unset):
        earned_at_lt (datetime.datetime | Unset):
        earned_at_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_notified (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy (int | Unset):
        trophy_in (list[int] | Unset):
        trophy_is_active (bool | Unset):
        trophy_is_hidden (bool | Unset):
        trophy_is_repeatable (bool | Unset):
        trophy_trophy_type (UserTrophyListTrophyTrophyType | Unset):
        trophy_trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserTrophyList]
    """

    kwargs = _get_kwargs(
        earned_at=earned_at,
        earned_at_gt=earned_at_gt,
        earned_at_gte=earned_at_gte,
        earned_at_lt=earned_at_lt,
        earned_at_lte=earned_at_lte,
        id=id,
        id_in=id_in,
        is_notified=is_notified,
        limit=limit,
        offset=offset,
        ordering=ordering,
        trophy=trophy,
        trophy_in=trophy_in,
        trophy_is_active=trophy_is_active,
        trophy_is_hidden=trophy_is_hidden,
        trophy_is_repeatable=trophy_is_repeatable,
        trophy_trophy_type=trophy_trophy_type,
        trophy_trophy_type_in=trophy_trophy_type_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    earned_at: datetime.datetime | Unset = UNSET,
    earned_at_gt: datetime.datetime | Unset = UNSET,
    earned_at_gte: datetime.datetime | Unset = UNSET,
    earned_at_lt: datetime.datetime | Unset = UNSET,
    earned_at_lte: datetime.datetime | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_notified: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    trophy: int | Unset = UNSET,
    trophy_in: list[int] | Unset = UNSET,
    trophy_is_active: bool | Unset = UNSET,
    trophy_is_hidden: bool | Unset = UNSET,
    trophy_is_repeatable: bool | Unset = UNSET,
    trophy_trophy_type: UserTrophyListTrophyTrophyType | Unset = UNSET,
    trophy_trophy_type_in: list[str] | Unset = UNSET,
) -> PaginatedUserTrophyList | None:
    """API endpoint for user's earned trophies.

    Returns the current user's earned trophies.

    list:
    Return all earned trophies for the current user

    retrieve:
    Return a specific user trophy by ID

    Args:
        earned_at (datetime.datetime | Unset):
        earned_at_gt (datetime.datetime | Unset):
        earned_at_gte (datetime.datetime | Unset):
        earned_at_lt (datetime.datetime | Unset):
        earned_at_lte (datetime.datetime | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_notified (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        trophy (int | Unset):
        trophy_in (list[int] | Unset):
        trophy_is_active (bool | Unset):
        trophy_is_hidden (bool | Unset):
        trophy_is_repeatable (bool | Unset):
        trophy_trophy_type (UserTrophyListTrophyTrophyType | Unset):
        trophy_trophy_type_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserTrophyList
    """

    return (
        await asyncio_detailed(
            client=client,
            earned_at=earned_at,
            earned_at_gt=earned_at_gt,
            earned_at_gte=earned_at_gte,
            earned_at_lt=earned_at_lt,
            earned_at_lte=earned_at_lte,
            id=id,
            id_in=id_in,
            is_notified=is_notified,
            limit=limit,
            offset=offset,
            ordering=ordering,
            trophy=trophy,
            trophy_in=trophy_in,
            trophy_is_active=trophy_is_active,
            trophy_is_hidden=trophy_is_hidden,
            trophy_is_repeatable=trophy_is_repeatable,
            trophy_trophy_type=trophy_trophy_type,
            trophy_trophy_type_in=trophy_trophy_type_in,
        )
    ).parsed
