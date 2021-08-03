from dataclasses import dataclass, field
from typing import List, Optional
from .actor import Actor
from .joint import Joint
from .light import Light
from .model import Model
from .physics import Physics
from .scene import Scene
from .state import State

__NAMESPACE__ = "sdformat/v1.0/world.xsd"


@dataclass
class World:
    class Meta:
        name = "world"

    gui: Optional["World.Gui"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    physics: Optional[Physics] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    scene: Optional[Scene] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    light: List[Light] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    model: List[Model] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    actor: List[Actor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    plugin: List["World.Plugin"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    joint: List[Joint] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    road: List["World.Road"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    state: List[State] = field(
        default_factory=list,
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
    class Gui:
        camera: Optional["World.Gui.Camera"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
        fullscreen: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass
        class Camera:
            view_controller: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            origin: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            track_visual: Optional["World.Gui.Camera.TrackVisual"] = field(
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
            class TrackVisual:
                name: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )
                min_dist: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )
                max_dist: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    }
                )

    @dataclass
    class Plugin:
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        filename: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Road:
        width: Optional[float] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        point: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
                "pattern": r"(\s*(-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+)\s+){2}((-|\+)?(\d+(\.\d*)?|\.\d+|\d+\.\d+[eE][-\+]?[0-9]+))\s*",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
