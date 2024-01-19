# Databricks notebook source
# MAGIC %run "./functions"

# COMMAND ----------

# DBTITLE 1,Import libraries
from pyspark.sql.functions import *

# COMMAND ----------

# DBTITLE 1,Load in Data from Bronze

assistance_df = load_csv_data(container_name, storage_acct_name, assistance)
contract_df = load_csv_data(container_name, storage_acct_name, contract)


# COMMAND ----------

# DBTITLE 1,Columns we want
wanted_cols = [
    "contract_transaction_unique_key",
    "contract_award_unique_key",
    "assistance_transaction_unique_key",
    "assistance_award_unique_key",
    "modification_number",
    "federal_action_obligation",
    "total_obligated_amount",
    "total_dollars_obligated",
    "total_outlayed_amount_for_overall_award",
    "face_value_of_loan",
    "original_loan_subsidy_cost",
    "total_face_value_of_loan",
    "total_loan_subsidy_cost",
    "disaster_emergency_fund_codes_for_overall_award",
    "outlayed_amount_from_COVID-19_supplementals_for_overall_award",
    "obligated_amount_from_COVID-19_supplementals_for_overall_award",
    "action_date",
    "action_date_fiscal_year",
    "awarding_agency_code",
    "awarding_agency_name",
    "awarding_sub_agency_code",
    "awarding_sub_agency_name",
    "awarding_office_code",
    "awarding_office_name",
    "funding_agency_code",
    "funding_agency_name",
    "funding_sub_agency_code",
    "funding_sub_agency_name",
    "funding_office_code",
    "funding_office_name",
    "object_classes_funding_this_award",
    "program_activities_funding_this_award",
    "recipient_uei",
    "recipient_name_raw",
    "recipient_parent_uei",
    "recipient_parent_name_raw",
    "recipient_country_code",
    "recipient_country_name",
    "recipient_city_code",
    "recipient_city_name",
    "prime_award_transaction_recipient_county_fips_code",
    "recipient_county_name",
    "prime_award_transaction_recipient_state_fips_code",
    "recipient_state_code",
    "recipient_state_name",
    "recipient_zip_code",
    "recipient_zip_last_4_code",
    "prime_award_transaction_recipient_cd_original",
    "prime_award_transaction_recipient_cd_current",
    "recipient_foreign_city_name",
    "recipient_foreign_province_name",
    "recipient_foreign_postal_code",
    "primary_place_of_performance_scope",
    "primary_place_of_performance_country_code",
    "primary_place_of_performance_country_name",
    "primary_place_of_performance_code",
    "primary_place_of_performance_city_name",
    "prime_award_transaction_place_of_performance_county_fips_code",
    "primary_place_of_performance_county_name",
    "prime_award_transaction_place_of_performance_state_fips_code",
    "primary_place_of_performance_state_name",
    "primary_place_of_performance_zip_4",
    "prime_award_transaction_place_of_performance_cd_original",
    "prime_award_transaction_place_of_performance_cd_current",
    "primary_place_of_performance_foreign_location",
    "cfda_number",
    "cfda_title",
    "naics_code",
    "naics_description",
    "place_of_manufacture_code",
    "place_of_manufacture",
    "national_interest_action_code",
    "national_interest_action",
    "country_of_product_or_service_origin_code",
    "country_of_product_or_service_origin",
    "contingency_humanitarian_or_peacekeeping_operation_code",
    "contingency_humanitarian_or_peacekeeping_operation",
    "contracting_officers_determination_of_business_size",
    "contracting_officers_determination_of_business_size_code",
    "business_types_code",
    "business_types_description",
    "correction_delete_indicator_code",
    "correction_delete_indicator_description",
    "action_type_code",
    "action_type_description",
    "record_type_code",
    "record_type_description",
    "domestic_or_foreign_entity_code",
    "domestic_or_foreign_entity",
    "foreign_funding",
    "domestic_or_foreign_entity_code",
    "domestic_or_foreign_entity",
    "foreign_funding_description",
    "product_or_service_code",
    "product_or_service_code_description",
    "highly_compensated_officer_1_name",
    "highly_compensated_officer_1_amount",
    "highly_compensated_officer_2_name",
    "highly_compensated_officer_2_amount",
    "highly_compensated_officer_3_name",
    "highly_compensated_officer_3_amount",
    "highly_compensated_officer_4_name",
    "highly_compensated_officer_4_amount",
    "highly_compensated_officer_5_name",
    "highly_compensated_officer_5_amount",
    "last_modified_date",
]

# COMMAND ----------

# DBTITLE 1,Select columns for each award
assistance_df = assistance_df.select([col for col in wanted_cols if col in assistance_df.columns])
contract_df = contract_df.select([col for col in wanted_cols if col in contract_df.columns])

# COMMAND ----------

# DBTITLE 1,Rename columns and Add New column
assistance_df = (
    assistance_df
        .withColumnRenamed('assistance_transaction_unique_key', 'transaction_unique_key')
        .withColumnRenamed('assistance_award_unique_key', 'award_unique_key')
        .withColumn('award_type', lit('assistance'))
)
contract_df = (
    contract_df
        .withColumnRenamed('contract_transaction_unique_key', 'transaction_unique_key')
        .withColumnRenamed('total_dollars_obligated', 'total_obligated_amount')
        .withColumnRenamed('contract_award_unique_key', 'award_unique_key')
        .withColumn('award_type', lit('contract'))
)

# COMMAND ----------


