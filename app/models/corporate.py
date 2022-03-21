from torpedo.db import CustomTextField, ModelUtilMixin, TextArrayField
from tortoise import Model, fields
from ..constants import CorporateType


class CorporateService(Model, ModelUtilMixin):

    id = fields.UUIDField(index=True, pk=True)
    name = CustomTextField(null=True)
    type = fields.CharEnumField(CorporateType, null=True)
    coupon_code = CustomTextField(null=True)
    logo_url = CustomTextField(null=True)
    dashboard_url = CustomTextField(null=True)
    is_plan_active = fields.BooleanField(null=True)
    is_active = fields.BooleanField(null=True)
    created_at = fields.DatetimeField(null=True)
    updated_at = fields.DatetimeField(null=True)
    domains = TextArrayField(null=True)
    address = CustomTextField(null=True)
    spoc_details = fields.JSONField()

    class Meta:
        table = "corporate_service"
