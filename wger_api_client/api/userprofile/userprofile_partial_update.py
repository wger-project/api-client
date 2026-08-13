from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_userprofile_request import PatchedUserprofileRequest
from ...models.userprofile import Userprofile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchedUserprofileRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/userprofile/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Userprofile | None:
    if response.status_code == 200:
        response_200 = Userprofile.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Userprofile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedUserprofileRequest | Unset = UNSET,
) -> Response[Userprofile]:
    """API endpoint for the user profile

    Every user has exactly one profile, so this endpoint has no list and no
    detail route: it always reads and writes the profile of the logged-in user.
    Updating it takes a PATCH since wger 2.7; up to 2.6 it took a POST.

    Args:
        body (PatchedUserprofileRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userprofile]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PatchedUserprofileRequest | Unset = UNSET,
) -> Userprofile | None:
    """API endpoint for the user profile

    Every user has exactly one profile, so this endpoint has no list and no
    detail route: it always reads and writes the profile of the logged-in user.
    Updating it takes a PATCH since wger 2.7; up to 2.6 it took a POST.

    Args:
        body (PatchedUserprofileRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userprofile
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedUserprofileRequest | Unset = UNSET,
) -> Response[Userprofile]:
    """API endpoint for the user profile

    Every user has exactly one profile, so this endpoint has no list and no
    detail route: it always reads and writes the profile of the logged-in user.
    Updating it takes a PATCH since wger 2.7; up to 2.6 it took a POST.

    Args:
        body (PatchedUserprofileRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userprofile]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PatchedUserprofileRequest | Unset = UNSET,
) -> Userprofile | None:
    """API endpoint for the user profile

    Every user has exactly one profile, so this endpoint has no list and no
    detail route: it always reads and writes the profile of the logged-in user.
    Updating it takes a PATCH since wger 2.7; up to 2.6 it took a POST.

    Args:
        body (PatchedUserprofileRequest | Unset): Workout session serializer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userprofile
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
