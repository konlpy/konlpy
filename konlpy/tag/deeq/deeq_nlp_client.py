import sys

import grpc
from google.protobuf.json_format import MessageToDict

import deeq.language_service_pb2 as pb
import deeq.language_service_pb2_grpc as ls


class BaikalLanguageServiceClient:
    stub = None

    def __init__(self, remote):
        channel = grpc.insecure_channel(remote)
        self.stub = ls.LanguageServiceStub(channel)

    def analyze_syntax(self, document, auto_split=False):
        req = pb.AnalyzeSyntaxRequest()
        req.document.content = document
        req.document.language = "ko_KR"
        req.encoding_type = pb.EncodingType.UTF32
        req.auto_split_sentence = auto_split

        res = self.stub.AnalyzeSyntax(req)
        return res
