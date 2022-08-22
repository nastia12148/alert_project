import pandas as pd



def first_11_errors(df:pd.DataFrame, bundle_id):
    if bundle_id:
        df = df[df["bundle_id"] == bundle_id]

    df = df[df["severity"] == "Error"]
    print(df["error_message"].head(11))


df = pd.read_csv('~/PycharmProjects/alert_project/data/data.csv', names=['error_code',
                                                                         'error_message',
                                                                         'severity',
                                                                         'log_location',
                                                                         'mode',
                                                                         'model',
                                                                         'graphics',
                                                                         'session_id',
                                                                         'sdkv',
                                                                         'test_mode',
                                                                         'flow_id',
                                                                         'flow_type',
                                                                         'sdk_date',
                                                                         'publisher_id',
                                                                         'game_id',
                                                                         'bundle_id',
                                                                         'appv',
                                                                         'language',
                                                                         'os',
                                                                         'adv_id',
                                                                         'gdpr',
                                                                         'ccpa',
                                                                         'country_code',
                                                                         'date']
                 ,dtype= {'test_mode':str,'gdpr': str,'ccpa': str},skiprows=1)

#print(df["bundle_id"].unique())
#print(df["error_message"].unique())
#print(df["severity"].value_counts())

first_11_errors(df, False)

first_11_errors(df, "com.thg.battleops.shooting.game")
