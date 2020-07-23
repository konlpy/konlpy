# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import deeq.custom_dict_pb2 as baikal_dot_language_dot_custom__dict__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CustomDictionaryServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCustomDictionaryList = channel.unary_unary(
                '/baikal.language.CustomDictionaryService/GetCustomDictionaryList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryListResponse.FromString,
                )
        self.GetCustomDictionary = channel.unary_unary(
                '/baikal.language.CustomDictionaryService/GetCustomDictionary',
                request_serializer=baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryRequest.SerializeToString,
                response_deserializer=baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryResponse.FromString,
                )
        self.UpdateCustomDictionary = channel.unary_unary(
                '/baikal.language.CustomDictionaryService/UpdateCustomDictionary',
                request_serializer=baikal_dot_language_dot_custom__dict__pb2.UpdateCustomDictionaryRequest.SerializeToString,
                response_deserializer=baikal_dot_language_dot_custom__dict__pb2.UpdateCustomDictionaryResponse.FromString,
                )
        self.RemoveCustomDictionaries = channel.unary_unary(
                '/baikal.language.CustomDictionaryService/RemoveCustomDictionaries',
                request_serializer=baikal_dot_language_dot_custom__dict__pb2.RemoveCustomDictionariesRequest.SerializeToString,
                response_deserializer=baikal_dot_language_dot_custom__dict__pb2.RemoveCustomDictionariesResponse.FromString,
                )


class CustomDictionaryServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetCustomDictionaryList(self, request, context):
        """전체 목록을 다 가져오기
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomDictionary(self, request, context):
        """현재 저장되어 있는 사전 하나만 가져온다.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCustomDictionary(self, request, context):
        """전체를 모두 다 바꿔치기하는 경우
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveCustomDictionaries(self, request, context):
        """여러 개를 한꺼번에 지운다.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomDictionaryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCustomDictionaryList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCustomDictionaryList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryListResponse.SerializeToString,
            ),
            'GetCustomDictionary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCustomDictionary,
                    request_deserializer=baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryRequest.FromString,
                    response_serializer=baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryResponse.SerializeToString,
            ),
            'UpdateCustomDictionary': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCustomDictionary,
                    request_deserializer=baikal_dot_language_dot_custom__dict__pb2.UpdateCustomDictionaryRequest.FromString,
                    response_serializer=baikal_dot_language_dot_custom__dict__pb2.UpdateCustomDictionaryResponse.SerializeToString,
            ),
            'RemoveCustomDictionaries': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveCustomDictionaries,
                    request_deserializer=baikal_dot_language_dot_custom__dict__pb2.RemoveCustomDictionariesRequest.FromString,
                    response_serializer=baikal_dot_language_dot_custom__dict__pb2.RemoveCustomDictionariesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'baikal.language.CustomDictionaryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomDictionaryService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetCustomDictionaryList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/baikal.language.CustomDictionaryService/GetCustomDictionaryList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryListResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCustomDictionary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/baikal.language.CustomDictionaryService/GetCustomDictionary',
            baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryRequest.SerializeToString,
            baikal_dot_language_dot_custom__dict__pb2.GetCustomDictionaryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCustomDictionary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/baikal.language.CustomDictionaryService/UpdateCustomDictionary',
            baikal_dot_language_dot_custom__dict__pb2.UpdateCustomDictionaryRequest.SerializeToString,
            baikal_dot_language_dot_custom__dict__pb2.UpdateCustomDictionaryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveCustomDictionaries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/baikal.language.CustomDictionaryService/RemoveCustomDictionaries',
            baikal_dot_language_dot_custom__dict__pb2.RemoveCustomDictionariesRequest.SerializeToString,
            baikal_dot_language_dot_custom__dict__pb2.RemoveCustomDictionariesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
