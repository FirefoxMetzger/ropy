import warnings

from .base import ElementBase


class Collision(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Collision` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<!-- Collision -->
<element name="collision" required="*">
  <description>The collision properties of a link. Note that this can be different from the visual properties of a link, for example, simpler collision models are often used to reduce computation time.</description>

  <attribute name="name" type="string" default="__default__" required="1">
    <description>Unique name for the collision element within the scope of the parent link.</description>
  </attribute>

  <element name="laser_retro" type="double" default="0" required="0">
    <description>intensity value returned by laser sensor.</description>
  </element>

  <element name="max_contacts" type="int" default="10" required="0">
    <description>Maximum number of contacts allowed between two entities. This value overrides the max_contacts element defined in physics.</description>
  </element>

  <include filename="pose.sdf" required="0"/>

  <include filename="geometry.sdf" required="1"/>
  <include filename="surface.sdf" required="0"/>

</element> <!-- End Collision -->
"""
