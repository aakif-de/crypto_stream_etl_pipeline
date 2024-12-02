# Crypto_Stream_Etl_Pipeline

## Introduction
This project involves implementing an Realtime ETL pipeline that utilizes Coingecko API and GCP Services. The pipeline extracts data from the Coingecko API, Ingest the data using Cloud Function and Pub/Sub; performs transformations using Dataflow. From there, the data is ingested into BigQuery for further downstream tasks, analysis and insights.

## Architecture
![Animation_2](https://github.com/user-attachments/assets/e99bd27e-ece7-4e8a-aafe-15e3cde2b20b)

## Business Problem: 
The client, a cryptocurrency enthusiast and investor, wants to extract and analyze real-time data for the top 10 cryptocurrencies to gain actionable insights. This includes monitoring price trends, market capitalization, and trading volumes, which can aid in identifying investment opportunities, understanding market dynamics, and making data-driven decisions. The processed data will be stored for further analysis and visualization, helping the client track performance and predict future trends in the highly volatile crypto market.

## Dataset/API Used:
Coingecko API: The CoinGecko API is a free and robust service providing data on cryptocurrency prices, market trends, and statistics. It supports real-time and historical data analysis, making it valuable for the cryptocurrency ecosystem.

## Services Used:
1. **Cloud Schedular**: Google Cloud Scheduler is a fully managed cron job service for scheduling virtually any job, including batch, big data jobs, and cloud infrastructure tasks. It supports running tasks at specific intervals and integrates seamlessly with other Google Cloud services like Cloud Functions, Pub/Sub, and App Engine. Ideal for automating workflows.

2. **Cloud Functions**: Google Cloud Functions is a serverless computing platform that enables to run code in response to events, without provisioning or managing servers. It supports various triggers like HTTP requests, Pub/Sub events, or changes in Cloud Storage, making it a versatile tool for building lightweight, scalable applications and automating workflows.

3. **Pub/Sub**: Google Cloud Pub/Sub is a fully managed messaging service designed to enable event-driven architectures. It provides asynchronous messaging between decoupled applications, ensuring reliable and scalable communication. Ideal for real-time event streaming, Pub/Sub supports integrations with Cloud Functions, DataFlow, and BigQuery for seamless workflows.

4. **DataFlow**: Google Cloud DataFlow is a fully managed streaming and batch data processing service that supports Apache Beam pipelines. It enables real-time analytics, ETL (Extract, Transform, Load) workflows, and machine learning data preparation. With its auto-scaling and high availability features, DataFlow is ideal for processing large-scale data in real-time or batch modes.

5. **BigQuery**: Google BigQuery is a fully managed, serverless data warehouse that allows for fast SQL-like querying of massive datasets. It supports real-time analytics and integrates natively with various Google Cloud services. BigQuery's features include built-in machine learning, geospatial analysis, and seamless scalability for handling structured and semi-structured data.
   
6. **Cloud Storage**: Google Cloud Storage is a scalable, secure, and highly durable object storage solution. It supports data archiving, backup, and content delivery at a global scale. Cloud Storage integrates with other Google Cloud services like DataFlow and BigQuery, making it ideal for storing and analyzing unstructured data like multimedia files, backups, and logs. 

## Installed Packages ( Refer requiremnets.txt)
requests: Simplifies making HTTP requests and handling API responses.
google-cloud-pubsub: Enables event-driven messaging with Google Cloud Pub/Sub.

## Project Execution Flow:
Cloud Scheduler triggers Cloud Function → Cloud Function extract data from the CoinGecko API & Publish extracted data to a Pub/Sub topic → Dataflow reads data from Pub/Sub → Dataflow registers Python UDF from Cloud Storage for transformation → Loads processed data into BigQuery for analysis and querying.
