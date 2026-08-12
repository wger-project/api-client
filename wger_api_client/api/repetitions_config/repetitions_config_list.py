from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_repetitions_config_list import PaginatedRepetitionsConfigList
from ...models.repetitions_config_list_operation import (
    RepetitionsConfigListOperation,
)
from ...models.repetitions_config_list_step import (
    RepetitionsConfigListStep,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    iteration: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    operation: RepetitionsConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: RepetitionsConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["iteration"] = iteration

    params["limit"] = limit

    params["offset"] = offset

    json_operation: str | Unset = UNSET
    if not isinstance(operation, Unset):
        json_operation = operation

    params["operation"] = json_operation

    params["ordering"] = ordering

    params["repeat"] = repeat

    params["slot_entry"] = slot_entry

    json_step: str | Unset = UNSET
    if not isinstance(step, Unset):
        json_step = step

    params["step"] = json_step

    params["value"] = value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/repetitions-config/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedRepetitionsConfigList | None:
    if response.status_code == 200:
        response_200 = PaginatedRepetitionsConfigList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedRepetitionsConfigList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    iteration: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    operation: RepetitionsConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: RepetitionsConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> Response[PaginatedRepetitionsConfigList]:
    """API endpoint for reps config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (RepetitionsConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (RepetitionsConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRepetitionsConfigList]
    """

    kwargs = _get_kwargs(
        id=id,
        iteration=iteration,
        limit=limit,
        offset=offset,
        operation=operation,
        ordering=ordering,
        repeat=repeat,
        slot_entry=slot_entry,
        step=step,
        value=value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    iteration: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    operation: RepetitionsConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: RepetitionsConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> PaginatedRepetitionsConfigList | None:
    """API endpoint for reps config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (RepetitionsConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (RepetitionsConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRepetitionsConfigList
    """

    return sync_detailed(
        client=client,
        id=id,
        iteration=iteration,
        limit=limit,
        offset=offset,
        operation=operation,
        ordering=ordering,
        repeat=repeat,
        slot_entry=slot_entry,
        step=step,
        value=value,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    iteration: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    operation: RepetitionsConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: RepetitionsConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> Response[PaginatedRepetitionsConfigList]:
    """API endpoint for reps config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (RepetitionsConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (RepetitionsConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRepetitionsConfigList]
    """

    kwargs = _get_kwargs(
        id=id,
        iteration=iteration,
        limit=limit,
        offset=offset,
        operation=operation,
        ordering=ordering,
        repeat=repeat,
        slot_entry=slot_entry,
        step=step,
        value=value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    iteration: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    operation: RepetitionsConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: RepetitionsConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> PaginatedRepetitionsConfigList | None:
    """API endpoint for reps config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (RepetitionsConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (RepetitionsConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRepetitionsConfigList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            iteration=iteration,
            limit=limit,
            offset=offset,
            operation=operation,
            ordering=ordering,
            repeat=repeat,
            slot_entry=slot_entry,
            step=step,
            value=value,
        )
    ).parsed
