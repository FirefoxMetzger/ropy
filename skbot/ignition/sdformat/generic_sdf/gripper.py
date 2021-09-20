import warnings

from .base import ElementBase


class Gripper(ElementBase):
  def __init__(self, *, sdf_version: str) -> None:
    warnings.warn("`Gripper` has not been implemented yet.")
    super().__init__(sdf_version=sdf_version)


"""<!-- Gripper -->
<element name="gripper" required="*">
  <description></description>

  <attribute name="name" type="string" default="__default__" required="1">
    <description></description>
  </attribute>

  <element name="grasp_check" required="0">
    <description></description>
    <element name="detach_steps" type="int" default="40" required="0">
      <description></description>
    </element>
    <element name="attach_steps" type="int" default="20" required="0">
      <description></description>
    </element>
    <element name="min_contact_count" type="unsigned int" default="2" required="0">
      <description></description>
    </element>
  </element>

  <element name="gripper_link" type="string" default="__default__" required="+">
    <description></description>
  </element>

  <element name="palm_link" type="string" default="__default__" required="1">
    <description></description>
  </element>

</element>
"""