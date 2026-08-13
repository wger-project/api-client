import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_workout_log_list import PaginatedWorkoutLogList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    exercise: int | Unset = UNSET,
    exercise_in: list[int] | Unset = UNSET,
    iteration: int | Unset = UNSET,
    iteration_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetitions: float | Unset = UNSET,
    repetitions_gt: float | Unset = UNSET,
    repetitions_gte: float | Unset = UNSET,
    repetitions_lt: float | Unset = UNSET,
    repetitions_lte: float | Unset = UNSET,
    repetitions_target: float | Unset = UNSET,
    repetitions_target_gt: float | Unset = UNSET,
    repetitions_target_gte: float | Unset = UNSET,
    repetitions_target_lt: float | Unset = UNSET,
    repetitions_target_lte: float | Unset = UNSET,
    repetitions_unit: int | Unset = UNSET,
    repetitions_unit_in: list[int] | Unset = UNSET,
    rir: float | Unset = UNSET,
    rir_gt: float | Unset = UNSET,
    rir_gte: float | Unset = UNSET,
    rir_in: list[float] | Unset = UNSET,
    rir_lt: float | Unset = UNSET,
    rir_lte: float | Unset = UNSET,
    rir_target: float | Unset = UNSET,
    rir_target_gt: float | Unset = UNSET,
    rir_target_gte: float | Unset = UNSET,
    rir_target_in: list[float] | Unset = UNSET,
    rir_target_lt: float | Unset = UNSET,
    rir_target_lte: float | Unset = UNSET,
    routine: int | Unset = UNSET,
    session: UUID | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
    weight_target: float | Unset = UNSET,
    weight_target_gt: float | Unset = UNSET,
    weight_target_gte: float | Unset = UNSET,
    weight_target_lt: float | Unset = UNSET,
    weight_target_lte: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
    weight_unit_in: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_date_date: str | Unset = UNSET
    if not isinstance(date_date, Unset):
        json_date_date = date_date.isoformat()
    params["date__date"] = json_date_date

    json_date_gt: str | Unset = UNSET
    if not isinstance(date_gt, Unset):
        json_date_gt = date_gt.isoformat()
    params["date__gt"] = json_date_gt

    json_date_gte: str | Unset = UNSET
    if not isinstance(date_gte, Unset):
        json_date_gte = date_gte.isoformat()
    params["date__gte"] = json_date_gte

    json_date_lt: str | Unset = UNSET
    if not isinstance(date_lt, Unset):
        json_date_lt = date_lt.isoformat()
    params["date__lt"] = json_date_lt

    json_date_lte: str | Unset = UNSET
    if not isinstance(date_lte, Unset):
        json_date_lte = date_lte.isoformat()
    params["date__lte"] = json_date_lte

    params["exercise"] = exercise

    json_exercise_in: str | Unset = UNSET
    if not isinstance(exercise_in, Unset):
        json_exercise_in = ",".join(str(v) for v in exercise_in)

    params["exercise__in"] = json_exercise_in

    params["iteration"] = iteration

    json_iteration_in: str | Unset = UNSET
    if not isinstance(iteration_in, Unset):
        json_iteration_in = ",".join(str(v) for v in iteration_in)

    params["iteration__in"] = json_iteration_in

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["repetitions"] = repetitions

    params["repetitions__gt"] = repetitions_gt

    params["repetitions__gte"] = repetitions_gte

    params["repetitions__lt"] = repetitions_lt

    params["repetitions__lte"] = repetitions_lte

    params["repetitions_target"] = repetitions_target

    params["repetitions_target__gt"] = repetitions_target_gt

    params["repetitions_target__gte"] = repetitions_target_gte

    params["repetitions_target__lt"] = repetitions_target_lt

    params["repetitions_target__lte"] = repetitions_target_lte

    params["repetitions_unit"] = repetitions_unit

    json_repetitions_unit_in: str | Unset = UNSET
    if not isinstance(repetitions_unit_in, Unset):
        json_repetitions_unit_in = ",".join(str(v) for v in repetitions_unit_in)

    params["repetitions_unit__in"] = json_repetitions_unit_in

    params["rir"] = rir

    params["rir__gt"] = rir_gt

    params["rir__gte"] = rir_gte

    json_rir_in: str | Unset = UNSET
    if not isinstance(rir_in, Unset):
        json_rir_in = ",".join(str(v) for v in rir_in)

    params["rir__in"] = json_rir_in

    params["rir__lt"] = rir_lt

    params["rir__lte"] = rir_lte

    params["rir_target"] = rir_target

    params["rir_target__gt"] = rir_target_gt

    params["rir_target__gte"] = rir_target_gte

    json_rir_target_in: str | Unset = UNSET
    if not isinstance(rir_target_in, Unset):
        json_rir_target_in = ",".join(str(v) for v in rir_target_in)

    params["rir_target__in"] = json_rir_target_in

    params["rir_target__lt"] = rir_target_lt

    params["rir_target__lte"] = rir_target_lte

    params["routine"] = routine

    json_session: str | Unset = UNSET
    if not isinstance(session, Unset):
        json_session = str(session)
    params["session"] = json_session

    params["weight"] = weight

    params["weight__gt"] = weight_gt

    params["weight__gte"] = weight_gte

    params["weight__lt"] = weight_lt

    params["weight__lte"] = weight_lte

    params["weight_target"] = weight_target

    params["weight_target__gt"] = weight_target_gt

    params["weight_target__gte"] = weight_target_gte

    params["weight_target__lt"] = weight_target_lt

    params["weight_target__lte"] = weight_target_lte

    params["weight_unit"] = weight_unit

    json_weight_unit_in: str | Unset = UNSET
    if not isinstance(weight_unit_in, Unset):
        json_weight_unit_in = ",".join(str(v) for v in weight_unit_in)

    params["weight_unit__in"] = json_weight_unit_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/workoutlog/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedWorkoutLogList | None:
    if response.status_code == 200:
        response_200 = PaginatedWorkoutLogList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedWorkoutLogList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    exercise: int | Unset = UNSET,
    exercise_in: list[int] | Unset = UNSET,
    iteration: int | Unset = UNSET,
    iteration_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetitions: float | Unset = UNSET,
    repetitions_gt: float | Unset = UNSET,
    repetitions_gte: float | Unset = UNSET,
    repetitions_lt: float | Unset = UNSET,
    repetitions_lte: float | Unset = UNSET,
    repetitions_target: float | Unset = UNSET,
    repetitions_target_gt: float | Unset = UNSET,
    repetitions_target_gte: float | Unset = UNSET,
    repetitions_target_lt: float | Unset = UNSET,
    repetitions_target_lte: float | Unset = UNSET,
    repetitions_unit: int | Unset = UNSET,
    repetitions_unit_in: list[int] | Unset = UNSET,
    rir: float | Unset = UNSET,
    rir_gt: float | Unset = UNSET,
    rir_gte: float | Unset = UNSET,
    rir_in: list[float] | Unset = UNSET,
    rir_lt: float | Unset = UNSET,
    rir_lte: float | Unset = UNSET,
    rir_target: float | Unset = UNSET,
    rir_target_gt: float | Unset = UNSET,
    rir_target_gte: float | Unset = UNSET,
    rir_target_in: list[float] | Unset = UNSET,
    rir_target_lt: float | Unset = UNSET,
    rir_target_lte: float | Unset = UNSET,
    routine: int | Unset = UNSET,
    session: UUID | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
    weight_target: float | Unset = UNSET,
    weight_target_gt: float | Unset = UNSET,
    weight_target_gte: float | Unset = UNSET,
    weight_target_lt: float | Unset = UNSET,
    weight_target_lte: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
    weight_unit_in: list[int] | Unset = UNSET,
) -> Response[PaginatedWorkoutLogList]:
    """API endpoint for workout log objects

    Args:
        date (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        exercise (int | Unset):
        exercise_in (list[int] | Unset):
        iteration (int | Unset):
        iteration_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        repetitions (float | Unset):
        repetitions_gt (float | Unset):
        repetitions_gte (float | Unset):
        repetitions_lt (float | Unset):
        repetitions_lte (float | Unset):
        repetitions_target (float | Unset):
        repetitions_target_gt (float | Unset):
        repetitions_target_gte (float | Unset):
        repetitions_target_lt (float | Unset):
        repetitions_target_lte (float | Unset):
        repetitions_unit (int | Unset):
        repetitions_unit_in (list[int] | Unset):
        rir (float | Unset):
        rir_gt (float | Unset):
        rir_gte (float | Unset):
        rir_in (list[float] | Unset):
        rir_lt (float | Unset):
        rir_lte (float | Unset):
        rir_target (float | Unset):
        rir_target_gt (float | Unset):
        rir_target_gte (float | Unset):
        rir_target_in (list[float] | Unset):
        rir_target_lt (float | Unset):
        rir_target_lte (float | Unset):
        routine (int | Unset):
        session (UUID | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):
        weight_target (float | Unset):
        weight_target_gt (float | Unset):
        weight_target_gte (float | Unset):
        weight_target_lt (float | Unset):
        weight_target_lte (float | Unset):
        weight_unit (int | Unset):
        weight_unit_in (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkoutLogList]
    """

    kwargs = _get_kwargs(
        date=date,
        date_date=date_date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        exercise=exercise,
        exercise_in=exercise_in,
        iteration=iteration,
        iteration_in=iteration_in,
        limit=limit,
        offset=offset,
        ordering=ordering,
        repetitions=repetitions,
        repetitions_gt=repetitions_gt,
        repetitions_gte=repetitions_gte,
        repetitions_lt=repetitions_lt,
        repetitions_lte=repetitions_lte,
        repetitions_target=repetitions_target,
        repetitions_target_gt=repetitions_target_gt,
        repetitions_target_gte=repetitions_target_gte,
        repetitions_target_lt=repetitions_target_lt,
        repetitions_target_lte=repetitions_target_lte,
        repetitions_unit=repetitions_unit,
        repetitions_unit_in=repetitions_unit_in,
        rir=rir,
        rir_gt=rir_gt,
        rir_gte=rir_gte,
        rir_in=rir_in,
        rir_lt=rir_lt,
        rir_lte=rir_lte,
        rir_target=rir_target,
        rir_target_gt=rir_target_gt,
        rir_target_gte=rir_target_gte,
        rir_target_in=rir_target_in,
        rir_target_lt=rir_target_lt,
        rir_target_lte=rir_target_lte,
        routine=routine,
        session=session,
        weight=weight,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_target=weight_target,
        weight_target_gt=weight_target_gt,
        weight_target_gte=weight_target_gte,
        weight_target_lt=weight_target_lt,
        weight_target_lte=weight_target_lte,
        weight_unit=weight_unit,
        weight_unit_in=weight_unit_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    exercise: int | Unset = UNSET,
    exercise_in: list[int] | Unset = UNSET,
    iteration: int | Unset = UNSET,
    iteration_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetitions: float | Unset = UNSET,
    repetitions_gt: float | Unset = UNSET,
    repetitions_gte: float | Unset = UNSET,
    repetitions_lt: float | Unset = UNSET,
    repetitions_lte: float | Unset = UNSET,
    repetitions_target: float | Unset = UNSET,
    repetitions_target_gt: float | Unset = UNSET,
    repetitions_target_gte: float | Unset = UNSET,
    repetitions_target_lt: float | Unset = UNSET,
    repetitions_target_lte: float | Unset = UNSET,
    repetitions_unit: int | Unset = UNSET,
    repetitions_unit_in: list[int] | Unset = UNSET,
    rir: float | Unset = UNSET,
    rir_gt: float | Unset = UNSET,
    rir_gte: float | Unset = UNSET,
    rir_in: list[float] | Unset = UNSET,
    rir_lt: float | Unset = UNSET,
    rir_lte: float | Unset = UNSET,
    rir_target: float | Unset = UNSET,
    rir_target_gt: float | Unset = UNSET,
    rir_target_gte: float | Unset = UNSET,
    rir_target_in: list[float] | Unset = UNSET,
    rir_target_lt: float | Unset = UNSET,
    rir_target_lte: float | Unset = UNSET,
    routine: int | Unset = UNSET,
    session: UUID | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
    weight_target: float | Unset = UNSET,
    weight_target_gt: float | Unset = UNSET,
    weight_target_gte: float | Unset = UNSET,
    weight_target_lt: float | Unset = UNSET,
    weight_target_lte: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
    weight_unit_in: list[int] | Unset = UNSET,
) -> PaginatedWorkoutLogList | None:
    """API endpoint for workout log objects

    Args:
        date (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        exercise (int | Unset):
        exercise_in (list[int] | Unset):
        iteration (int | Unset):
        iteration_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        repetitions (float | Unset):
        repetitions_gt (float | Unset):
        repetitions_gte (float | Unset):
        repetitions_lt (float | Unset):
        repetitions_lte (float | Unset):
        repetitions_target (float | Unset):
        repetitions_target_gt (float | Unset):
        repetitions_target_gte (float | Unset):
        repetitions_target_lt (float | Unset):
        repetitions_target_lte (float | Unset):
        repetitions_unit (int | Unset):
        repetitions_unit_in (list[int] | Unset):
        rir (float | Unset):
        rir_gt (float | Unset):
        rir_gte (float | Unset):
        rir_in (list[float] | Unset):
        rir_lt (float | Unset):
        rir_lte (float | Unset):
        rir_target (float | Unset):
        rir_target_gt (float | Unset):
        rir_target_gte (float | Unset):
        rir_target_in (list[float] | Unset):
        rir_target_lt (float | Unset):
        rir_target_lte (float | Unset):
        routine (int | Unset):
        session (UUID | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):
        weight_target (float | Unset):
        weight_target_gt (float | Unset):
        weight_target_gte (float | Unset):
        weight_target_lt (float | Unset):
        weight_target_lte (float | Unset):
        weight_unit (int | Unset):
        weight_unit_in (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkoutLogList
    """

    return sync_detailed(
        client=client,
        date=date,
        date_date=date_date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        exercise=exercise,
        exercise_in=exercise_in,
        iteration=iteration,
        iteration_in=iteration_in,
        limit=limit,
        offset=offset,
        ordering=ordering,
        repetitions=repetitions,
        repetitions_gt=repetitions_gt,
        repetitions_gte=repetitions_gte,
        repetitions_lt=repetitions_lt,
        repetitions_lte=repetitions_lte,
        repetitions_target=repetitions_target,
        repetitions_target_gt=repetitions_target_gt,
        repetitions_target_gte=repetitions_target_gte,
        repetitions_target_lt=repetitions_target_lt,
        repetitions_target_lte=repetitions_target_lte,
        repetitions_unit=repetitions_unit,
        repetitions_unit_in=repetitions_unit_in,
        rir=rir,
        rir_gt=rir_gt,
        rir_gte=rir_gte,
        rir_in=rir_in,
        rir_lt=rir_lt,
        rir_lte=rir_lte,
        rir_target=rir_target,
        rir_target_gt=rir_target_gt,
        rir_target_gte=rir_target_gte,
        rir_target_in=rir_target_in,
        rir_target_lt=rir_target_lt,
        rir_target_lte=rir_target_lte,
        routine=routine,
        session=session,
        weight=weight,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_target=weight_target,
        weight_target_gt=weight_target_gt,
        weight_target_gte=weight_target_gte,
        weight_target_lt=weight_target_lt,
        weight_target_lte=weight_target_lte,
        weight_unit=weight_unit,
        weight_unit_in=weight_unit_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    exercise: int | Unset = UNSET,
    exercise_in: list[int] | Unset = UNSET,
    iteration: int | Unset = UNSET,
    iteration_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetitions: float | Unset = UNSET,
    repetitions_gt: float | Unset = UNSET,
    repetitions_gte: float | Unset = UNSET,
    repetitions_lt: float | Unset = UNSET,
    repetitions_lte: float | Unset = UNSET,
    repetitions_target: float | Unset = UNSET,
    repetitions_target_gt: float | Unset = UNSET,
    repetitions_target_gte: float | Unset = UNSET,
    repetitions_target_lt: float | Unset = UNSET,
    repetitions_target_lte: float | Unset = UNSET,
    repetitions_unit: int | Unset = UNSET,
    repetitions_unit_in: list[int] | Unset = UNSET,
    rir: float | Unset = UNSET,
    rir_gt: float | Unset = UNSET,
    rir_gte: float | Unset = UNSET,
    rir_in: list[float] | Unset = UNSET,
    rir_lt: float | Unset = UNSET,
    rir_lte: float | Unset = UNSET,
    rir_target: float | Unset = UNSET,
    rir_target_gt: float | Unset = UNSET,
    rir_target_gte: float | Unset = UNSET,
    rir_target_in: list[float] | Unset = UNSET,
    rir_target_lt: float | Unset = UNSET,
    rir_target_lte: float | Unset = UNSET,
    routine: int | Unset = UNSET,
    session: UUID | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
    weight_target: float | Unset = UNSET,
    weight_target_gt: float | Unset = UNSET,
    weight_target_gte: float | Unset = UNSET,
    weight_target_lt: float | Unset = UNSET,
    weight_target_lte: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
    weight_unit_in: list[int] | Unset = UNSET,
) -> Response[PaginatedWorkoutLogList]:
    """API endpoint for workout log objects

    Args:
        date (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        exercise (int | Unset):
        exercise_in (list[int] | Unset):
        iteration (int | Unset):
        iteration_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        repetitions (float | Unset):
        repetitions_gt (float | Unset):
        repetitions_gte (float | Unset):
        repetitions_lt (float | Unset):
        repetitions_lte (float | Unset):
        repetitions_target (float | Unset):
        repetitions_target_gt (float | Unset):
        repetitions_target_gte (float | Unset):
        repetitions_target_lt (float | Unset):
        repetitions_target_lte (float | Unset):
        repetitions_unit (int | Unset):
        repetitions_unit_in (list[int] | Unset):
        rir (float | Unset):
        rir_gt (float | Unset):
        rir_gte (float | Unset):
        rir_in (list[float] | Unset):
        rir_lt (float | Unset):
        rir_lte (float | Unset):
        rir_target (float | Unset):
        rir_target_gt (float | Unset):
        rir_target_gte (float | Unset):
        rir_target_in (list[float] | Unset):
        rir_target_lt (float | Unset):
        rir_target_lte (float | Unset):
        routine (int | Unset):
        session (UUID | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):
        weight_target (float | Unset):
        weight_target_gt (float | Unset):
        weight_target_gte (float | Unset):
        weight_target_lt (float | Unset):
        weight_target_lte (float | Unset):
        weight_unit (int | Unset):
        weight_unit_in (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkoutLogList]
    """

    kwargs = _get_kwargs(
        date=date,
        date_date=date_date,
        date_gt=date_gt,
        date_gte=date_gte,
        date_lt=date_lt,
        date_lte=date_lte,
        exercise=exercise,
        exercise_in=exercise_in,
        iteration=iteration,
        iteration_in=iteration_in,
        limit=limit,
        offset=offset,
        ordering=ordering,
        repetitions=repetitions,
        repetitions_gt=repetitions_gt,
        repetitions_gte=repetitions_gte,
        repetitions_lt=repetitions_lt,
        repetitions_lte=repetitions_lte,
        repetitions_target=repetitions_target,
        repetitions_target_gt=repetitions_target_gt,
        repetitions_target_gte=repetitions_target_gte,
        repetitions_target_lt=repetitions_target_lt,
        repetitions_target_lte=repetitions_target_lte,
        repetitions_unit=repetitions_unit,
        repetitions_unit_in=repetitions_unit_in,
        rir=rir,
        rir_gt=rir_gt,
        rir_gte=rir_gte,
        rir_in=rir_in,
        rir_lt=rir_lt,
        rir_lte=rir_lte,
        rir_target=rir_target,
        rir_target_gt=rir_target_gt,
        rir_target_gte=rir_target_gte,
        rir_target_in=rir_target_in,
        rir_target_lt=rir_target_lt,
        rir_target_lte=rir_target_lte,
        routine=routine,
        session=session,
        weight=weight,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_target=weight_target,
        weight_target_gt=weight_target_gt,
        weight_target_gte=weight_target_gte,
        weight_target_lt=weight_target_lt,
        weight_target_lte=weight_target_lte,
        weight_unit=weight_unit,
        weight_unit_in=weight_unit_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    exercise: int | Unset = UNSET,
    exercise_in: list[int] | Unset = UNSET,
    iteration: int | Unset = UNSET,
    iteration_in: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    repetitions: float | Unset = UNSET,
    repetitions_gt: float | Unset = UNSET,
    repetitions_gte: float | Unset = UNSET,
    repetitions_lt: float | Unset = UNSET,
    repetitions_lte: float | Unset = UNSET,
    repetitions_target: float | Unset = UNSET,
    repetitions_target_gt: float | Unset = UNSET,
    repetitions_target_gte: float | Unset = UNSET,
    repetitions_target_lt: float | Unset = UNSET,
    repetitions_target_lte: float | Unset = UNSET,
    repetitions_unit: int | Unset = UNSET,
    repetitions_unit_in: list[int] | Unset = UNSET,
    rir: float | Unset = UNSET,
    rir_gt: float | Unset = UNSET,
    rir_gte: float | Unset = UNSET,
    rir_in: list[float] | Unset = UNSET,
    rir_lt: float | Unset = UNSET,
    rir_lte: float | Unset = UNSET,
    rir_target: float | Unset = UNSET,
    rir_target_gt: float | Unset = UNSET,
    rir_target_gte: float | Unset = UNSET,
    rir_target_in: list[float] | Unset = UNSET,
    rir_target_lt: float | Unset = UNSET,
    rir_target_lte: float | Unset = UNSET,
    routine: int | Unset = UNSET,
    session: UUID | Unset = UNSET,
    weight: float | Unset = UNSET,
    weight_gt: float | Unset = UNSET,
    weight_gte: float | Unset = UNSET,
    weight_lt: float | Unset = UNSET,
    weight_lte: float | Unset = UNSET,
    weight_target: float | Unset = UNSET,
    weight_target_gt: float | Unset = UNSET,
    weight_target_gte: float | Unset = UNSET,
    weight_target_lt: float | Unset = UNSET,
    weight_target_lte: float | Unset = UNSET,
    weight_unit: int | Unset = UNSET,
    weight_unit_in: list[int] | Unset = UNSET,
) -> PaginatedWorkoutLogList | None:
    """API endpoint for workout log objects

    Args:
        date (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        exercise (int | Unset):
        exercise_in (list[int] | Unset):
        iteration (int | Unset):
        iteration_in (list[int] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        repetitions (float | Unset):
        repetitions_gt (float | Unset):
        repetitions_gte (float | Unset):
        repetitions_lt (float | Unset):
        repetitions_lte (float | Unset):
        repetitions_target (float | Unset):
        repetitions_target_gt (float | Unset):
        repetitions_target_gte (float | Unset):
        repetitions_target_lt (float | Unset):
        repetitions_target_lte (float | Unset):
        repetitions_unit (int | Unset):
        repetitions_unit_in (list[int] | Unset):
        rir (float | Unset):
        rir_gt (float | Unset):
        rir_gte (float | Unset):
        rir_in (list[float] | Unset):
        rir_lt (float | Unset):
        rir_lte (float | Unset):
        rir_target (float | Unset):
        rir_target_gt (float | Unset):
        rir_target_gte (float | Unset):
        rir_target_in (list[float] | Unset):
        rir_target_lt (float | Unset):
        rir_target_lte (float | Unset):
        routine (int | Unset):
        session (UUID | Unset):
        weight (float | Unset):
        weight_gt (float | Unset):
        weight_gte (float | Unset):
        weight_lt (float | Unset):
        weight_lte (float | Unset):
        weight_target (float | Unset):
        weight_target_gt (float | Unset):
        weight_target_gte (float | Unset):
        weight_target_lt (float | Unset):
        weight_target_lte (float | Unset):
        weight_unit (int | Unset):
        weight_unit_in (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkoutLogList
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            date_date=date_date,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            exercise=exercise,
            exercise_in=exercise_in,
            iteration=iteration,
            iteration_in=iteration_in,
            limit=limit,
            offset=offset,
            ordering=ordering,
            repetitions=repetitions,
            repetitions_gt=repetitions_gt,
            repetitions_gte=repetitions_gte,
            repetitions_lt=repetitions_lt,
            repetitions_lte=repetitions_lte,
            repetitions_target=repetitions_target,
            repetitions_target_gt=repetitions_target_gt,
            repetitions_target_gte=repetitions_target_gte,
            repetitions_target_lt=repetitions_target_lt,
            repetitions_target_lte=repetitions_target_lte,
            repetitions_unit=repetitions_unit,
            repetitions_unit_in=repetitions_unit_in,
            rir=rir,
            rir_gt=rir_gt,
            rir_gte=rir_gte,
            rir_in=rir_in,
            rir_lt=rir_lt,
            rir_lte=rir_lte,
            rir_target=rir_target,
            rir_target_gt=rir_target_gt,
            rir_target_gte=rir_target_gte,
            rir_target_in=rir_target_in,
            rir_target_lt=rir_target_lt,
            rir_target_lte=rir_target_lte,
            routine=routine,
            session=session,
            weight=weight,
            weight_gt=weight_gt,
            weight_gte=weight_gte,
            weight_lt=weight_lt,
            weight_lte=weight_lte,
            weight_target=weight_target,
            weight_target_gt=weight_target_gt,
            weight_target_gte=weight_target_gte,
            weight_target_lt=weight_target_lt,
            weight_target_lte=weight_target_lte,
            weight_unit=weight_unit,
            weight_unit_in=weight_unit_in,
        )
    ).parsed
