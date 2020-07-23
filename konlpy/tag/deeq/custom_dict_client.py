import grpc
from typing import List

from google.protobuf.empty_pb2 import Empty
import deeq.custom_dict_pb2 as pb
import deeq.dict_common_pb2 as common
import deeq.custom_dict_pb2_grpc as cds


def build_dict_set(domain, name, dict_set: set) -> common.DictSet:
    ret = common.DictSet()
    ret.name = domain + "-" + name
    ret.type = common.DictType.WORD_LIST
    for v in dict_set:
        ret.items[v] = 1
    return ret


class CustomDictionaryServiceClient:
    """
    커스텀 사전을 생성, 조회, 업데이트, 삭제하는 클라이언트
    """
    stub = None

    def __init__(self, remote):
        super().__init__()
        channel = grpc.insecure_channel(remote)
        self.stub = cds.CustomDictionaryServiceStub(channel)

    def get_list(self) -> List[pb.CustomDictionaryMeta]:
        req = Empty()
        res = self.stub.GetCustomDictionaryList(req)
        return res.domain_dicts

    def update(self, domain: str, np: set, cp: set, cp_caret: set) -> bool:
        req = pb.UpdateCustomDictionaryRequest()
        req.domain_name = domain

        req.dict.domain_name = domain

        req.dict.np_set.CopyFrom(build_dict_set(domain, 'np-set', np))
        req.dict.cp_set.CopyFrom(build_dict_set(domain, 'cp-set', cp))
        req.dict.cp_caret_set.CopyFrom(build_dict_set(domain, 'cp-caret-set', cp_caret))

        res = self.stub.UpdateCustomDictionary(req)
        return res.updated_domain_name == domain

    def remove_all(self) -> List[str]:
        """
        모든 커스텀 사전을 삭제한 이후에 반환한다.
        :return: 삭제된 도메인의 이름들
        """
        req = pb.RemoveCustomDictionariesRequest()
        req.all = True

        res = self.stub.RemoveCustomDictionaries(req)
        return res.deleted_domain_names.keys()

    def remove(self, domains: List[str]) -> List[str]:
        """
        지정한 도메인의 커스텀 사전을 삭제한다.
        :param domains: 삭제할 커스텀 사전의 도메인의 배열들
        :return: 정상 삭제 여부
        """
        req = pb.RemoveCustomDictionariesRequest()
        req.domain_names.extend(domains)
        req.all = False

        res = self.stub.RemoveCustomDictionaries(req)
        return res.deleted_domain_names.keys()
