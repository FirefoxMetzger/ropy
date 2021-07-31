from xml.etree import ElementTree
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.exceptions import ParserError as XSDataParserError
import io
from typing import Dict, Callable, Type, TypeVar

from .models.v15 import Sdf as SDFv15
from .models.v16 import Sdf as SDFv16
from .models.v17 import Sdf as SDFv17
from .models.v18 import Sdf as SDFv18

T = TypeVar("T")

# available SDF elements by version
_parser_roots = {
    "1.0": None,
    "1.2": None,
    "1.3": None,
    "1.4": None,
    "1.5": SDFv15,
    "1.6": SDFv16,
    "1.7": SDFv17,
    "1.8": SDFv18,
}

# recommended to reuse the same parser context
# see: https://xsdata.readthedocs.io/en/latest/xml.html
xml_ctx = XmlContext()


class ParseError(XSDataParserError):
    pass


def get_version(sdf: str):
    """Returns the version of a SDF string.

    Parameters
    ----------
    sdf : str
        The SDFormat XML to be parsed.

    Notes
    -----
    This function only checks the root tag and does not parse the entire string.

    """

    parser = ElementTree.iterparse(io.StringIO(sdf), events=("start",))

    _, root = next(parser)

    if root.tag != "sdf":
        raise ParseError("SDF root element not found.")

    if "version" in root.attrib:
        version = root.attrib["version"]
        if version not in _parser_roots.keys():
            raise ParseError(f"Invalid version: {version}")
        return root.attrib["version"]
    else:
        raise ParseError("SDF doesnt specify a version.")


def loads(
    sdf: str,
    *,
    version: str = None,
    custom_constructor: Dict[Type[T], Callable] = None,
):
    """Convert an XML string into a sdformat.models tree.

    Parameters
    ----------
    sdf : str
        The SDFormat XML to be parsed.
    version : str
        The SDFormat version to use while parsing. If None (default) it will
        automatically determine the version from the <sdf> element. If specified
        the given version will be used instead.
    custom_constructor : Dict[Type[T], Callable]
        Overwrite the default constructor for a certain model class with
        callable. This is useful for doing pre- or post-initialization of
        bound classes or to replace them entirely.

    Returns
    -------
    SdfRoot : object
        An instance of ``ropy.ignition.models.vXX.Sdf`` where XX corresponds to the
        version of the SDFormat XML.

    Notes
    -----
    ``custom_constructure`` is currently disabled and has no effect. It will
    become available with xsData v21.8.

    """

    # Disabled until xsData upgrades to the next version
    # if custom_constructor is None:
    #     custom_constructor = dict()

    # def custom_class_factory(clazz, params):
    #     if clazz in custom_constructor:
    #         return custom_constructor[clazz](**params)

    #     return clazz(**params)

    if version is None:
        version = get_version(sdf)
    else:
        version = version

    root_class = _parser_roots[version]

    if root_class is None:
        raise ParseError(f"Ropy currently doesnt support SDFormat v{version}")

    # Disabled until xsData upgrades to the next version
    # sdf_parser = XmlParser(
    #     ParserConfig(class_factory=custom_class_factory), context=xml_ctx
    # )
    sdf_parser = XmlParser(ParserConfig(), xml_ctx)

    try:
        sdf_parser.from_string(sdf, root_class)
    except ElementTree.ParseError as e:
        raise ParseError("Invalid XML.") from e

    return sdf_parser.from_string(sdf, root_class)


def dumps(root_element, *, format=False) -> str:
    """Serialize a SDFormat object to an XML string.

    Parameters
    ----------
    root_element : object
        An instance of ``ropy.ignition.models.vXX.Sdf``. XX represents the SDFormat
        version and can be any version currently supported by ropy.
    format : bool
        If true, add indentation and linebreaks to the output to increase human
        readability. If false (default) the entire XML will appear as a single
        line with no spaces between elements.

    Returns
    -------
    sdformat_string : str
        A string containing SDFormat XML representing the given input.

    """
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=format))

    return serializer.render(root_element)