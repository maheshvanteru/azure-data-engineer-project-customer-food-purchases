# azure-data-engineer-project-customer-food-purchases

## Beginner Data Engineering Project 
## Description

A food chain service consolidates the customer purchases data at the end of the each day, a JSON formatted file will be added into S3 bucket.  

This project gives a real-time understanding of how data is ingested into Azure SQL from S3 bucket using ADLS Gen2, ADF, Key Vault, Azure Functions, Pipelines, Storage Trigger.  


## Prereq

1. [Azure account] (https://azure.microsoft.com/) to setup azure services
2. [AWS account](https://aws.amazon.com/) to set up S3 Bucket component

By the end of the setup you should have(or know how to use)

1. `S3` Bucket
2. `AZURE SQL` Configuring a new database and accessing it.
3. `AZURE DATA FACTORY` Creating pipelines to perform actions.  
4. `AZURE DATA LAKE STORAGE GEN2` Configuring Storage account with region and redundancy
5. `AZURE FUNCTION` Creating an Azure function, using it as Storgae Trigger
6. `AZURE KEY VAULT` Configure a Key Vault with region, and access policies

## Design

![Engineering Design](assets/images/eng_spec.jpg)

## Data
