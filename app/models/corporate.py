from torpedo.db import CustomTextField, ModelUtilMixin, TextArrayField
from tortoise import Model, fields

class CorporateService(Model, ModelUtilMixin):

    id = fields.UUIDField(index=True, pk=True)
    name = CustomTextField(null=False)
    type = CustomTextField(null=False)
    address = CustomTextField(null=False)
    phone = CustomTextField(null=False)
    spoc_email = CustomTextField(null=False)
    spoc_phone = CustomTextField(null=False)
    coupon_code = CustomTextField(null=False)
    domains = TextArrayField()
    logo_url = CustomTextField(null=True)
    dashboard_url = CustomTextField(null=True)
    html = CustomTextField(null=True)
    is_plan_active = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    created_at = fields.DateField()
    updated_at = fields.DateField()

    class Meta:
        table = "corporates"



