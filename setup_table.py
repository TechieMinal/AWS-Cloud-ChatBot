# import boto3

# def setup_table():
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.create_table(
#         TableName='ChatbotUserData',
#         KeySchema=[
#             {'AttributeName': 'UserId', 'KeyType': 'HASH'}
#         ],
#         AttributeDefinitions=[
#             {'AttributeName': 'UserId', 'AttributeType': 'S'}
#         ],
#         ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
#     )
#     print("DynamoDB Table created:", table.table_status)
#     import boto3

# def setup_table():
#     dynamodb = boto3.resource('dynamodb')
#     try:
#         table = dynamodb.create_table(
#             TableName='ChatbotUserData',
#             KeySchema=[
#                 {'AttributeName': 'UserId', 'KeyType': 'HASH'}
#             ],
#             AttributeDefinitions=[
#                 {'AttributeName': 'UserId', 'AttributeType': 'S'}
#             ],
#             ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
#         )
#         print("DynamoDB Table created:", table.table_status)
#     except dynamodb.meta.client.exceptions.ResourceInUseException:
#         print("Table already exists")
#     except dynamodb.meta.client.exceptions.LimitExceededException:
#         print("Limit exceeded, cannot create table")
#     except Exception as e:
#         print("An error occurred:", str(e))

import boto3
import logging

logger = logging.getLogger(__name__)

def setup_table(table_name: str, read_capacity_units: int = 1, write_capacity_units: int = 1) -> None:
    """
    Create a DynamoDB table.

    Args:
        table_name (str): The name of the table to create.
        read_capacity_units (int): The number of read capacity units to provision. Defaults to 1.
        write_capacity_units (int): The number of write capacity units to provision. Defaults to 1.

    Returns:
        None
    """
    try:
        if not table_name:
            raise ValueError("Invalid table name")

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'UserId', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'UserId', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': read_capacity_units,
                'WriteCapacityUnits': write_capacity_units
            }
        )
        logger.info("Table created: %s", table.table_status)
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        logger.error("Table already exists")
    except dynamodb.meta.client.exceptions.LimitExceededException:
        logger.error("Limit exceeded, cannot create table")
    except Exception as e:
        logger.error("Unexpected error: %s", e)