import warnings

from .base import ElementBase


class Plugin(ElementBase):
    def __init__(self, *, sdf_version: str) -> None:
        warnings.warn("`Plugin` has not been implemented yet.")
        super().__init__(sdf_version=sdf_version)


"""<!-- Plugin -->
<element name="plugin" required="*">
  <description>A plugin is a dynamically loaded chunk of code. It can exist as a child of world, model, and sensor.</description>
  <attribute name="name" type="string" default="__default__" required="1">
    <description>A unique name for the plugin, scoped to its parent.</description>
  </attribute>
  <attribute name="filename" type="string" default="__default__" required="1">
    <description>Name of the shared library to load. If the filename is not a full path name, the file will be searched for in the configuration paths.</description>
  </attribute>
  <element copy_data="true" required="*">
    <description>This is a special element that should not be specified in an SDFormat file. It automatically copies child elements into the SDFormat element so that a plugin can access the data.</description>
  </element>
</element> <!-- End Plugin -->
"""
