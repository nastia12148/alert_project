import pandas as pd
import logging

logger = logging.getLogger(__name__)


def log_reader(filepath):
    log_table = pd.read_csv(
        filepath,
        names=[
            "error_code",
            "error_message",
            "severity",
            "log_location",
            "mode",
            "model",
            "graphics",
            "session_id",
            "sdkv",
            "test_mode",
            "flow_id",
            "flow_type",
            "sdk_date",
            "publisher_id",
            "game_id",
            "bundle_id",
            "appv",
            "language",
            "os",
            "adv_id",
            "gdpr",
            "ccpa",
            "country_code",
            "date",
        ],
        dtype={"test_mode": str, "gdpr": str, "ccpa": str},
        skiprows=1,
    )

    logger.info("file is read")

    log_table = log_table.loc[:, ["severity", "bundle_id", "date"]]

    logger.info("returned table is:\n" + str(log_table.head()))

    return log_table


def alert(log_table: pd.DataFrame, time: int = 60):
    log_table = log_table[log_table["severity"] == "Error"]

    if log_table.empty:
        logger.info("log table is empty")
        return 0

    row_number = 0
    beg_time = log_table.iloc[0, 2]
    alert_counter = 0

    while row_number < len(log_table) - 11:
        error_list = log_table[(beg_time - log_table["date"]) <= time].head(11)
        if len(error_list) > 10:
            logger.warning("Alert!")
            row_number += 1
            alert_counter += 1
            beg_time = log_table.iloc[row_number, 2]
        else:
            row_number += 1
            beg_time = log_table.iloc[row_number, 2]

    return str("Amount of more than 11 alerts: " + str(alert_counter))


def alert_by_id(log_table: pd.DataFrame, bundle_id: str):
    log_table = log_table[log_table["bundle_id"] == bundle_id]

    return alert(log_table, 3600)


df = log_reader("data/data.csv")

print(alert(df))
# print(alert_by_id(df, "com.thg.battleops.shooting.game"))
