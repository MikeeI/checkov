from typing import List, Any

from checkov.common.models.consts import ANY_VALUE
from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class AKSApiServerAuthorizedIpRanges(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure AKS has an API Server Authorized IP Ranges enabled"
        id = "CKV_AZURE_6"
        supported_resources = ("azurerm_kubernetes_cluster",)
        categories = (CheckCategories.KUBERNETES,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "api_server_authorized_ip_ranges/[0]"

    def get_expected_values(self) -> List[Any]:
        return [ANY_VALUE]


check = AKSApiServerAuthorizedIpRanges()
