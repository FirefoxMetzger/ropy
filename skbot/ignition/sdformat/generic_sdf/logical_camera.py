import warnings

from .base import ElementBase


class LogicalCamera(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`LogicalCamera` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<element name="logical_camera" required="0">
  <description>These elements are specific to logical camera sensors. A logical camera reports objects that fall within a frustum. Computation should be performed on the CPU.</description>

  <element name="near" type="double" default="0" required="1">
    <description>Near clipping distance of the view frustum</description>
  </element>

  <element name="far" type="double" default="1" required="1">
    <description>Far clipping distance of the view frustum</description>
  </element>

  <element name="aspect_ratio" type="double" default="1" required="1">
    <description>Aspect ratio of the near and far planes. This is the width divided by the height of the near or far planes.</description>
  </element>

  <element name="horizontal_fov" type="double" default="1" required="1">
    <description>Horizontal field of view of the frustum, in radians. This is the angle between the frustum's vertex and the edges of the near or far plane.</description>
  </element>
</element>
"""
