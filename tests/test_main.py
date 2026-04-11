from accel6050.mpu6050 import initialize


def test_sensor():
    r = initialize()
    v = r()
    assert v is not None
