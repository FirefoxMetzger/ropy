import warnings

from .base import ElementBase


class Navsat(ElementBase):
  def __init__(self, *, sdf_version: str) -> None:
    warnings.warn("`Navsat` has not been implemented yet.")
    super().__init__(sdf_version=sdf_version)

"""<element name="navsat" required="0">
  <description>These elements are specific to the NAVSAT sensor.</description>

  <element name="position_sensing" required="0">
    <description>
      Parameters related to NAVSAT position measurement.
    </description>
    <element name="horizontal" required="0">
      <description>
        Noise parameters for horizontal position measurement, in units of meters.
      </description>
      <include filename="noise.sdf" required="0"/>
    </element>
    <element name="vertical" required="0">
      <description>
        Noise parameters for vertical position measurement, in units of meters.
      </description>
      <include filename="noise.sdf" required="0"/>
    </element>
  </element>

  <element name="velocity_sensing" required="0">
    <description>
      Parameters related to NAVSAT position measurement.
    </description>
    <element name="horizontal" required="0">
      <description>
        Noise parameters for horizontal velocity measurement, in units of meters/second.
      </description>
      <include filename="noise.sdf" required="0"/>
    </element>
    <element name="vertical" required="0">
      <description>
        Noise parameters for vertical velocity measurement, in units of meters/second.
      </description>
      <include filename="noise.sdf" required="0"/>
    </element>
  </element>

</element>
"""