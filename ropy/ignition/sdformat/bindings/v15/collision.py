from dataclasses import dataclass, field
from typing import List, Optional
from .geometry import Geometry

__NAMESPACE__ = "sdformat/v1.5/collision.xsd"


@dataclass
class Collision:
    """The collision properties of a link.

    Note that this can be different from the visual properties of a
    link, for example, simpler collision models are often used to reduce
    computation time.

    Parameters
    ----------
    laser_retro: intensity value returned by laser sensor.
    max_contacts: Maximum number of contacts allowed between two
        entities. This value overrides the max_contacts element defined
        in physics.
    frame: A frame of reference to which a pose is relative.
    pose: A position(x,y,z) and orientation(roll, pitch yaw) with
        respect to the specified frame.
    geometry: The shape of the visual or collision object.
    surface: The surface parameters
    name: Unique name for the collision element within the scope of the
        parent link.
    """
    class Meta:
        name = "collision"

    laser_retro: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    max_contacts: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    frame: List["Collision.Frame"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    pose: Optional["Collision.Pose"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: Optional[Geometry] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    surface: Optional["Collision.Surface"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Frame:
        """
        A frame of reference to which a pose is relative.

        Parameters
        ----------
        pose: A position(x,y,z) and orientation(roll, pitch yaw) with
            respect to the specified frame.
        name: Name of the frame. This name must not match another frame
            defined inside the parent that this frame is attached to.
        """
        pose: Optional["Collision.Frame.Pose"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

        @dataclass
        class Pose:
            """
            Parameters
            ----------
            value:
            frame: Name of frame which the pose is defined relative to.
            """
            value: Optional[str] = field(
                default=None,
                metadata={
                    "required": True,
                    "pattern": r"(\s*(-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){5}((-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+))\s*",
                }
            )
            frame: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                }
            )

    @dataclass
    class Pose:
        """
        Parameters
        ----------
        value:
        frame: Name of frame which the pose is defined relative to.
        """
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"(\s*(-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){5}((-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+))\s*",
            }
        )
        frame: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Surface:
        """
        The surface parameters.
        """
        bounce: Optional["Collision.Surface.Bounce"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        friction: Optional["Collision.Surface.Friction"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        contact: Optional["Collision.Surface.Contact"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        soft_contact: Optional["Collision.Surface.SoftContact"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class Bounce:
            """
            Parameters
            ----------
            restitution_coefficient: Bounciness coefficient of
                restitution, from [0...1], where 0=no bounciness.
            threshold: Bounce capture velocity, below which effective
                coefficient of restitution is 0.
            """
            restitution_coefficient: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            threshold: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class Friction:
            """
            Parameters
            ----------
            torsional: Parameters for torsional friction
            ode: ODE friction parameters
            bullet:
            """
            torsional: Optional["Collision.Surface.Friction.Torsional"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ode: Optional["Collision.Surface.Friction.Ode"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            bullet: Optional["Collision.Surface.Friction.Bullet"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Torsional:
                """
                Parameters for torsional friction.

                Parameters
                ----------
                coefficient: Torsional friction coefficient in the range
                    of [0..1].
                use_patch_radius: If this flag is true,
                    torsional friction is calculated using the
                    "patch_radius" parameter.           If this flag is
                    set to false,           "surface_radius" (R) and
                    contact depth (d)           are used to compute the
                    patch radius as sqrt(R*d).
                patch_radius: Radius of contact patch surface.
                surface_radius: Surface radius on the point of contact.
                ode: Torsional friction parameters for ODE
                """
                coefficient: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                use_patch_radius: Optional[bool] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                patch_radius: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                surface_radius: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                ode: Optional["Collision.Surface.Friction.Torsional.Ode"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )

                @dataclass
                class Ode:
                    """
                    Torsional friction parameters for ODE.

                    Parameters
                    ----------
                    slip: Force dependent slip for torsional friction,
                        between the range of [0..1].
                    """
                    slip: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "",
                        }
                    )

            @dataclass
            class Ode:
                """
                ODE friction parameters.

                Parameters
                ----------
                mu: Coefficient of friction in the range of [0..1].
                mu2: Second coefficient of friction in the range of
                    [0..1]
                fdir1: 3-tuple specifying direction of mu1 in the
                    collision local reference frame.
                slip1: Force dependent slip direction 1 in collision
                    local frame, between the range of [0..1].
                slip2: Force dependent slip direction 2 in collision
                    local frame, between the range of [0..1].
                """
                mu: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                mu2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                fdir1: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "pattern": r"(\s*(-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){2}((-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+))\s*",
                    }
                )
                slip1: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                slip2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )

            @dataclass
            class Bullet:
                """
                Parameters
                ----------
                friction: Coefficient of friction in the range of
                    [0..1].
                friction2: Coefficient of friction in the range of
                    [0..1].
                fdir1: 3-tuple specifying direction of mu1 in the
                    collision local reference frame.
                rolling_friction: coefficient of friction in the range
                    of [0..1]
                """
                friction: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                friction2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                fdir1: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "pattern": r"(\s*(-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){2}((-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+))\s*",
                    }
                )
                rolling_friction: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )

        @dataclass
        class Contact:
            """
            Parameters
            ----------
            collide_without_contact: Flag to disable contact force
                generation, while still allowing collision checks and
                contact visualization to occur.
            collide_without_contact_bitmask: Bitmask for collision
                filtering when collide_without_contact is on
            collide_bitmask: Bitmask for collision filtering. This will
                override collide_without_contact. Parsed as 16-bit
                unsigned integer.
            poissons_ratio: Poisson's ratio is the ratio between
                transverse and axial strain.         This value must lie
                between (-1, 0.5).  Defaults to 0.3 for typical steel.
                Note typical silicone elastomers have Poisson's ratio
                near 0.49 ~ 0.50.          For reference, approximate
                values for Material:(Young's Modulus, Poisson's Ratio)
                for some of the typical materials are:
                Plastic:  (1e8 ~ 3e9 Pa,  0.35 ~ 0.41),           Wood:
                (4e9 ~ 1e10 Pa, 0.22 ~ 0.50),           Aluminum: (7e10
                Pa,       0.32 ~ 0.35),           Steel:    (2e11 Pa,
                0.26 ~ 0.31).
            elastic_modulus: Young's Modulus in SI derived unit Pascal.
                Defaults to -1.  If value is less or equal to zero,
                contact using elastic modulus (with Poisson's Ratio) is
                disabled.          For reference, approximate values for
                Material:(Young's Modulus, Poisson's Ratio)         for
                some of the typical materials are:           Plastic:
                (1e8 ~ 3e9 Pa,  0.35 ~ 0.41),           Wood:     (4e9 ~
                1e10 Pa, 0.22 ~ 0.50),           Aluminum: (7e10 Pa,
                0.32 ~ 0.35),           Steel:    (2e11 Pa,       0.26 ~
                0.31).
            ode: ODE contact parameters
            bullet: Bullet contact parameters
            """
            collide_without_contact: Optional[bool] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            collide_without_contact_bitmask: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            collide_bitmask: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            poissons_ratio: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            elastic_modulus: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            ode: Optional["Collision.Surface.Contact.Ode"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            bullet: Optional["Collision.Surface.Contact.Bullet"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Ode:
                """
                ODE contact parameters.

                Parameters
                ----------
                soft_cfm: Soft constraint force mixing.
                soft_erp: Soft error reduction parameter
                kp: dynamically "stiffness"-equivalent coefficient for
                    contact joints
                kd: dynamically "damping"-equivalent coefficient for
                    contact joints
                max_vel: maximum contact correction velocity truncation
                    term.
                min_depth: minimum allowable depth before contact
                    correction impulse is applied
                """
                soft_cfm: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                soft_erp: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                kp: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                kd: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                max_vel: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                min_depth: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )

            @dataclass
            class Bullet:
                """
                Bullet contact parameters.

                Parameters
                ----------
                soft_cfm: Soft constraint force mixing.
                soft_erp: Soft error reduction parameter
                kp: dynamically "stiffness"-equivalent coefficient for
                    contact joints
                kd: dynamically "damping"-equivalent coefficient for
                    contact joints
                split_impulse: Similar to ODE's max_vel implementation.
                    See
                    http://bulletphysics.org/mediawiki-1.5.8/index.php/BtContactSolverInfo#Split_Impulse
                    for more information.
                split_impulse_penetration_threshold: Similar to ODE's
                    max_vel implementation.  See
                    http://bulletphysics.org/mediawiki-1.5.8/index.php/BtContactSolverInfo#Split_Impulse
                    for more information.
                """
                soft_cfm: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                soft_erp: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                kp: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                kd: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                split_impulse: Optional[bool] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )
                split_impulse_penetration_threshold: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )

        @dataclass
        class SoftContact:
            """
            Parameters
            ----------
            dart: soft contact pamameters based on paper:
                http://www.cc.gatech.edu/graphics/projects/Sumit/homepage/papers/sigasia11/jain_softcontacts_siga11.pdf
            """
            dart: Optional["Collision.Surface.SoftContact.Dart"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Dart:
                """
                soft contact pamameters based on paper:              http://www
                .cc.gatech.edu/graphics/projects/Sumit/homepage/papers/sigasia1
                1/jain_softcontacts_siga11.pdf.

                Parameters
                ----------
                bone_attachment: This is variable k_v in the soft
                    contacts paper.  Its unit is N/m.
                stiffness: This is variable k_e in the soft contacts
                    paper.  Its unit is N/m.
                damping: Viscous damping of point velocity in body
                    frame.  Its unit is N/m/s.
                flesh_mass_fraction: Fraction of mass to be distributed
                    among deformable nodes.
                """
                bone_attachment: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )
                stiffness: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )
                damping: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )
                flesh_mass_fraction: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )