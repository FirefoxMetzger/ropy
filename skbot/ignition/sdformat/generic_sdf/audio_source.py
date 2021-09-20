import warnings

from .base import ElementBase


class AudioSource(ElementBase):
  def __init__(self, *, sdf_version: str) -> None:
    warnings.warn("`AudioSource` has not been implemented yet.")
    super().__init__(sdf_version=sdf_version)


"""<!-- Audio Source -->
<element name="audio_source" required="*">
  <description>An audio source.</description>

  <element name="uri" type="string" default="__default__" required="1">
    <description>URI of the audio media.</description>
  </element>

  <element name="pitch" type="double" default="1.0" required="0">
    <description>Pitch for the audio media, in Hz</description>
  </element>

  <element name="gain" type="double" default="1.0" required="0">
    <description>Gain for the audio media, in dB.</description>
  </element>

  <element name="contact" required="0">
    <description>List of collision objects that will trigger audio playback.</description>
    <element name="collision" type="string" default="__default__" required="+">
      <description>Name of child collision element that will trigger audio playback.</description>
    </element>
  </element>

  <element name="loop" type="bool" default="false" required="0">
    <description>True to make the audio source loop playback.</description>
  </element>

  <include filename="pose.sdf" required="0"/>

</element>
"""