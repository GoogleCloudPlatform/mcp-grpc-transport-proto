import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProtocolVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION_UNKNOWN: _ClassVar[ProtocolVersion]
    VERSION_20250326: _ClassVar[ProtocolVersion]
    VERSION_20250618: _ClassVar[ProtocolVersion]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_LEVEL_UNKNOWN: _ClassVar[LogLevel]
    LOG_LEVEL_DEBUG: _ClassVar[LogLevel]
    LOG_LEVEL_INFO: _ClassVar[LogLevel]
    LOG_LEVEL_NOTICE: _ClassVar[LogLevel]
    LOG_LEVEL_WARNING: _ClassVar[LogLevel]
    LOG_LEVEL_ERROR: _ClassVar[LogLevel]
    LOG_LEVEL_CRITICAL: _ClassVar[LogLevel]
    LOG_LEVEL_ALERT: _ClassVar[LogLevel]
    LOG_LEVEL_EMERGENCY: _ClassVar[LogLevel]

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNKNOWN: _ClassVar[Role]
    ROLE_USER: _ClassVar[Role]
    ROLE_ASSISTANT: _ClassVar[Role]
VERSION_UNKNOWN: ProtocolVersion
VERSION_20250326: ProtocolVersion
VERSION_20250618: ProtocolVersion
LOG_LEVEL_UNKNOWN: LogLevel
LOG_LEVEL_DEBUG: LogLevel
LOG_LEVEL_INFO: LogLevel
LOG_LEVEL_NOTICE: LogLevel
LOG_LEVEL_WARNING: LogLevel
LOG_LEVEL_ERROR: LogLevel
LOG_LEVEL_CRITICAL: LogLevel
LOG_LEVEL_ALERT: LogLevel
LOG_LEVEL_EMERGENCY: LogLevel
ROLE_UNKNOWN: Role
ROLE_USER: Role
ROLE_ASSISTANT: Role

class ProgressNotification(_message.Message):
    __slots__ = ("progress_token", "progress", "total", "message")
    PROGRESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    progress_token: str
    progress: float
    total: float
    message: str
    def __init__(self, progress_token: _Optional[str] = ..., progress: _Optional[float] = ..., total: _Optional[float] = ..., message: _Optional[str] = ...) -> None: ...

class LogMessage(_message.Message):
    __slots__ = ("log_level", "logger", "data")
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LOGGER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    log_level: LogLevel
    logger: str
    data: _struct_pb2.Value
    def __init__(self, log_level: _Optional[_Union[LogLevel, str]] = ..., logger: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ServerInitiatedRequest(_message.Message):
    __slots__ = ("sampling_create_message", "list_roots_request", "notify_on_root_list_update", "elicit_request")
    SAMPLING_CREATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LIST_ROOTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ON_ROOT_LIST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ELICIT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    sampling_create_message: SamplingCreateMessageRequest
    list_roots_request: ListRootsRequest
    notify_on_root_list_update: bool
    elicit_request: ElicitRequest
    def __init__(self, sampling_create_message: _Optional[_Union[SamplingCreateMessageRequest, _Mapping]] = ..., list_roots_request: _Optional[_Union[ListRootsRequest, _Mapping]] = ..., notify_on_root_list_update: bool = ..., elicit_request: _Optional[_Union[ElicitRequest, _Mapping]] = ...) -> None: ...

class ServerInitiatedResponse(_message.Message):
    __slots__ = ("sampling_create_message_result", "root_list_result", "elicit_result")
    SAMPLING_CREATE_MESSAGE_RESULT_FIELD_NUMBER: _ClassVar[int]
    ROOT_LIST_RESULT_FIELD_NUMBER: _ClassVar[int]
    ELICIT_RESULT_FIELD_NUMBER: _ClassVar[int]
    sampling_create_message_result: SamplingCreateMessageResult
    root_list_result: ListRootsResult
    elicit_result: ElicitResult
    def __init__(self, sampling_create_message_result: _Optional[_Union[SamplingCreateMessageResult, _Mapping]] = ..., root_list_result: _Optional[_Union[ListRootsResult, _Mapping]] = ..., elicit_result: _Optional[_Union[ElicitResult, _Mapping]] = ...) -> None: ...

class RequestFields(_message.Message):
    __slots__ = ("metadata", "cursor", "progress", "log_level", "task_id", "dependent_responses", "resume_data")
    class DependentResponsesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ServerInitiatedResponse
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ServerInitiatedResponse, _Mapping]] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    RESUME_DATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _struct_pb2.Struct
    cursor: str
    progress: ProgressNotification
    log_level: LogLevel
    task_id: str
    dependent_responses: _containers.MessageMap[str, ServerInitiatedResponse]
    resume_data: _struct_pb2.Struct
    def __init__(self, metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., cursor: _Optional[str] = ..., progress: _Optional[_Union[ProgressNotification, _Mapping]] = ..., log_level: _Optional[_Union[LogLevel, str]] = ..., task_id: _Optional[str] = ..., dependent_responses: _Optional[_Mapping[str, ServerInitiatedResponse]] = ..., resume_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ResponseFields(_message.Message):
    __slots__ = ("instructions", "metadata", "next_cursor", "progress", "log_message", "task_id", "dependent_requests", "resume_data")
    class DependentRequestsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ServerInitiatedRequest
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ServerInitiatedRequest, _Mapping]] = ...) -> None: ...
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LOG_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    RESUME_DATA_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    metadata: _struct_pb2.Struct
    next_cursor: str
    progress: ProgressNotification
    log_message: LogMessage
    task_id: str
    dependent_requests: _containers.MessageMap[str, ServerInitiatedRequest]
    resume_data: _struct_pb2.Struct
    def __init__(self, instructions: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., next_cursor: _Optional[str] = ..., progress: _Optional[_Union[ProgressNotification, _Mapping]] = ..., log_message: _Optional[_Union[LogMessage, _Mapping]] = ..., task_id: _Optional[str] = ..., dependent_requests: _Optional[_Mapping[str, ServerInitiatedRequest]] = ..., resume_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Annotations(_message.Message):
    __slots__ = ("audience", "priority")
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    audience: _containers.RepeatedScalarFieldContainer[Role]
    priority: float
    def __init__(self, audience: _Optional[_Iterable[_Union[Role, str]]] = ..., priority: _Optional[float] = ...) -> None: ...

class TextContent(_message.Message):
    __slots__ = ("text", "annotations")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    annotations: Annotations
    def __init__(self, text: _Optional[str] = ..., annotations: _Optional[_Union[Annotations, _Mapping]] = ...) -> None: ...

class ImageContent(_message.Message):
    __slots__ = ("data", "mime_type", "annotations")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    mime_type: str
    annotations: Annotations
    def __init__(self, data: _Optional[bytes] = ..., mime_type: _Optional[str] = ..., annotations: _Optional[_Union[Annotations, _Mapping]] = ...) -> None: ...

class AudioContent(_message.Message):
    __slots__ = ("data", "mime_type", "annotations")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    mime_type: str
    annotations: Annotations
    def __init__(self, data: _Optional[bytes] = ..., mime_type: _Optional[str] = ..., annotations: _Optional[_Union[Annotations, _Mapping]] = ...) -> None: ...

class ListRootsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRootsResult(_message.Message):
    __slots__ = ("roots",)
    class Root(_message.Message):
        __slots__ = ("uri", "name")
        URI_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        uri: str
        name: str
        def __init__(self, uri: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    ROOTS_FIELD_NUMBER: _ClassVar[int]
    roots: _containers.RepeatedCompositeFieldContainer[ListRootsResult.Root]
    def __init__(self, roots: _Optional[_Iterable[_Union[ListRootsResult.Root, _Mapping]]] = ...) -> None: ...

class SamplingMessage(_message.Message):
    __slots__ = ("role", "text", "image", "audio")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    role: Role
    text: TextContent
    image: ImageContent
    audio: AudioContent
    def __init__(self, role: _Optional[_Union[Role, str]] = ..., text: _Optional[_Union[TextContent, _Mapping]] = ..., image: _Optional[_Union[ImageContent, _Mapping]] = ..., audio: _Optional[_Union[AudioContent, _Mapping]] = ...) -> None: ...

class SamplingCreateMessageRequest(_message.Message):
    __slots__ = ("messages", "model_preferences", "system_prompt", "include_context", "temperature", "max_tokens", "stop_sequence")
    class IncludeContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SamplingCreateMessageRequest.IncludeContext]
        THIS_SERVER: _ClassVar[SamplingCreateMessageRequest.IncludeContext]
        ALL_SERVERS: _ClassVar[SamplingCreateMessageRequest.IncludeContext]
    NONE: SamplingCreateMessageRequest.IncludeContext
    THIS_SERVER: SamplingCreateMessageRequest.IncludeContext
    ALL_SERVERS: SamplingCreateMessageRequest.IncludeContext
    class ModelPreferences(_message.Message):
        __slots__ = ("hints", "intelligence_priority", "speed_priority", "cost_priority")
        class ModelHint(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        HINTS_FIELD_NUMBER: _ClassVar[int]
        INTELLIGENCE_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        SPEED_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        COST_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        hints: _containers.RepeatedCompositeFieldContainer[SamplingCreateMessageRequest.ModelPreferences.ModelHint]
        intelligence_priority: float
        speed_priority: float
        cost_priority: float
        def __init__(self, hints: _Optional[_Iterable[_Union[SamplingCreateMessageRequest.ModelPreferences.ModelHint, _Mapping]]] = ..., intelligence_priority: _Optional[float] = ..., speed_priority: _Optional[float] = ..., cost_priority: _Optional[float] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MODEL_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    STOP_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[SamplingMessage]
    model_preferences: SamplingCreateMessageRequest.ModelPreferences
    system_prompt: str
    include_context: SamplingCreateMessageRequest.IncludeContext
    temperature: float
    max_tokens: int
    stop_sequence: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, messages: _Optional[_Iterable[_Union[SamplingMessage, _Mapping]]] = ..., model_preferences: _Optional[_Union[SamplingCreateMessageRequest.ModelPreferences, _Mapping]] = ..., system_prompt: _Optional[str] = ..., include_context: _Optional[_Union[SamplingCreateMessageRequest.IncludeContext, str]] = ..., temperature: _Optional[float] = ..., max_tokens: _Optional[int] = ..., stop_sequence: _Optional[_Iterable[str]] = ...) -> None: ...

class SamplingCreateMessageResult(_message.Message):
    __slots__ = ("message", "model", "stop_reason")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    message: SamplingMessage
    model: str
    stop_reason: str
    def __init__(self, message: _Optional[_Union[SamplingMessage, _Mapping]] = ..., model: _Optional[str] = ..., stop_reason: _Optional[str] = ...) -> None: ...

class PrimitiveSchemaDefinition(_message.Message):
    __slots__ = ("string_schema", "number_schema", "boolean_schema", "enum_schema")
    class StringSchema(_message.Message):
        __slots__ = ("title", "description", "min_length", "max_length", "format")
        class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FORMAT_UNKNOWN: _ClassVar[PrimitiveSchemaDefinition.StringSchema.Format]
            FORMAT_EMAIL: _ClassVar[PrimitiveSchemaDefinition.StringSchema.Format]
            FORMAT_URI: _ClassVar[PrimitiveSchemaDefinition.StringSchema.Format]
            FORMAT_DATE: _ClassVar[PrimitiveSchemaDefinition.StringSchema.Format]
            FORMAT_DATE_TIME: _ClassVar[PrimitiveSchemaDefinition.StringSchema.Format]
        FORMAT_UNKNOWN: PrimitiveSchemaDefinition.StringSchema.Format
        FORMAT_EMAIL: PrimitiveSchemaDefinition.StringSchema.Format
        FORMAT_URI: PrimitiveSchemaDefinition.StringSchema.Format
        FORMAT_DATE: PrimitiveSchemaDefinition.StringSchema.Format
        FORMAT_DATE_TIME: PrimitiveSchemaDefinition.StringSchema.Format
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
        MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        min_length: int
        max_length: int
        format: PrimitiveSchemaDefinition.StringSchema.Format
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., min_length: _Optional[int] = ..., max_length: _Optional[int] = ..., format: _Optional[_Union[PrimitiveSchemaDefinition.StringSchema.Format, str]] = ...) -> None: ...
    class NumberSchema(_message.Message):
        __slots__ = ("title", "description", "minimum", "maximum")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        minimum: int
        maximum: int
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., minimum: _Optional[int] = ..., maximum: _Optional[int] = ...) -> None: ...
    class BooleanSchema(_message.Message):
        __slots__ = ("title", "description", "default")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        default: bool
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., default: bool = ...) -> None: ...
    class EnumSchema(_message.Message):
        __slots__ = ("title", "description", "enum_list", "enum_names")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ENUM_LIST_FIELD_NUMBER: _ClassVar[int]
        ENUM_NAMES_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        enum_list: _containers.RepeatedScalarFieldContainer[str]
        enum_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., enum_list: _Optional[_Iterable[str]] = ..., enum_names: _Optional[_Iterable[str]] = ...) -> None: ...
    STRING_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NUMBER_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ENUM_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    string_schema: PrimitiveSchemaDefinition.StringSchema
    number_schema: PrimitiveSchemaDefinition.NumberSchema
    boolean_schema: PrimitiveSchemaDefinition.BooleanSchema
    enum_schema: PrimitiveSchemaDefinition.EnumSchema
    def __init__(self, string_schema: _Optional[_Union[PrimitiveSchemaDefinition.StringSchema, _Mapping]] = ..., number_schema: _Optional[_Union[PrimitiveSchemaDefinition.NumberSchema, _Mapping]] = ..., boolean_schema: _Optional[_Union[PrimitiveSchemaDefinition.BooleanSchema, _Mapping]] = ..., enum_schema: _Optional[_Union[PrimitiveSchemaDefinition.EnumSchema, _Mapping]] = ...) -> None: ...

class ElicitRequest(_message.Message):
    __slots__ = ("message", "requested_schema", "required_fields")
    class RequestedSchemaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PrimitiveSchemaDefinition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PrimitiveSchemaDefinition, _Mapping]] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    message: str
    requested_schema: _containers.MessageMap[str, PrimitiveSchemaDefinition]
    required_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message: _Optional[str] = ..., requested_schema: _Optional[_Mapping[str, PrimitiveSchemaDefinition]] = ..., required_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class ElicitResult(_message.Message):
    __slots__ = ("type", "content")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ElicitResult.Type]
        TYPE_ACCEPT: _ClassVar[ElicitResult.Type]
        TYPE_DECLINE: _ClassVar[ElicitResult.Type]
        TYPE_CANCEL: _ClassVar[ElicitResult.Type]
    UNKNOWN: ElicitResult.Type
    TYPE_ACCEPT: ElicitResult.Type
    TYPE_DECLINE: ElicitResult.Type
    TYPE_CANCEL: ElicitResult.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: ElicitResult.Type
    content: _struct_pb2.Struct
    def __init__(self, type: _Optional[_Union[ElicitResult.Type, str]] = ..., content: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ("uri", "name", "title", "description", "mime_type", "annotations", "size")
    URI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    name: str
    title: str
    description: str
    mime_type: str
    annotations: Annotations
    size: int
    def __init__(self, uri: _Optional[str] = ..., name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., mime_type: _Optional[str] = ..., annotations: _Optional[_Union[Annotations, _Mapping]] = ..., size: _Optional[int] = ...) -> None: ...

class ListResourcesRequest(_message.Message):
    __slots__ = ("common",)
    COMMON_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ...) -> None: ...

class ListResourcesResponse(_message.Message):
    __slots__ = ("common", "resources", "ttl")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    resources: _containers.RepeatedCompositeFieldContainer[Resource]
    ttl: _duration_pb2.Duration
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., resources: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ResourceContents(_message.Message):
    __slots__ = ("uri", "mime_type", "text", "blob")
    URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    uri: str
    mime_type: str
    text: str
    blob: bytes
    def __init__(self, uri: _Optional[str] = ..., mime_type: _Optional[str] = ..., text: _Optional[str] = ..., blob: _Optional[bytes] = ...) -> None: ...

class ReadResourceRequest(_message.Message):
    __slots__ = ("common", "uri")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    uri: str
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ..., uri: _Optional[str] = ...) -> None: ...

class ReadResourceResponse(_message.Message):
    __slots__ = ("common", "resource")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    resource: _containers.RepeatedCompositeFieldContainer[ResourceContents]
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., resource: _Optional[_Iterable[_Union[ResourceContents, _Mapping]]] = ...) -> None: ...

class ResourceTemplate(_message.Message):
    __slots__ = ("uri_template", "name", "title", "description", "mime_type", "annotations")
    URI_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    uri_template: str
    name: str
    title: str
    description: str
    mime_type: str
    annotations: Annotations
    def __init__(self, uri_template: _Optional[str] = ..., name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., mime_type: _Optional[str] = ..., annotations: _Optional[_Union[Annotations, _Mapping]] = ...) -> None: ...

class ListResourceTemplatesRequest(_message.Message):
    __slots__ = ("common",)
    COMMON_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ...) -> None: ...

class ListResourceTemplatesResponse(_message.Message):
    __slots__ = ("common", "resource_templates", "ttl")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    resource_templates: _containers.RepeatedCompositeFieldContainer[ResourceTemplate]
    ttl: _duration_pb2.Duration
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., resource_templates: _Optional[_Iterable[_Union[ResourceTemplate, _Mapping]]] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class Prompt(_message.Message):
    __slots__ = ("name", "title", "description", "arguments")
    class Argument(_message.Message):
        __slots__ = ("name", "title", "description", "required")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        name: str
        title: str
        description: str
        required: bool
        def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    arguments: _containers.RepeatedCompositeFieldContainer[Prompt.Argument]
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., arguments: _Optional[_Iterable[_Union[Prompt.Argument, _Mapping]]] = ...) -> None: ...

class ListPromptsRequest(_message.Message):
    __slots__ = ("common",)
    COMMON_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ...) -> None: ...

class ListPromptsResponse(_message.Message):
    __slots__ = ("common", "prompts", "ttl")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    PROMPTS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    prompts: _containers.RepeatedCompositeFieldContainer[Prompt]
    ttl: _duration_pb2.Duration
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., prompts: _Optional[_Iterable[_Union[Prompt, _Mapping]]] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class EmbeddedResource(_message.Message):
    __slots__ = ("contents", "annotations")
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    contents: ResourceContents
    annotations: Annotations
    def __init__(self, contents: _Optional[_Union[ResourceContents, _Mapping]] = ..., annotations: _Optional[_Union[Annotations, _Mapping]] = ...) -> None: ...

class PromptMessage(_message.Message):
    __slots__ = ("role", "text", "image", "audio", "embedded_resource", "resource_link")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    role: Role
    text: TextContent
    image: ImageContent
    audio: AudioContent
    embedded_resource: EmbeddedResource
    resource_link: Resource
    def __init__(self, role: _Optional[_Union[Role, str]] = ..., text: _Optional[_Union[TextContent, _Mapping]] = ..., image: _Optional[_Union[ImageContent, _Mapping]] = ..., audio: _Optional[_Union[AudioContent, _Mapping]] = ..., embedded_resource: _Optional[_Union[EmbeddedResource, _Mapping]] = ..., resource_link: _Optional[_Union[Resource, _Mapping]] = ...) -> None: ...

class GetPromptRequest(_message.Message):
    __slots__ = ("common", "name", "arguments")
    class ArgumentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMON_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    name: str
    arguments: _containers.ScalarMap[str, str]
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ..., name: _Optional[str] = ..., arguments: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetPromptResponse(_message.Message):
    __slots__ = ("common", "description", "messages")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    description: str
    messages: _containers.RepeatedCompositeFieldContainer[PromptMessage]
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., description: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[PromptMessage, _Mapping]]] = ...) -> None: ...

class ToolAnnotations(_message.Message):
    __slots__ = ("title", "read_only_hint", "destructive_hint", "idempotent_hint", "open_world_hint")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_HINT_FIELD_NUMBER: _ClassVar[int]
    DESTRUCTIVE_HINT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_HINT_FIELD_NUMBER: _ClassVar[int]
    OPEN_WORLD_HINT_FIELD_NUMBER: _ClassVar[int]
    title: str
    read_only_hint: bool
    destructive_hint: bool
    idempotent_hint: bool
    open_world_hint: bool
    def __init__(self, title: _Optional[str] = ..., read_only_hint: bool = ..., destructive_hint: bool = ..., idempotent_hint: bool = ..., open_world_hint: bool = ...) -> None: ...

class Tool(_message.Message):
    __slots__ = ("name", "title", "description", "input_schema", "output_schema", "annotations")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    input_schema: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    annotations: ToolAnnotations
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., annotations: _Optional[_Union[ToolAnnotations, _Mapping]] = ...) -> None: ...

class ListToolsRequest(_message.Message):
    __slots__ = ("common",)
    COMMON_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ...) -> None: ...

class ListToolsResponse(_message.Message):
    __slots__ = ("common", "tools", "ttl")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    ttl: _duration_pb2.Duration
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., tools: _Optional[_Iterable[_Union[Tool, _Mapping]]] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CallToolRequest(_message.Message):
    __slots__ = ("common", "request")
    class Request(_message.Message):
        __slots__ = ("name", "arguments")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        name: str
        arguments: _struct_pb2.Struct
        def __init__(self, name: _Optional[str] = ..., arguments: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    COMMON_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    request: CallToolRequest.Request
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ..., request: _Optional[_Union[CallToolRequest.Request, _Mapping]] = ...) -> None: ...

class CallToolResponse(_message.Message):
    __slots__ = ("common", "content", "structured_content", "is_error")
    class Content(_message.Message):
        __slots__ = ("text", "image", "audio", "embedded_resource", "resource_link")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        EMBEDDED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
        text: TextContent
        image: ImageContent
        audio: AudioContent
        embedded_resource: EmbeddedResource
        resource_link: Resource
        def __init__(self, text: _Optional[_Union[TextContent, _Mapping]] = ..., image: _Optional[_Union[ImageContent, _Mapping]] = ..., audio: _Optional[_Union[AudioContent, _Mapping]] = ..., embedded_resource: _Optional[_Union[EmbeddedResource, _Mapping]] = ..., resource_link: _Optional[_Union[Resource, _Mapping]] = ...) -> None: ...
    COMMON_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    content: _containers.RepeatedCompositeFieldContainer[CallToolResponse.Content]
    structured_content: _struct_pb2.Struct
    is_error: bool
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., content: _Optional[_Iterable[_Union[CallToolResponse.Content, _Mapping]]] = ..., structured_content: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., is_error: bool = ...) -> None: ...

class ResourceReference(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class PromptReference(_message.Message):
    __slots__ = ("name", "title")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class CompletionRequest(_message.Message):
    __slots__ = ("common", "resource_reference", "prompt_reference", "argument", "context")
    class Argument(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Context(_message.Message):
        __slots__ = ("arguments",)
        class ArgumentsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        arguments: _containers.ScalarMap[str, str]
        def __init__(self, arguments: _Optional[_Mapping[str, str]] = ...) -> None: ...
    COMMON_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    resource_reference: ResourceReference
    prompt_reference: PromptReference
    argument: CompletionRequest.Argument
    context: CompletionRequest.Context
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ..., resource_reference: _Optional[_Union[ResourceReference, _Mapping]] = ..., prompt_reference: _Optional[_Union[PromptReference, _Mapping]] = ..., argument: _Optional[_Union[CompletionRequest.Argument, _Mapping]] = ..., context: _Optional[_Union[CompletionRequest.Context, _Mapping]] = ...) -> None: ...

class CompletionResponse(_message.Message):
    __slots__ = ("common", "values", "total_matches", "has_more")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHES_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    values: _containers.RepeatedScalarFieldContainer[str]
    total_matches: int
    has_more: bool
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ..., values: _Optional[_Iterable[str]] = ..., total_matches: _Optional[int] = ..., has_more: bool = ...) -> None: ...

class CancelTaskRequest(_message.Message):
    __slots__ = ("common",)
    COMMON_FIELD_NUMBER: _ClassVar[int]
    common: RequestFields
    def __init__(self, common: _Optional[_Union[RequestFields, _Mapping]] = ...) -> None: ...

class CancelTaskResponse(_message.Message):
    __slots__ = ("common",)
    COMMON_FIELD_NUMBER: _ClassVar[int]
    common: ResponseFields
    def __init__(self, common: _Optional[_Union[ResponseFields, _Mapping]] = ...) -> None: ...
