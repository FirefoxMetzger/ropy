import warnings

from .base import ElementBase


class AirPressure(ElementBase):
  def __init__(self, *, sdf_version: str) -> None:
    warnings.warn("`AirPressure` has not been implemented yet.")
    super().__init__(sdf_version=sdf_version)


"""<element name="air_pressure" required="0">
  <description>These elements are specific to an air pressure sensor.</description>

  <element name="reference_altitude" type="double" default="0.0" required="0">
    <description>The initial altitude in meters. This value can be used by a sensor implementation to augment the altitude of the sensor. For example, if you are using simulation instead of creating a 1000 m mountain model on which to place your sensor, you could instead set this value to 1000 and place your model on a ground plane with a Z height of zero.</description>
  </element>

  <element name="pressure" required="0">
    <description>
      Noise parameters for the pressure data.
    </description>
    <include filename="noise.sdf" required="0"/>
  </element>

</element>
"""