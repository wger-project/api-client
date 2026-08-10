import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.log_display import LogDisplay
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    name: str | Unset = UNSET,
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

    params["name"] = name

    params["ordering"] = ordering

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/routine/{id}/logs/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[LogDisplay] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LogDisplay.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[LogDisplay]]:
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
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> Response[list[LogDisplay]]:
    """Returns the logs for the routine

    Args:
        id (int):
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        name (str | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[LogDisplay]]
    """

    kwargs = _get_kwargs(
        id=id,
        created=created,
        description=description,
        end=end,
        is_public=is_public,
        is_template=is_template,
        name=name,
        ordering=ordering,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> list[LogDisplay] | None:
    """Returns the logs for the routine

    Args:
        id (int):
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        name (str | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[LogDisplay]
    """

    return sync_detailed(
        id=id,
        client=client,
        created=created,
        description=description,
        end=end,
        is_public=is_public,
        is_template=is_template,
        name=name,
        ordering=ordering,
        start=start,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> Response[list[LogDisplay]]:
    """Returns the logs for the routine

    Args:
        id (int):
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        name (str | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[LogDisplay]]
    """

    kwargs = _get_kwargs(
        id=id,
        created=created,
        description=description,
        end=end,
        is_public=is_public,
        is_template=is_template,
        name=name,
        ordering=ordering,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    description: str | Unset = UNSET,
    end: datetime.date | Unset = UNSET,
    is_public: bool | Unset = UNSET,
    is_template: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
) -> list[LogDisplay] | None:
    """Returns the logs for the routine

    Args:
        id (int):
        created (datetime.datetime | Unset):
        description (str | Unset):
        end (datetime.date | Unset):
        is_public (bool | Unset):
        is_template (bool | Unset):
        name (str | Unset):
        ordering (str | Unset):
        start (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[LogDisplay]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            created=created,
            description=description,
            end=end,
            is_public=is_public,
            is_template=is_template,
            name=name,
            ordering=ordering,
            start=start,
        )
    ).parsed
