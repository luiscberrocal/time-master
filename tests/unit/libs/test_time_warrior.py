from time_master.libs.time_warrior import TimeWarriorWrapper


class TestTimeWarriorWrapper:
    def test_summary(self) -> None:
        tw = TimeWarriorWrapper()
        tw.summary("yesterday")

        assert tw.summary() == "summary"
