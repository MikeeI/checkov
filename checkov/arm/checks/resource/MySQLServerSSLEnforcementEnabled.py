from typing import Any

from checkov.arm.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories


class MySQLServerSSLEnforcementEnabled(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure 'Enforce SSL connection' is set to 'ENABLED' for MySQL Database Server"
        id = "CKV_AZURE_28"
        supported_resources = ["Microsoft.DBforMySQL/servers"]
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "properties/sslEnforcement"

    def get_expected_value(self) -> Any:
        return "Enabled"


check = MySQLServerSSLEnforcementEnabled()
