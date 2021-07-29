import pytest


@pytest.fixture
def light_sdf():
    sdf_string = """<?xml version="1.0" ?>
    <sdf version="1.5">
        <light type="point" name="point_light">
        <pose>0 2 2 0 0 0</pose>
        <diffuse>1 0 0 1</diffuse>
        <specular>.1 .1 .1 1</specular>
        <attenuation>
            <range>20</range>
            <linear>0.2</linear>
            <constant>0.8</constant>
            <quadratic>0.01</quadratic>
        </attenuation>
        <cast_shadows>false</cast_shadows>
        </light>
    </sdf>
    """

    return sdf_string
