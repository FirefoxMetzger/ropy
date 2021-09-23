import warnings

from .base import ElementBase


class Link(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Link` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<!-- State information for a link -->
<element name="link" required="*">
  <description>Link state</description>

  <attribute name="name" type="string" default="__default__" required="1">
    <description>Name of the link</description>
  </attribute>

  <element name="velocity" type="pose" default="0 0 0 0 0 0" required="0">
    <description>Velocity of the link. The x, y, z components of the pose
      correspond to the linear velocity of the link, and the roll, pitch, yaw
      components correspond to the angular velocity of the link
    </description>
  </element>

  <element name="acceleration" type="pose" default="0 0 0 0 0 0" required="0">
    <description>Acceleration of the link. The x, y, z components of the pose
      correspond to the linear acceleration of the link, and the roll,
      pitch, yaw components correspond to the angular acceleration of the link
    </description>
  </element>

  <element name="wrench" type="pose" default="0 0 0 0 0 0" required="0">
    <description>Force and torque applied to the link. The x, y, z components
      of the pose correspond to the force applied to the link, and the roll,
      pitch, yaw components correspond to the torque applied to the link
    </description>
  </element>

  <element name="collision" required="*">
    <description>Collision state</description>

    <attribute name="name" type="string" default="__default__" required="1">
      <description>Name of the collision</description>
    </attribute>
  </element>

  <include filename="pose.sdf" required="0"/>

</element> <!-- End Link -->
"""
