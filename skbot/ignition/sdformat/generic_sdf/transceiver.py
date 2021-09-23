import warnings

from .base import ElementBase


class Transceiver(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Transceiver` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<element name="transceiver" required="0">
  <description>These elements are specific to a wireless transceiver.</description>

  <element name="essid" type="string" default="wireless" required="0">
    <description>Service set identifier (network name)</description>
  </element> <!-- End Essid -->

  <element name="frequency" type="double" default="2442" required="0">
    <description>Specifies the frequency of transmission in MHz</description>
  </element> <!-- End Frequency -->

  <element name="min_frequency" type="double" default="2412" required="0">
    <description>Only a frequency range is filtered. Here we set the lower bound (MHz).
    </description>
  </element> <!-- End min_frequency -->

  <element name="max_frequency" type="double" default="2484" required="0">
    <description>Only a frequency range is filtered. Here we set the upper bound (MHz).
    </description>
  </element> <!-- End max_frequency -->

  <element name="gain" type="double" default="2.5" required="1">
    <description>Specifies the antenna gain in dBi</description>
  </element> <!-- End Gain -->

  <element name="power" type="double" default="14.50" required="1">
    <description>Specifies the transmission power in dBm</description>
  </element> <!-- End Power -->

  <element name="sensitivity" type="double" default="-90" required="0">
    <description>Mininum received signal power in dBm</description>
  </element> <!-- End Sensitivity -->

</element> <!-- End Transceiver -->
"""
