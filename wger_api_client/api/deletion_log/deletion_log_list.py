from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deletion_log_list_model_type import DeletionLogListModelType
from ...models.paginated_deletion_log_list import PaginatedDeletionLogList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    model_type: DeletionLogListModelType | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_model_type: str | Unset = UNSET
    if not isinstance(model_type, Unset):
        json_model_type = model_type.value

    params["model_type"] = json_model_type

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/deletion-log/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedDeletionLogList | None:
    if response.status_code == 200:
        response_200 = PaginatedDeletionLogList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedDeletionLogList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    model_type: DeletionLogListModelType | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedDeletionLogList]:
    """API endpoint for exercise deletion logs

    This lists objects that where deleted on a wger instance and should be deleted
    as well when performing a sync (e.g. because many exercises where submitted at
    once or an image was uploaded that hasn't a CC license)

    Args:
        limit (int | Unset):
        model_type (DeletionLogListModelType | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeletionLogList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        model_type=model_type,
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
    limit: int | Unset = UNSET,
    model_type: DeletionLogListModelType | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedDeletionLogList | None:
    """API endpoint for exercise deletion logs

    This lists objects that where deleted on a wger instance and should be deleted
    as well when performing a sync (e.g. because many exercises where submitted at
    once or an image was uploaded that hasn't a CC license)

    Args:
        limit (int | Unset):
        model_type (DeletionLogListModelType | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDeletionLogList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        model_type=model_type,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    model_type: DeletionLogListModelType | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedDeletionLogList]:
    """API endpoint for exercise deletion logs

    This lists objects that where deleted on a wger instance and should be deleted
    as well when performing a sync (e.g. because many exercises where submitted at
    once or an image was uploaded that hasn't a CC license)

    Args:
        limit (int | Unset):
        model_type (DeletionLogListModelType | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeletionLogList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        model_type=model_type,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    model_type: DeletionLogListModelType | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedDeletionLogList | None:
    """API endpoint for exercise deletion logs

    This lists objects that where deleted on a wger instance and should be deleted
    as well when performing a sync (e.g. because many exercises where submitted at
    once or an image was uploaded that hasn't a CC license)

    Args:
        limit (int | Unset):
        model_type (DeletionLogListModelType | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDeletionLogList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            model_type=model_type,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
