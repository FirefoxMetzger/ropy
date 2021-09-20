import warnings

from .base import ElementBase


class Mesh(ElementBase):
  def __init__(self, *, sdf_version: str) -> None:
    warnings.warn("`Mesh` has not been implemented yet.")
    super().__init__(sdf_version=sdf_version)

"""<element name="mesh" required="0">
  <description>Mesh shape</description>
  <element name="uri" type="string" default="__default__" required="1">
    <description>Mesh uri</description>
  </element>

  <element name="submesh" required="0">
    <description>Use a named submesh. The submesh must exist in the mesh specified by the uri</description>
    <element name="name" type="string" default="__default__" required="1">
      <description>Name of the submesh within the parent mesh</description>
    </element>
    <element name="center" type="bool" default="false" required="0">
      <description>Set to true to center the vertices of the submesh at 0,0,0. This will effectively remove any transformations on the submesh before the poses from parent links and models are applied.</description>
    </element>
  </element> <!-- End submesh -->

  <element name="scale" type="vector3" default="1 1 1" required="0">
    <description>Scaling factor applied to the mesh</description>
  </element>
</element>
"""