import warnings

from .base import ElementBase


class Model(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Model` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<!-- State information for a model -->
<element name="model" required="*">
  <description>Model state</description>

  <attribute name="name" type="string" default="__default__" required="1">
    <description>Name of the model</description>
  </attribute>

  <element name="joint" required="*">
    <description>Joint angle</description>

    <attribute name="name" type="string" default="__default__" required="1">
      <description>Name of the joint</description>
    </attribute>

    <element name="angle" type="double" default="0" required="+">
      <attribute name="axis" type="unsigned int" default="0" required="1">
        <description>Index of the axis.</description>
      </attribute>

      <description>Angle of an axis</description>
    </element>
  </element>

  <element name="model" ref="model_state" required="*">
    <description>A nested model state element</description>
    <attribute name="name" type="string" default="__default__" required="1">
      <description>Name of the model. </description>
    </attribute>
  </element>

  <include filename="frame.sdf" required="*"/>
  <include filename="pose.sdf" required="0"/>

  <element name="scale" type="vector3" default="1 1 1" required="0">
    <description>Scale for the 3 dimensions of the model.</description>
  </element>

  <include filename="link_state.sdf" required="*"/>

</element> <!-- End Model -->
"""