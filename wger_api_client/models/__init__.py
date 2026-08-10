"""Contains all the data models used in inputs/outputs"""

from .blank_enum import BlankEnum
from .category import Category
from .category_request import CategoryRequest
from .day import Day
from .day_request import DayRequest
from .day_structure import DayStructure
from .day_type_enum import DayTypeEnum
from .deletion_log import DeletionLog
from .deletion_log_list_model_type import DeletionLogListModelType
from .equipment import Equipment
from .exercise import Exercise
from .exercise_alias import ExerciseAlias
from .exercise_alias_request import ExerciseAliasRequest
from .exercise_category import ExerciseCategory
from .exercise_comment import ExerciseComment
from .exercise_comment_request import ExerciseCommentRequest
from .exercise_image import ExerciseImage
from .exercise_image_request import ExerciseImageRequest
from .exercise_info import ExerciseInfo
from .exercise_info_alias import ExerciseInfoAlias
from .exercise_request import ExerciseRequest
from .exercise_submission import ExerciseSubmission
from .exercise_submission_request import ExerciseSubmissionRequest
from .exercise_translation import ExerciseTranslation
from .exercise_translation_info import ExerciseTranslationInfo
from .exercise_translation_request import ExerciseTranslationRequest
from .exercise_translation_submission import ExerciseTranslationSubmission
from .exercise_translation_submission_request import (
    ExerciseTranslationSubmissionRequest,
)
from .exercise_type_enum import ExerciseTypeEnum
from .exercise_video import ExerciseVideo
from .exercise_video_info import ExerciseVideoInfo
from .exercise_video_request import ExerciseVideoRequest
from .gender_enum import GenderEnum
from .grouped_log_data import GroupedLogData
from .grouped_log_data_daily import GroupedLogDataDaily
from .grouped_log_data_iteration import GroupedLogDataIteration
from .grouped_log_data_weekly import GroupedLogDataWeekly
from .image import Image
from .image_request import ImageRequest
from .impression_enum import ImpressionEnum
from .ingredient import Ingredient
from .ingredient_image import IngredientImage
from .ingredient_info import IngredientInfo
from .ingredient_list_nutri_score import IngredientListNutriScore
from .ingredient_sync_list_nutri_score import IngredientSyncListNutriScore
from .ingredient_values import IngredientValues
from .ingredient_values_errors import IngredientValuesErrors
from .ingredient_weight_unit import IngredientWeightUnit
from .ingredientinfo_list_nutri_score import IngredientinfoListNutriScore
from .intensity_enum import IntensityEnum
from .language import Language
from .language_check_request import LanguageCheckRequest
from .language_check_response import LanguageCheckResponse
from .license_ import License
from .log_data import LogData
from .log_data_exercises import LogDataExercises
from .log_data_muscle import LogDataMuscle
from .log_display import LogDisplay
from .log_item import LogItem
from .log_item_request import LogItemRequest
from .log_stats_data import LogStatsData
from .max_repetitions_config import MaxRepetitionsConfig
from .max_repetitions_config_list_operation import MaxRepetitionsConfigListOperation
from .max_repetitions_config_list_step import MaxRepetitionsConfigListStep
from .max_repetitions_config_request import MaxRepetitionsConfigRequest
from .max_rest_config import MaxRestConfig
from .max_rest_config_list_operation import MaxRestConfigListOperation
from .max_rest_config_list_step import MaxRestConfigListStep
from .max_rest_config_request import MaxRestConfigRequest
from .max_ri_r_config import MaxRiRConfig
from .max_ri_r_config_request import MaxRiRConfigRequest
from .max_rir_config_list_operation import MaxRirConfigListOperation
from .max_rir_config_list_step import MaxRirConfigListStep
from .max_set_nr_config import MaxSetNrConfig
from .max_set_nr_config_request import MaxSetNrConfigRequest
from .max_sets_config_list_operation import MaxSetsConfigListOperation
from .max_sets_config_list_step import MaxSetsConfigListStep
from .max_weight_config import MaxWeightConfig
from .max_weight_config_list_operation import MaxWeightConfigListOperation
from .max_weight_config_list_step import MaxWeightConfigListStep
from .max_weight_config_request import MaxWeightConfigRequest
from .meal import Meal
from .meal_info import MealInfo
from .meal_item import MealItem
from .meal_item_info import MealItemInfo
from .meal_item_request import MealItemRequest
from .meal_request import MealRequest
from .measurement import Measurement
from .measurement_request import MeasurementRequest
from .model_type_enum import ModelTypeEnum
from .muscle import Muscle
from .nutriscore_enum import NutriscoreEnum
from .nutrition_plan import NutritionPlan
from .nutrition_plan_info import NutritionPlanInfo
from .nutrition_plan_request import NutritionPlanRequest
from .nutritional_values import NutritionalValues
from .operation_enum import OperationEnum
from .paginated_category_list import PaginatedCategoryList
from .paginated_day_list import PaginatedDayList
from .paginated_deletion_log_list import PaginatedDeletionLogList
from .paginated_equipment_list import PaginatedEquipmentList
from .paginated_exercise_alias_list import PaginatedExerciseAliasList
from .paginated_exercise_category_list import PaginatedExerciseCategoryList
from .paginated_exercise_comment_list import PaginatedExerciseCommentList
from .paginated_exercise_image_list import PaginatedExerciseImageList
from .paginated_exercise_info_list import PaginatedExerciseInfoList
from .paginated_exercise_list import PaginatedExerciseList
from .paginated_exercise_translation_list import PaginatedExerciseTranslationList
from .paginated_exercise_video_list import PaginatedExerciseVideoList
from .paginated_image_list import PaginatedImageList
from .paginated_ingredient_image_list import PaginatedIngredientImageList
from .paginated_ingredient_info_list import PaginatedIngredientInfoList
from .paginated_ingredient_list import PaginatedIngredientList
from .paginated_ingredient_weight_unit_list import PaginatedIngredientWeightUnitList
from .paginated_language_list import PaginatedLanguageList
from .paginated_license_list import PaginatedLicenseList
from .paginated_log_item_list import PaginatedLogItemList
from .paginated_max_repetitions_config_list import PaginatedMaxRepetitionsConfigList
from .paginated_max_rest_config_list import PaginatedMaxRestConfigList
from .paginated_max_ri_r_config_list import PaginatedMaxRiRConfigList
from .paginated_max_set_nr_config_list import PaginatedMaxSetNrConfigList
from .paginated_max_weight_config_list import PaginatedMaxWeightConfigList
from .paginated_meal_item_list import PaginatedMealItemList
from .paginated_meal_list import PaginatedMealList
from .paginated_measurement_list import PaginatedMeasurementList
from .paginated_muscle_list import PaginatedMuscleList
from .paginated_nutrition_plan_info_list import PaginatedNutritionPlanInfoList
from .paginated_nutrition_plan_list import PaginatedNutritionPlanList
from .paginated_repetition_unit_list import PaginatedRepetitionUnitList
from .paginated_repetitions_config_list import PaginatedRepetitionsConfigList
from .paginated_rest_config_list import PaginatedRestConfigList
from .paginated_ri_r_config_list import PaginatedRiRConfigList
from .paginated_routine_list import PaginatedRoutineList
from .paginated_routine_weight_unit_list import PaginatedRoutineWeightUnitList
from .paginated_set_nr_config_list import PaginatedSetNrConfigList
from .paginated_slot_entry_list import PaginatedSlotEntryList
from .paginated_slot_list import PaginatedSlotList
from .paginated_trophy_list import PaginatedTrophyList
from .paginated_trophy_progress_list import PaginatedTrophyProgressList
from .paginated_user_statistics_list import PaginatedUserStatisticsList
from .paginated_user_trophy_list import PaginatedUserTrophyList
from .paginated_weight_config_list import PaginatedWeightConfigList
from .paginated_weight_entry_list import PaginatedWeightEntryList
from .paginated_workout_log_list import PaginatedWorkoutLogList
from .paginated_workout_session_list import PaginatedWorkoutSessionList
from .patched_category_request import PatchedCategoryRequest
from .patched_day_request import PatchedDayRequest
from .patched_exercise_alias_request import PatchedExerciseAliasRequest
from .patched_exercise_comment_request import PatchedExerciseCommentRequest
from .patched_exercise_image_request import PatchedExerciseImageRequest
from .patched_exercise_request import PatchedExerciseRequest
from .patched_exercise_translation_request import PatchedExerciseTranslationRequest
from .patched_exercise_video_request import PatchedExerciseVideoRequest
from .patched_image_request import PatchedImageRequest
from .patched_log_item_request import PatchedLogItemRequest
from .patched_max_repetitions_config_request import PatchedMaxRepetitionsConfigRequest
from .patched_max_rest_config_request import PatchedMaxRestConfigRequest
from .patched_max_ri_r_config_request import PatchedMaxRiRConfigRequest
from .patched_max_set_nr_config_request import PatchedMaxSetNrConfigRequest
from .patched_max_weight_config_request import PatchedMaxWeightConfigRequest
from .patched_meal_item_request import PatchedMealItemRequest
from .patched_meal_request import PatchedMealRequest
from .patched_measurement_request import PatchedMeasurementRequest
from .patched_nutrition_plan_request import PatchedNutritionPlanRequest
from .patched_powersync_upload_request import PatchedPowersyncUploadRequest
from .patched_repetitions_config_request import PatchedRepetitionsConfigRequest
from .patched_rest_config_request import PatchedRestConfigRequest
from .patched_ri_r_config_request import PatchedRiRConfigRequest
from .patched_routine_request import PatchedRoutineRequest
from .patched_set_nr_config_request import PatchedSetNrConfigRequest
from .patched_slot_entry_request import PatchedSlotEntryRequest
from .patched_slot_request import PatchedSlotRequest
from .patched_userprofile_request import PatchedUserprofileRequest
from .patched_weight_config_request import PatchedWeightConfigRequest
from .patched_weight_entry_request import PatchedWeightEntryRequest
from .patched_workout_log_request import PatchedWorkoutLogRequest
from .patched_workout_session_request import PatchedWorkoutSessionRequest
from .permission_response import PermissionResponse
from .powersync_keys_response import PowersyncKeysResponse
from .powersync_keys_response_keys_item import PowersyncKeysResponseKeysItem
from .powersync_token_response import PowersyncTokenResponse
from .powersync_upload_request import PowersyncUploadRequest
from .powersync_upload_response import PowersyncUploadResponse
from .refresh_token_response import RefreshTokenResponse
from .repetition_unit import RepetitionUnit
from .repetitions_config import RepetitionsConfig
from .repetitions_config_list_operation import RepetitionsConfigListOperation
from .repetitions_config_list_step import RepetitionsConfigListStep
from .repetitions_config_request import RepetitionsConfigRequest
from .rest_config import RestConfig
from .rest_config_list_operation import RestConfigListOperation
from .rest_config_list_step import RestConfigListStep
from .rest_config_request import RestConfigRequest
from .ri_r_config import RiRConfig
from .ri_r_config_request import RiRConfigRequest
from .rir_config_list_operation import RirConfigListOperation
from .rir_config_list_step import RirConfigListStep
from .routine import Routine
from .routine_request import RoutineRequest
from .routine_structure import RoutineStructure
from .routine_weight_unit import RoutineWeightUnit
from .schema_retrieve_format import SchemaRetrieveFormat
from .schema_retrieve_lang import SchemaRetrieveLang
from .schema_retrieve_response_200 import SchemaRetrieveResponse200
from .set_config_data import SetConfigData
from .set_nr_config import SetNrConfig
from .set_nr_config_request import SetNrConfigRequest
from .sets_config_list_operation import SetsConfigListOperation
from .sets_config_list_step import SetsConfigListStep
from .slot import Slot
from .slot_data import SlotData
from .slot_entry import SlotEntry
from .slot_entry_list_type import SlotEntryListType
from .slot_entry_request import SlotEntryRequest
from .slot_entry_structure import SlotEntryStructure
from .slot_request import SlotRequest
from .slot_structure import SlotStructure
from .step_enum import StepEnum
from .style_enum import StyleEnum
from .thumbnails import Thumbnails
from .token_refresh import TokenRefresh
from .token_refresh_request import TokenRefreshRequest
from .token_verify_request import TokenVerifyRequest
from .trophy import Trophy
from .trophy_list_trophy_type import TrophyListTrophyType
from .trophy_progress import TrophyProgress
from .trophy_progress_list_trophy_type import TrophyProgressListTrophyType
from .trophy_type_enum import TrophyTypeEnum
from .unit_type_enum import UnitTypeEnum
from .user_statistics import UserStatistics
from .user_trophy import UserTrophy
from .user_trophy_list_trophy_trophy_type import UserTrophyListTrophyTrophyType
from .userprofile import Userprofile
from .userprofile_request import UserprofileRequest
from .verify_email_response import VerifyEmailResponse
from .weight_config import WeightConfig
from .weight_config_list_operation import WeightConfigListOperation
from .weight_config_list_step import WeightConfigListStep
from .weight_config_request import WeightConfigRequest
from .weight_entry import WeightEntry
from .weight_entry_request import WeightEntryRequest
from .weight_unit_enum import WeightUnitEnum
from .workout_day_data_display_mode import WorkoutDayDataDisplayMode
from .workout_day_data_gym_mode import WorkoutDayDataGymMode
from .workout_log import WorkoutLog
from .workout_log_request import WorkoutLogRequest
from .workout_session import WorkoutSession
from .workout_session_request import WorkoutSessionRequest
from .workoutsession_list_general_impression import WorkoutsessionListGeneralImpression

__all__ = (
    "BlankEnum",
    "Category",
    "CategoryRequest",
    "Day",
    "DayRequest",
    "DayStructure",
    "DayTypeEnum",
    "DeletionLog",
    "DeletionLogListModelType",
    "Equipment",
    "Exercise",
    "ExerciseAlias",
    "ExerciseAliasRequest",
    "ExerciseCategory",
    "ExerciseComment",
    "ExerciseCommentRequest",
    "ExerciseImage",
    "ExerciseImageRequest",
    "ExerciseInfo",
    "ExerciseInfoAlias",
    "ExerciseRequest",
    "ExerciseSubmission",
    "ExerciseSubmissionRequest",
    "ExerciseTranslation",
    "ExerciseTranslationInfo",
    "ExerciseTranslationRequest",
    "ExerciseTranslationSubmission",
    "ExerciseTranslationSubmissionRequest",
    "ExerciseTypeEnum",
    "ExerciseVideo",
    "ExerciseVideoInfo",
    "ExerciseVideoRequest",
    "GenderEnum",
    "GroupedLogData",
    "GroupedLogDataDaily",
    "GroupedLogDataIteration",
    "GroupedLogDataWeekly",
    "Image",
    "ImageRequest",
    "ImpressionEnum",
    "Ingredient",
    "IngredientImage",
    "IngredientInfo",
    "IngredientListNutriScore",
    "IngredientSyncListNutriScore",
    "IngredientValues",
    "IngredientValuesErrors",
    "IngredientWeightUnit",
    "IngredientinfoListNutriScore",
    "IntensityEnum",
    "Language",
    "LanguageCheckRequest",
    "LanguageCheckResponse",
    "License",
    "LogData",
    "LogDataExercises",
    "LogDataMuscle",
    "LogDisplay",
    "LogItem",
    "LogItemRequest",
    "LogStatsData",
    "MaxRepetitionsConfig",
    "MaxRepetitionsConfigListOperation",
    "MaxRepetitionsConfigListStep",
    "MaxRepetitionsConfigRequest",
    "MaxRestConfig",
    "MaxRestConfigListOperation",
    "MaxRestConfigListStep",
    "MaxRestConfigRequest",
    "MaxRiRConfig",
    "MaxRiRConfigRequest",
    "MaxRirConfigListOperation",
    "MaxRirConfigListStep",
    "MaxSetNrConfig",
    "MaxSetNrConfigRequest",
    "MaxSetsConfigListOperation",
    "MaxSetsConfigListStep",
    "MaxWeightConfig",
    "MaxWeightConfigListOperation",
    "MaxWeightConfigListStep",
    "MaxWeightConfigRequest",
    "Meal",
    "MealInfo",
    "MealItem",
    "MealItemInfo",
    "MealItemRequest",
    "MealRequest",
    "Measurement",
    "MeasurementRequest",
    "ModelTypeEnum",
    "Muscle",
    "NutriscoreEnum",
    "NutritionPlan",
    "NutritionPlanInfo",
    "NutritionPlanRequest",
    "NutritionalValues",
    "OperationEnum",
    "PaginatedCategoryList",
    "PaginatedDayList",
    "PaginatedDeletionLogList",
    "PaginatedEquipmentList",
    "PaginatedExerciseAliasList",
    "PaginatedExerciseCategoryList",
    "PaginatedExerciseCommentList",
    "PaginatedExerciseImageList",
    "PaginatedExerciseInfoList",
    "PaginatedExerciseList",
    "PaginatedExerciseTranslationList",
    "PaginatedExerciseVideoList",
    "PaginatedImageList",
    "PaginatedIngredientImageList",
    "PaginatedIngredientInfoList",
    "PaginatedIngredientList",
    "PaginatedIngredientWeightUnitList",
    "PaginatedLanguageList",
    "PaginatedLicenseList",
    "PaginatedLogItemList",
    "PaginatedMaxRepetitionsConfigList",
    "PaginatedMaxRestConfigList",
    "PaginatedMaxRiRConfigList",
    "PaginatedMaxSetNrConfigList",
    "PaginatedMaxWeightConfigList",
    "PaginatedMealItemList",
    "PaginatedMealList",
    "PaginatedMeasurementList",
    "PaginatedMuscleList",
    "PaginatedNutritionPlanInfoList",
    "PaginatedNutritionPlanList",
    "PaginatedRepetitionUnitList",
    "PaginatedRepetitionsConfigList",
    "PaginatedRestConfigList",
    "PaginatedRiRConfigList",
    "PaginatedRoutineList",
    "PaginatedRoutineWeightUnitList",
    "PaginatedSetNrConfigList",
    "PaginatedSlotEntryList",
    "PaginatedSlotList",
    "PaginatedTrophyList",
    "PaginatedTrophyProgressList",
    "PaginatedUserStatisticsList",
    "PaginatedUserTrophyList",
    "PaginatedWeightConfigList",
    "PaginatedWeightEntryList",
    "PaginatedWorkoutLogList",
    "PaginatedWorkoutSessionList",
    "PatchedCategoryRequest",
    "PatchedDayRequest",
    "PatchedExerciseAliasRequest",
    "PatchedExerciseCommentRequest",
    "PatchedExerciseImageRequest",
    "PatchedExerciseRequest",
    "PatchedExerciseTranslationRequest",
    "PatchedExerciseVideoRequest",
    "PatchedImageRequest",
    "PatchedLogItemRequest",
    "PatchedMaxRepetitionsConfigRequest",
    "PatchedMaxRestConfigRequest",
    "PatchedMaxRiRConfigRequest",
    "PatchedMaxSetNrConfigRequest",
    "PatchedMaxWeightConfigRequest",
    "PatchedMealItemRequest",
    "PatchedMealRequest",
    "PatchedMeasurementRequest",
    "PatchedNutritionPlanRequest",
    "PatchedPowersyncUploadRequest",
    "PatchedRepetitionsConfigRequest",
    "PatchedRestConfigRequest",
    "PatchedRiRConfigRequest",
    "PatchedRoutineRequest",
    "PatchedSetNrConfigRequest",
    "PatchedSlotEntryRequest",
    "PatchedSlotRequest",
    "PatchedUserprofileRequest",
    "PatchedWeightConfigRequest",
    "PatchedWeightEntryRequest",
    "PatchedWorkoutLogRequest",
    "PatchedWorkoutSessionRequest",
    "PermissionResponse",
    "PowersyncKeysResponse",
    "PowersyncKeysResponseKeysItem",
    "PowersyncTokenResponse",
    "PowersyncUploadRequest",
    "PowersyncUploadResponse",
    "RefreshTokenResponse",
    "RepetitionUnit",
    "RepetitionsConfig",
    "RepetitionsConfigListOperation",
    "RepetitionsConfigListStep",
    "RepetitionsConfigRequest",
    "RestConfig",
    "RestConfigListOperation",
    "RestConfigListStep",
    "RestConfigRequest",
    "RiRConfig",
    "RiRConfigRequest",
    "RirConfigListOperation",
    "RirConfigListStep",
    "Routine",
    "RoutineRequest",
    "RoutineStructure",
    "RoutineWeightUnit",
    "SchemaRetrieveFormat",
    "SchemaRetrieveLang",
    "SchemaRetrieveResponse200",
    "SetConfigData",
    "SetNrConfig",
    "SetNrConfigRequest",
    "SetsConfigListOperation",
    "SetsConfigListStep",
    "Slot",
    "SlotData",
    "SlotEntry",
    "SlotEntryListType",
    "SlotEntryRequest",
    "SlotEntryStructure",
    "SlotRequest",
    "SlotStructure",
    "StepEnum",
    "StyleEnum",
    "Thumbnails",
    "TokenRefresh",
    "TokenRefreshRequest",
    "TokenVerifyRequest",
    "Trophy",
    "TrophyListTrophyType",
    "TrophyProgress",
    "TrophyProgressListTrophyType",
    "TrophyTypeEnum",
    "UnitTypeEnum",
    "UserStatistics",
    "UserTrophy",
    "UserTrophyListTrophyTrophyType",
    "Userprofile",
    "UserprofileRequest",
    "VerifyEmailResponse",
    "WeightConfig",
    "WeightConfigListOperation",
    "WeightConfigListStep",
    "WeightConfigRequest",
    "WeightEntry",
    "WeightEntryRequest",
    "WeightUnitEnum",
    "WorkoutDayDataDisplayMode",
    "WorkoutDayDataGymMode",
    "WorkoutLog",
    "WorkoutLogRequest",
    "WorkoutSession",
    "WorkoutSessionRequest",
    "WorkoutsessionListGeneralImpression",
)
