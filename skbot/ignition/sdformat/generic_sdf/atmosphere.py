import warnings

from .base import ElementBase


class Atmosphere(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Atmosphere` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<!-- Atmosphere -->
<element name="atmosphere" required="1">
  <description>The atmosphere tag specifies the type and properties of the atmosphere model.</description>

  <attribute name="type" type="string" default="adiabatic" required="1">
    <description>The type of the atmosphere engine. Current options are adiabatic.  Defaults to adiabatic if left unspecified.</description>
  </attribute>

  <element name="temperature" type="double" default="288.15" required="0">
    <description>Temperature at sea level in kelvins.</description>
  </element>

  <element name="pressure" type="double" default="101325" required="0">
    <description>Pressure at sea level in pascals.</description>
  </element>

  <element name="temperature_gradient" type="double" default="-0.0065" required="0">
    <description>Temperature gradient with respect to increasing altitude at sea level in units of K/m.</description>
  </element>

</element> <!-- Atmosphere -->
"""
