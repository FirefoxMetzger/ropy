import warnings

from .base import ElementBase


class Imu(ElementBase):
  def __init__(self, *, sdf_version: str) -> None:
    warnings.warn("`Imu` has not been implemented yet.")
    super().__init__(sdf_version=sdf_version)

"""<element name="imu" required="0">
  <description>These elements are specific to the IMU sensor.</description>

  <element name="orientation_reference_frame" required="0">
    <!-- move this under custom_rpy? -->
    <element name="localization" type="string" default="CUSTOM" required="1">
      <description>
        This string represents special hardcoded use cases that are commonly seen with typical robot IMU's:
          - CUSTOM: use Euler angle custom_rpy orientation specification.
                 The orientation of the IMU's reference frame is defined by adding the custom_rpy rotation
                 to the parent_frame.
          - NED: The IMU XYZ aligns with NED, where NED orientation relative to Gazebo world
                 is defined by the SphericalCoordinates class.
          - ENU: The IMU XYZ aligns with ENU, where ENU orientation relative to Gazebo world
                 is defined by the SphericalCoordinates class.
          - NWU: The IMU XYZ aligns with NWU, where NWU orientation relative to Gazebo world
                 is defined by the SphericalCoordinates class.
          - GRAV_UP: where direction of gravity maps to IMU reference frame Z-axis with Z-axis pointing in
                     the opposite direction of gravity. IMU reference frame X-axis direction is defined by grav_dir_x.
                     Note if grav_dir_x is parallel to gravity direction, this configuration fails.
                     Otherwise, IMU reference frame X-axis is defined by projection of grav_dir_x onto a plane
                     normal to the gravity vector. IMU reference frame Y-axis is a vector orthogonal to both
                     X and Z axis following the right hand rule.
          - GRAV_DOWN: where direction of gravity maps to IMU reference frame Z-axis with Z-axis pointing in
                       the direction of gravity. IMU reference frame X-axis direction is defined by grav_dir_x.
                       Note if grav_dir_x is parallel to gravity direction, this configuration fails.
                       Otherwise, IMU reference frame X-axis is defined by projection of grav_dir_x onto a plane
                       normal to the gravity vector. IMU reference frame Y-axis is a vector orthogonal to both
                       X and Z axis following the right hand rule.
      </description>
    </element>
    <element name="custom_rpy" type="vector3" default="0 0 0" required="0">
      <description>
        This field and parent_frame are used when localization is set to CUSTOM.
        Orientation (fixed axis roll, pitch yaw) transform from parent_frame to this IMU's reference frame.
        Some common examples are:
          - IMU reports in its local frame on boot. IMU sensor frame is the reference frame.
             Example: parent_frame="", custom_rpy="0 0 0"
          - IMU reports in Gazebo world frame.
             Example sdf: parent_frame="world", custom_rpy="0 0 0"
          - IMU reports in NWU frame.
             Uses SphericalCoordinates class to determine world frame in relation to magnetic north and gravity;
             i.e. rotation between North-West-Up and world (+X,+Y,+Z) frame is defined by SphericalCoordinates class.
             Example sdf given world is NWU: parent_frame="world", custom_rpy="0 0 0"
          - IMU reports in NED frame.
             Uses SphericalCoordinates class to determine world frame in relation to magnetic north and gravity;
             i.e. rotation between North-East-Down and world (+X,+Y,+Z) frame is defined by SphericalCoordinates class.
             Example sdf given world is NWU: parent_frame="world", custom_rpy="M_PI 0 0"
          - IMU reports in ENU frame.
             Uses SphericalCoordinates class to determine world frame in relation to magnetic north and gravity;
             i.e. rotation between East-North-Up and world (+X,+Y,+Z) frame is defined by SphericalCoordinates class.
             Example sdf given world is NWU: parent_frame="world", custom_rpy="0 0 -0.5*M_PI"
          - IMU reports in ROS optical frame as described in http://www.ros.org/reps/rep-0103.html#suffix-frames, which is
             (z-forward, x-left to right when facing +z, y-top to bottom when facing +z).
             (default gazebo camera is +x:view direction, +y:left, +z:up).
             Example sdf: parent_frame="local", custom_rpy="-0.5*M_PI 0 -0.5*M_PI"
      </description>
      <attribute name="parent_frame" type="string" default="" required="0">
        <description>
          Name of parent frame which the custom_rpy transform is defined relative to.
          It can be any valid fully scoped Gazebo Link name or the special reserved "world" frame.
          If left empty, use the sensor's own local frame.
        </description>
      </attribute>
    </element>
    <element name="grav_dir_x" type="vector3" default="1 0 0" required="0">
      <description>
        Used when localization is set to GRAV_UP or GRAV_DOWN, a projection of this vector
        into a plane that is orthogonal to the gravity vector
        defines the direction of the IMU reference frame's X-axis.
        grav_dir_x is  defined in the coordinate frame as defined by the parent_frame element.
      </description>
      <attribute name="parent_frame" type="string" default="" required="0">
        <description>
          Name of parent frame in which the grav_dir_x vector is defined.
          It can be any valid fully scoped Gazebo Link name or the special reserved "world" frame.
          If left empty, use the sensor's own local frame.
        </description>
      </attribute>
    </element>
  </element>

  <element name="angular_velocity" required="0">
    <description>These elements are specific to body-frame angular velocity,
    which is expressed in radians per second</description>
    <element name="x" required="0">
      <description>Angular velocity about the X axis</description>
      <include filename="noise.sdf" required="0"/>
    </element>
    <element name="y" required="0">
      <description>Angular velocity about the Y axis</description>
      <include filename="noise.sdf" required="0"/>
    </element>
    <element name="z" required="0">
      <description>Angular velocity about the Z axis</description>
      <include filename="noise.sdf" required="0"/>
    </element>
  </element>

  <element name="linear_acceleration" required="0">
    <description>These elements are specific to body-frame linear acceleration,
    which is expressed in meters per second squared</description>
    <element name="x" required="0">
      <description>Linear acceleration about the X axis</description>
      <include filename="noise.sdf" required="0"/>
    </element>
    <element name="y" required="0">
      <description>Linear acceleration about the Y axis</description>
      <include filename="noise.sdf" required="0"/>
    </element>
    <element name="z" required="0">
      <description>Linear acceleration about the Z axis</description>
      <include filename="noise.sdf" required="0"/>
    </element>
  </element>

  <element name="enable_orientation" type="bool" default="true" required="0">
    <description>Some IMU sensors rely on external filters to produce orientation estimates. True to generate and output orientation data, false to disable orientation data generation.</description>
  </element>
</element>
"""