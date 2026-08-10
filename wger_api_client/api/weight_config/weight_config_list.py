from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_weight_config_list import PaginatedWeightConfigList
from ...models.weight_config_list_operation import WeightConfigListOperation
from ...models.weight_config_list_step import WeightConfigListStep
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    iteration: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    operation: WeightConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: WeightConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["iteration"] = iteration

    params["limit"] = limit

    params["offset"] = offset

    json_operation: str | Unset = UNSET
    if not isinstance(operation, Unset):
        json_operation = operation.value

    params["operation"] = json_operation

    params["ordering"] = ordering

    params["repeat"] = repeat

    params["slot_entry"] = slot_entry

    json_step: str | Unset = UNSET
    if not isinstance(step, Unset):
        json_step = step.value

    params["step"] = json_step

    params["value"] = value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/weight-config/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedWeightConfigList | None:
    if response.status_code == 200:
        response_200 = PaginatedWeightConfigList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedWeightConfigList]:
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
    operation: WeightConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: WeightConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> Response[PaginatedWeightConfigList]:
    """API endpoint for weight config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (WeightConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (WeightConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWeightConfigList]
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
    operation: WeightConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: WeightConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> PaginatedWeightConfigList | None:
    """API endpoint for weight config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (WeightConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (WeightConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWeightConfigList
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
    operation: WeightConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: WeightConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> Response[PaginatedWeightConfigList]:
    """API endpoint for weight config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (WeightConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (WeightConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWeightConfigList]
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
    operation: WeightConfigListOperation | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repeat: bool | Unset = UNSET,
    slot_entry: int | Unset = UNSET,
    step: WeightConfigListStep | Unset = UNSET,
    value: float | Unset = UNSET,
) -> PaginatedWeightConfigList | None:
    """API endpoint for weight config objects

    Args:
        id (int | Unset):
        iteration (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        operation (WeightConfigListOperation | Unset):
        ordering (str | Unset):
        repeat (bool | Unset):
        slot_entry (int | Unset):
        step (WeightConfigListStep | Unset):
        value (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWeightConfigList
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
