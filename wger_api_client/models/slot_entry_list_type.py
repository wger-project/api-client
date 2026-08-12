from typing import Literal

SlotEntryListType = Literal[
    "dropset", "forced", "iso", "jump", "myo", "normal", "partial", "tut", "warmup"
]

SLOT_ENTRY_LIST_TYPE_VALUES: set[SlotEntryListType] = {
    "dropset",
    "forced",
    "iso",
    "jump",
    "myo",
    "normal",
    "partial",
    "tut",
    "warmup",
}


def check_slot_entry_list_type(value: str) -> SlotEntryListType:
    if value in SLOT_ENTRY_LIST_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SLOT_ENTRY_LIST_TYPE_VALUES!r}"
    )
