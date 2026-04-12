import pytest

acc = pytest.importorskip("accel6050")
mpu = pytest.importorskip("mpu6050")


def test_sensor():
    r = mpu.initialize()
    v = r()
    assert v is not None
