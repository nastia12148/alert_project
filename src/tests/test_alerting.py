from hypothesis.extra.pandas import data_frames, column, range_indexes
from hypothesis import given, settings, strategies as st
from src.alerting.alert_system import alert, alert_by_id
import pandas as pd


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


def create_dataframe_by_alerts(alerts: int) -> pd.DataFrame:
    test_df = pd.DataFrame(columns=[
        "severity", "bundle_id", "date"])
    print(test_df.columns.tolist())

    beg_time: float = st.floats(min_value=16314, max_value=273140).example()

    while alerts > 0:
        k = st.integers(min_value=1, max_value=alerts).example()

        for i in range(0, st.integers(min_value=0, max_value=10).example()):
            time: float = beg_time + st.floats(min_value=0, max_value=100.0).example()
            test_df = test_df.append({"severity": "Successful", "bundle_id": st.sampled_from(
                [
                    "com.thg.battleops.shooting.game",
                    "com.pregnantcatemma.virtualpet",
                    "com.mytalkingcatemma.ballerinagames",
                    "com.sayollo.cobra_Android_RealBundleId",
                    "com.sayollo.cobra2_Android_RealBundleId",
                    "com.sayollo.JetpackCatGame",
                ]
            ).example(), "date": time}, ignore_index=True)

        for i in range(0, k + 10):
            time: float = beg_time + 0.000001*i + st.floats(min_value=0.1, max_value=58.9).example()
            test_df = test_df.append({"severity": "Error", "bundle_id": st.sampled_from(
                [
                    "com.thg.battleops.shooting.game",
                    "com.pregnantcatemma.virtualpet",
                    "com.mytalkingcatemma.ballerinagames",
                    "com.sayollo.cobra_Android_RealBundleId",
                    "com.sayollo.cobra2_Android_RealBundleId",
                    "com.sayollo.JetpackCatGame",
                ]
            ).example(), "date": time}, ignore_index=True)

        beg_time: float = beg_time + st.floats(min_value=120.0,
                                               max_value=273140 - (alerts - k) * 61.0).example()

        alerts = alerts - k

    return test_df


def hyp_generate_bundle_id():
    bundle_id = st.sampled_from(
        [
            "com.thg.battleops.shooting.game",
            "com.pregnantcatemma.virtualpet",
            "com.mytalkingcatemma.ballerinagames",
            "com.sayollo.cobra_Android_RealBundleId",
            "com.sayollo.cobra2_Android_RealBundleId",
            "com.sayollo.JetpackCatGame",
        ]
    )
    return bundle_id


@settings(max_examples=10)
@given(df=hyp_create_dataframe())
def test_alert_(df):
    print(df)
    print(alert(df))
    assert 1


@settings(max_examples=10)
@given(df=hyp_create_dataframe(), bundle_id=hyp_generate_bundle_id())
def test_alert_by_id(df, bundle_id):
    print(df)
    print(bundle_id)
    print(alert_by_id(df, bundle_id))
    assert 1


def test_alert(alerts=st.integers(min_value=1, max_value=10).example()):
    df = create_dataframe_by_alerts(alerts)
    assert (alert(df) == alerts)
