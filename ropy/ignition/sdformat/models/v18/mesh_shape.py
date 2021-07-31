from dataclasses import dataclass
from .mesh_shape_type import MeshType


@dataclass
class Mesh(MeshType):
    """
    Mesh shape.
    """

    class Meta:
        name = "mesh"