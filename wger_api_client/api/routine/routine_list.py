import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_routine_list import PaginatedRoutineList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_created: str | Unset = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["description"] = description

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["is_public"] = is_public

    params["is_template"] = is_template

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["ordering"] = ordering

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/routine/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedRoutineList | None:
    if response.status_code == 200:
        response_200 = PaginatedRoutineList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedRoutineList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> Response[PaginatedRoutineList]:
    """API endpoint for routine objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRoutineList]
    """

    kwargs = _get_kwargs(
        created=created,
        description=description,
        end=end,
        is_public=is_public,
        is_template=is_template,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> PaginatedRoutineList | None:
    """API endpoint for routine objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRoutineList
    """

    return sync_detailed(
        client=client,
        created=created,
        description=description,
        end=end,
        is_public=is_public,
        is_template=is_template,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        start=start,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> Response[PaginatedRoutineList]:
    """API endpoint for routine objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRoutineList]
    """

    kwargs = _get_kwargs(
        created=created,
        description=description,
        end=end,
        is_public=is_public,
        is_template=is_template,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> PaginatedRoutineList | None:
    """API endpoint for routine objects

    Args:
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRoutineList
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            description=description,
            end=end,
            is_public=is_public,
            is_template=is_template,
            limit=limit,
            name=name,
            offset=offset,
            ordering=ordering,
            start=start,
        )
    ).parsed
