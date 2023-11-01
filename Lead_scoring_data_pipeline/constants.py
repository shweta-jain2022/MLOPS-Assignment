# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = '/home/airflow/dags/Lead_scoring_data_pipeline/'
DB_FILE_NAME = 'lead_scoring_data_cleaning.db'
UNIT_TEST_DB_FILE_NAME = ''
DATA_DIRECTORY = '/home/airflow/dags/Lead_scoring_data_pipeline/data/'
RAW_FILE = 'leadscoring.csv'
INFERENCE_FILE = 'leadscoring_inference.csv'
FLAG = 1   ## 0:Use RAW_FILE, 1:Use INFERENCE_FILE
INTERACTION_MAPPING = '/home/airflow/dags/Lead_scoring_data_pipeline/mapping/interaction_mapping.csv'
INDEX_COLUMNS_TRAINING = ['created_date', 'first_platform_c','first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier','referred_lead', 'app_complete_flag']
INDEX_COLUMNS_INFERENCE = ['created_date', 'first_platform_c','first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier','referred_lead']
NOT_FEATURES = ['created_date', 'assistance_interaction', 'career_interaction','payment_interaction', 'social_interaction', 'syllabus_interaction']




