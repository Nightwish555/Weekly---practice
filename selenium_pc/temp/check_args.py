
def check_time_out(time_to_wait):
    return int(float(time_to_wait) * 1000)


def test_check_time_out():
    #try:
        print(check_time_out("err"))
        assert isinstance(check_time_out("50"), int)
        assert isinstance(check_time_out("1.0"), int)
        assert isinstance(check_time_out("1.5"), int)
        assert isinstance(check_time_out("err"),int)
    # except Exception as e:
    #     print(e)

