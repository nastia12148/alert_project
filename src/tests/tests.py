from hypothesis.extra.pandas import data_frames, column, range_indexes
from hypothesis import given, settings, strategies as st
from src.alert_system import alert


def hyp_create_dataframe():
    severity = st.sampled_from(["Error", "Successful"])
    data = data_frames(
        columns=[
            column(name="severity", elements=severity),
            column(
                name="bundle_id",
                elements=st.sampled_from(
                    [
                        "com.thg.battleops.shooting.game",
                        "com.pregnantcatemma.virtualpet",
                        "com.mytalkingcatemma.ballerinagames",
                        "com.sayollo.cobra_Android_RealBundleId",
                        "com.sayollo.cobra2_Android_RealBundleId",
                        "com.sayollo.JetpackCatGame",
                    ]
                ),
            ),
            column(
                name="date",
                elements=st.floats(
                    min_value=1531442679.384516, max_value=1631442730.384516
                ),
            ),
        ],
        index=range_indexes(min_size=100),
    )

    return data


@given(df=hyp_create_dataframe())
@settings(max_examples=50)
def test_hypothesis(df):
    print(df)
    print(alert(df))
    assert 1
