import warnings

from .base import ElementBase


class State(ElementBase):
  def __init__(self, *, sdf_version: str) -> None:
    warnings.warn("`State` has not been implemented yet.")
    super().__init__(sdf_version=sdf_version)


"""<!-- State Info -->
<element name="state" required="*">
  <!-- Name of the world this state applies to -->
  <attribute name="world_name" type="string" default="__default__" required="1">
    <description>Name of the world this state applies to</description>
  </attribute>

  <element name="sim_time" type="time" default="0 0" required="0">
    <description>Simulation time stamp of the state [seconds nanoseconds]</description>
  </element>

  <element name="wall_time" type="time" default="0 0" required="0">
    <description>Wall time stamp of the state [seconds nanoseconds]</description>
  </element>

  <element name="real_time" type="time" default="0 0" required="0">
    <description>Real time stamp of the state [seconds nanoseconds]</description>
  </element>

  <element name="iterations" type="unsigned int" default="0" required="1">
    <description>Number of simulation iterations.</description>
  </element>

  <element name="insertions" required="0">
    <description>A list containing the entire description of entities inserted.</description>
    <include filename="model.sdf" required="+"/>
    <include filename="light.sdf" required="+"/>
  </element>

  <element name="deletions" required="0">
    <description>A list of names of deleted entities/</description>
    <element name="name" type="string" default="__default__" required="+">
      <description>The name of a deleted entity.</description>
    </element>
  </element>

  <include filename="model_state.sdf" required="*"/>

  <include filename="light_state.sdf" required="*"/>

</element> <!-- End State -->
"""