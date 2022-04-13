# Road traffic data project 

You are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setup that uses different file formats. In the first Hands-on Lab, your job is to collect data available in different formats and, consolidate it into a single file.

As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id, and timestamp are streamed to Kafka. In the second Hands-on Lab, your job is to create a data pipeline that collects the streaming data and loads it into a database. 

**Final Airflow Dag in file ETL_toll_data.py**

ETL Workflow:
- Airflow task to unzip data
- Airflow task to extract data from csv file
- Airflow task to extract data from tsv file
- Airflow task to extract data from fixed width file
- Airflow task to consolidate data extracted from previous task
- Airflow task to transform and load the data
- Define the task pipeline
