import pytest
from pathlib import Path
import numpy as np

import skbot.ignition as ign
import skbot.transform as tf


def test_v18_parsing(v18_sdf):
    try:
        frame = ign.sdformat.to_frame_graph(v18_sdf)
    except NotImplementedError:
        pytest.skip("Elements not implemented yet.")

    if isinstance(frame, list):
        assert len(frame) > 1
        for el in frame:
            assert isinstance(el, tf.Frame)
    else:
        assert isinstance(frame, tf.Frame)


def test_v18_parsing_wrapped(v18_sdf):
    try:
        frame_list = ign.sdformat.to_frame_graph(v18_sdf, unwrap=False)
    except NotImplementedError:
        pytest.skip("Elements not implemented yet.")

    for el in frame_list:
        assert isinstance(el, tf.Frame)


def test_v18_refuted(v18_sdf_refuted):
    with pytest.raises(ign.sdformat.sdformat.ParseError):
        ign.sdformat.to_frame_graph(v18_sdf_refuted)


def test_v17_parsing(v17_sdf):
    try:
        frame = ign.sdformat.to_frame_graph(v17_sdf)
    except NotImplementedError:
        pytest.skip("Elements not implemented yet.")

    if isinstance(frame, list):
        assert len(frame) > 1
        for el in frame:
            assert isinstance(el, tf.Frame)
    else:
        assert isinstance(frame, tf.Frame)


def test_v17_refuted(v17_sdf_refuted):
    with pytest.raises(ign.sdformat.sdformat.ParseError):
        ign.sdformat.to_frame_graph(v17_sdf_refuted)


def test_v15_parsing(v15_sdf):
    try:
        frame = ign.sdformat.to_frame_graph(v15_sdf)
    except NotImplementedError:
        pytest.skip("Elements not implemented yet.")

    if isinstance(frame, list):
        assert len(frame) > 1
        for el in frame:
            assert isinstance(el, tf.Frame)
    else:
        assert isinstance(frame, tf.Frame)


def test_v15_refuted(v15_sdf_refuted):
    with pytest.raises(ign.sdformat.sdformat.ParseError):
        ign.sdformat.to_frame_graph(v15_sdf_refuted)


def test_panda():
    model_file = Path(__file__).parent / "sdf" / "robots" / "panda" / "model.sdf"
    sdf_string = model_file.read_text()

    root_frame = ign.sdformat.to_frame_graph(sdf_string)


def test_nd_panda():
    model_file = Path(__file__).parent / "sdf" / "robots" / "panda" / "model.sdf"
    sdf_string = model_file.read_text()

    root_frame = ign.sdformat.to_frame_graph(sdf_string, shape=(5, 3))


def test_poses():
    model_file = Path(__file__).parent / "sdf" / "v18" / "pose_testing.sdf"
    sdf_string = model_file.read_text()

    world = ign.sdformat.to_frame_graph(sdf_string)
    frame_a = world.find_frame("world/A")
    frame_b = world.find_frame("world/B")
    frame_c = world.find_frame("world/C")
    frame_d = world.find_frame("world/D")

    # origin tests
    origin_a = frame_a.transform((0, 0, 0), world)
    origin_b = frame_b.transform((0, 0, 0), world)
    origin_c = frame_c.transform((0, 0, 0), world)
    origin_d = frame_d.transform((0, 0, 0), world)

    assert np.allclose(origin_a, (1, 2, 3))
    assert np.allclose(origin_b, (0, 0, 0))
    assert np.allclose(origin_c, (0, 0, 0))
    assert np.allclose(origin_d, (1, 2, 3))

    # test vector x
    vector_a = frame_a.transform((1, 0, 0), world)
    vector_b = frame_b.transform((1, 0, 0), world)
    vector_c = frame_c.transform((1, 0, 0), world)
    vector_d = frame_d.transform((1, 0, 0), world)

    assert np.allclose(vector_a, (2, 2, 3))
    assert np.allclose(vector_b, (0, 1, 0))
    assert np.allclose(vector_c, (0, 0, 1))
    assert np.allclose(vector_d, (1, 2, 4))


def test_double_pendulum():
    model_file = (
        Path(__file__).parent / "sdf" / "robots" / "double_pendulum" / "model.sdf"
    )
    sdf_string = model_file.read_text()

    root_frame = ign.sdformat.to_frame_graph(sdf_string)

def test_perspective_transform():
    model_file = Path(__file__).parent / "sdf" / "v18" / "perspective_transform.sdf"
    sdf_string = model_file.read_text()

    root_frame = ign.sdformat.to_frame_graph(sdf_string)
    px_space = root_frame.find_frame(".../pixel-space")
    cam_space = root_frame.find_frame(".../camera-space")
    box = root_frame.find_frame(".../box_visual")
    vertices = np.array(
        [
            [0.025, 0.025, 0.025],#0
            [0.025, -0.025, 0.025],
            [0.025, 0.025, -0.025],
            [0.025, -0.025, -0.025],
            [-0.025, 0.025, 0.025],
            [-0.025, 0.025, -0.025],#5
            [-0.025, -0.025, 0.025],
            [-0.025, -0.025, -0.025],
        ]
    )

    edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 6),
        (2, 3),
        (2, 5),
        (3, 7),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7)
    ]

    center = np.array([0,0,0])


    from matplotlib.patches import Circle
    import matplotlib.pyplot as plt

    import imageio as iio
    img = iio.imread("test_image.png")
    _, ax = plt.subplots(1)
    ax.imshow(img)
    corner_px = box.transform(vertices, px_space)
    distance = list()
    for idx_a, idx_b in edges:
        x = np.linspace(corner_px[idx_a, 1], corner_px[idx_b, 1], 100)
        y = np.linspace(corner_px[idx_a, 0], corner_px[idx_b, 0], 100)
        ax.plot(x, y, "blue")
        distance.append(np.linalg.norm(y - x))
    
    ax.add_patch(Circle(box.transform(center, px_space)[::-1], radius=3, color="red"))

    # centered_corner_px = cam_space.transform(vertices+np.array([0.5, 0, 0]), px_space)
    # ax.scatter(centered_corner_px[:, 1], centered_corner_px[:, 0], 10)
    # ax.set_xlim([0, 1920])
    # ax.set_ylim([0, 1080])
    # ax.invert_yaxis()
    plt.show()


def test_four_goals():
    model_file = Path(__file__).parent / "sdf" / "v18" / "four_goals.sdf"
    sdf_string = model_file.read_text()

    root_frame = ign.sdformat.to_frame_graph(sdf_string)
    px_space = root_frame.find_frame(".../main_camera/.../pixel-space")
    cam_space = root_frame.find_frame(".../main_camera/.../camera-space")
    box = root_frame.find_frame(".../box_copy_0/.../box_visual")
    vertices = np.array(
        [
            [0.025, 0.025, 0.025],#0
            [0.025, -0.025, 0.025],
            [0.025, 0.025, -0.025],
            [0.025, -0.025, -0.025],
            [-0.025, 0.025, 0.025],
            [-0.025, 0.025, -0.025],#5
            [-0.025, -0.025, 0.025],
            [-0.025, -0.025, -0.025],
        ]
    )

    edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 6),
        (2, 3),
        (2, 5),
        (3, 7),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7)
    ]

    center = np.array([0,0,0])


    from matplotlib.patches import Circle
    import matplotlib.pyplot as plt
    import imageio as iio

    img = iio.imread("front_view.png")
    _, ax = plt.subplots(1)
    ax.imshow(img)
    corner_px = box.transform(vertices, px_space)
    distance = list()
    for idx_a, idx_b in edges:
        x = np.linspace(corner_px[idx_a, 1], corner_px[idx_b, 1], 100)
        y = np.linspace(corner_px[idx_a, 0], corner_px[idx_b, 0], 100)
        ax.plot(x, y, "blue")
        distance.append(np.linalg.norm(y - x))
    
    # ax.scatter(corner_px[:, 1], corner_px[:, 0], 10)
    ax.add_patch(Circle(box.transform(center, px_space)[::-1], radius=3, color="red"))

    # centered_corner_px = cam_space.transform(vertices+np.array([0.5, 0, 0]), px_space)
    # ax.scatter(centered_corner_px[:, 1], centered_corner_px[:, 0], 10)
    plt.show()

    print("")
