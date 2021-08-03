from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "sdformat/v1.7/material.xsd"


@dataclass
class Material:
    """
    The material of the visual element.

    Parameters
    ----------
    script: Name of material from an installed script file. This will
        override the color element if the script exists.
    shader:
    render_order: Set render order for coplanar polygons. The higher
        value will be rendered on top of the other coplanar polygons
    lighting: If false, dynamic lighting will be disabled
    ambient: The ambient color of a material specified by set of four
        numbers representing red/green/blue, each in the range of [0,1].
    diffuse: The diffuse color of a material specified by set of four
        numbers representing red/green/blue/alpha, each in the range of
        [0,1].
    specular: The specular color of a material specified by set of four
        numbers representing red/green/blue/alpha, each in the range of
        [0,1].
    emissive: The emissive color of a material specified by set of four
        numbers representing red/green/blue, each in the range of [0,1].
    double_sided: If true, the mesh that this material is applied to
        will be rendered as double sided
    pbr: Physically Based Rendering (PBR) material. There are two PBR
        workflows: metal and specular. While both workflows and their
        parameters can be specified at the same time, typically only one
        of them will be used (depending on the underlying renderer
        capability). It is also recommended to use the same workflow for
        all materials in the world.
    """
    class Meta:
        name = "material"

    script: Optional["Material.Script"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    shader: Optional["Material.Shader"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    render_order: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    lighting: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    ambient: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"(\s*\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){3}\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s*",
        }
    )
    diffuse: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"(\s*\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){3}\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s*",
        }
    )
    specular: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"(\s*\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){3}\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s*",
        }
    )
    emissive: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"(\s*\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){3}\+?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s*",
        }
    )
    double_sided: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    pbr: Optional["Material.Pbr"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Script:
        """Name of material from an installed script file.

        This will override the color element if the script exists.

        Parameters
        ----------
        uri: URI of the material script file
        name: Name of the script within the script file
        """
        uri: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )

    @dataclass
    class Shader:
        """
        Parameters
        ----------
        normal_map: filename of the normal map
        type: vertex, pixel, normal_map_object_space,
            normal_map_tangent_space
        """
        normal_map: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Pbr:
        """Physically Based Rendering (PBR) material.

        There are two PBR workflows: metal and specular. While both
        workflows and their parameters can be specified at the same
        time, typically only one of them will be used (depending on the
        underlying renderer capability). It is also recommended to use
        the same workflow for all materials in the world.

        Parameters
        ----------
        metal: PBR using the Metallic/Roughness workflow.
        specular: PBR using the Specular/Glossiness workflow.
        """
        metal: Optional["Material.Pbr.Metal"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        specular: Optional["Material.Pbr.Specular"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class Metal:
            """
            PBR using the Metallic/Roughness workflow.

            Parameters
            ----------
            albedo_map: Filename of the diffuse/albedo map.
            roughness_map: Filename of the roughness map.
            roughness: Material roughness in the range of [0,1], where 0
                represents a smooth surface and 1 represents a rough
                surface. This is the inverse of a specular map in a PBR
                specular workflow.
            metalness_map: Filename of the metalness map.
            metalness: Material metalness in the range of [0,1], where 0
                represents non-metal and 1 represents raw metal
            environment_map: Filename of the environment / reflection
                map, typically in the form of a cubemap
            ambient_occlusion_map: Filename of the ambient occlusion
                map. The map defines the amount of ambient lighting on
                the surface.
            normal_map: Filename of the normal map. The normals can be
                in the object space or tangent space as specified in the
                'type' attribute
            emissive_map: Filename of the emissive map.
            light_map: Filename of the light map. The light map is a
                prebaked light texture that is applied over the albedo
                map
            """
            albedo_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            roughness_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            roughness: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            metalness_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            metalness: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            environment_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ambient_occlusion_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            normal_map: Optional["Material.Pbr.Metal.NormalMap"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            emissive_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            light_map: Optional["Material.Pbr.Metal.LightMap"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class NormalMap:
                """
                Parameters
                ----------
                value:
                type: The space that the normals are in. Values are:
                    'object' or 'tangent'
                """
                value: Optional[str] = field(
                    default=None,
                    metadata={
                        "required": True,
                    }
                )
                type: str = field(
                    default="tangent",
                    metadata={
                        "type": "Attribute",
                    }
                )

            @dataclass
            class LightMap:
                """
                Parameters
                ----------
                value:
                uv_set: Index of the texture coordinate set to use.
                """
                value: Optional[str] = field(
                    default=None,
                    metadata={
                        "required": True,
                    }
                )
                uv_set: int = field(
                    default=0,
                    metadata={
                        "type": "Attribute",
                    }
                )

        @dataclass
        class Specular:
            """
            PBR using the Specular/Glossiness workflow.

            Parameters
            ----------
            albedo_map: Filename of the diffuse/albedo map.
            specular_map: Filename of the specular map.
            glossiness_map: Filename of the glossiness map.
            glossiness: Material glossiness in the range of [0-1], where
                0 represents a rough surface and 1 represents a smooth
                surface. This is the inverse of a roughness map in a PBR
                metal workflow.
            ambient_occlusion_map: Filename of the ambient occlusion
                map. The map defines the amount of ambient lighting on
                the surface.
            normal_map: Filename of the normal map. The normals can be
                in the object space or tangent space as specified in the
                'type' attribute
            emissive_map: Filename of the emissive map.
            light_map: Filename of the light map. The light map is a
                prebaked light texture that is applied over the albedo
                map
            """
            albedo_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            specular_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            glossiness_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            glossiness: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ambient_occlusion_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            normal_map: Optional["Material.Pbr.Specular.NormalMap"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            emissive_map: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            light_map: Optional["Material.Pbr.Specular.LightMap"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class NormalMap:
                """
                Parameters
                ----------
                value:
                type: The space that the normals are in. Values are:
                    'object' or 'tangent'
                """
                value: Optional[str] = field(
                    default=None,
                    metadata={
                        "required": True,
                    }
                )
                type: str = field(
                    default="tangent",
                    metadata={
                        "type": "Attribute",
                    }
                )

            @dataclass
            class LightMap:
                """
                Parameters
                ----------
                value:
                uv_set: Index of the texture coordinate set to use.
                """
                value: Optional[str] = field(
                    default=None,
                    metadata={
                        "required": True,
                    }
                )
                uv_set: int = field(
                    default=0,
                    metadata={
                        "type": "Attribute",
                    }
                )