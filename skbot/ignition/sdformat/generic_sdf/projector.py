import warnings

from .base import ElementBase


class Projector(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Projector` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<!-- Projector -->
<element name="projector" required="0">
  <attribute name="name" type="string" default="__default__" required="1">
    <description>Name of the projector</description>
  </attribute>

  <element name="texture" type="string" default="__default__" required="1">
    <description>Texture name</description>
  </element>

  <element name="fov" type="double" default="0.785" required="0">
    <description>Field of view</description>
  </element>


  <element name="near_clip" type="double" default="0.1" required="0">
    <description>Near clip distance</description>
  </element>


  <element name="far_clip" type="double" default="10.0" required="0">
    <description>far clip distance</description>
  </element>

  <include filename="pose.sdf" required="0"/>

  <include filename="plugin.sdf" required="*"/>
</element>
"""