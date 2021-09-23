import warnings

from .base import ElementBase


class Visual(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Visual` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<!-- Visual -->
<element name="visual" required="*">
  <description>The visual properties of the link. This element specifies the shape of the object (box, cylinder, etc.) for visualization purposes.</description>

  <attribute name="name" type="string" default="__default__" required="1">
    <description>Unique name for the visual element within the scope of the parent link.</description>
  </attribute>

  <element name="cast_shadows" type="bool" default="true" required="0">
    <description>If true the visual will cast shadows.</description>
  </element>

  <element name="laser_retro" type="double" default="0.0" required="0">
    <description>will be implemented in the future release.</description>
  </element>

  <element name="transparency" type="double" default="0.0" required="0">
    <description>The amount of transparency( 0=opaque, 1 = fully transparent)</description>
  </element>

  <element name="visibility_flags" type="unsigned int" default="4294967295" required="0">
    <description><![CDATA[Visibility flags of a visual. When (camera's visibility_mask & visual's visibility_flags) evaluates to non-zero, the visual will be visible to the camera.]]></description>
  </element>

  <element name="meta" required="0">
    <description>Optional meta information for the visual. The information contained within this element should be used to provide additional feedback to an end user.</description>

    <element name="layer" type="int" default="0" required="0">
      <description>The layer in which this visual is displayed. The layer number is useful for programs, such as Gazebo, that put visuals in different layers for enhanced visualization.</description>
    </element>
  </element>

  <include filename="pose.sdf" required="0"/>

  <include filename="material.sdf" required="0"/>
  <include filename="geometry.sdf" required="1"/>
  <include filename="plugin.sdf" required="*"/>
</element> <!-- End Visual -->
"""
