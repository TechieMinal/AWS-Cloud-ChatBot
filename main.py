# import os
# import lex.create_bot as lex_bot
# import dynamodb.setup_table as dynamodb_setup
# import s3.upload_log as s3_uploader
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# # AWS Configuration
# AWS_REGION = os.getenv('AWS_REGION')
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# # Initialize AWS Services
# def initialize_aws_services():
#     print("Initializing AWS services...")
#     print(f"Region: {AWS_REGION}")
#     print(f"Access Key: {AWS_ACCESS_KEY_ID[:4]}**")  # Hide the full key for security
#     print("Services ready to use.")

# # Link Lex Bot Creation
# def create_lex_bot():
#     print("\nStep 1: Creating Lex bot...")
#     lex_bot.create_bot()  # Calls the create_bot.py script in the lex module
#     print("Lex bot created successfully!")

# # Link DynamoDB Table Setup
# def setup_dynamodb():
#     print("\nStep 2: Setting up DynamoDB table...")
#     dynamodb_setup.setup_table()  # Calls the setup_table.py script in the dynamodb module
#     print("DynamoDB table set up successfully!")

# # Link S3 Log Upload
# def upload_logs_to_s3():
#     print("\nStep 3: Uploading logs to S3...")
#     bucket_name = "chatbot-logs"
#     log_file = "test_log.txt"
#     log_data = "This is a sample log file."
#     s3_uploader.upload_log(bucket_name, log_file, log_data)  # Calls the upload_log.py script in the s3 module
#     print(f"Log file '{log_file}' uploaded to bucket '{bucket_name}' successfully!")

# # Main Workflow
# if _name_ == "_main_":
#     print("Starting Chatbot Integration with AWS...")
#     initialize_aws_services()

#     # Run steps in sequence
#     create_lex_bot()
#     setup_dynamodb()
#     upload_logs_to_s3()

#     print("\nAll steps completed successfully!")import os
# import lex.create_bot as lex_bot
# import dynamodb.setup_table as dynamodb_setup
# import s3.upload_log as s3_uploader
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# # AWS Configuration
# AWS_REGION = os.getenv('AWS_REGION')
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# # Initialize AWS Services
# def initialize_aws_services():
#     try:
#         print("Initializing AWS services...")
#         print(f"Region: {AWS_REGION}")
#         print(f"Access Key: {AWS_ACCESS_KEY_ID[:4]}**")  # Hide the full key for security
#         print("Services ready to use.")
#     except Exception as e:
#         print(f"Error initializing AWS services: {str(e)}")

# # Link Lex Bot Creation
# def create_lex_bot():
#     try:
#         print("\nStep 1: Creating Lex bot...")
#         lex_bot.create_bot()  # Calls the create_bot.py script in the lex module
#         print("Lex bot created successfully!")
#     except Exception as e:
#         print(f"Error creating Lex bot: {str(e)}")

# # Link DynamoDB Table Setup
# def setup_dynamodb():
#     try:
#         print("\nStep 2: Setting up DynamoDB table...")
#         dynamodb_setup.setup_table()  # Calls the setup_table.py script in the dynamodb module
#         print("DynamoDB table set up successfully!")
#     except Exception as e:
#         print(f"Error setting up DynamoDB table: {str(e)}")

# # Link S3 Log Upload
# def upload_logs_to_s3():
#     try:
#         print("\nStep 3: Uploading logs to S3...")
#         bucket_name = "chatbot-logs"
#         log_file = "test_log.txt"
#         log_data = "This is a sample log file."
#         s3_uploader.upload_log(bucket_name, log_file, log_data)  # Calls the upload_log.py script in the s3 module
#         print(f"Log file '{log_file}' uploaded to bucket '{bucket_name}' successfully!")
#     except Exception as e:
#         print(f"Error uploading log to S3: {str(e)}")

# # Main Workflow
# if __name__ == "__main__":
#     try:
#         print("Starting Chatbot Integration with AWS...")
#         initialize_aws_services()

#         # Run steps in sequence
#         create_lex_bot()
#         setup_dynamodb()
#         upload_logs_to_s3()

#         print("\nAll steps completed successfully!")
#     except Exception as e:
#         print(f"Error in main workflow: {str(e)}")
#         print(f"Error setting up DynamoDB
# import os
# import lex.create_bot as lex_bot
# import dynamodb.setup_table as dynamodb_setup
# import s3.upload_log as s3_uploader
# from dotenv import load_dotenv
# import logging

# # Load environment variables from .env
# load_dotenv()

# # AWS Configuration
# AWS_REGION = os.getenv('AWS_REGION')
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# # Initialize logger
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Initialize AWS Services
# def initialize_aws_services():
#     try:
#         logger.info("Initializing AWS services...")
#         logger.info(f"Region: {AWS_REGION}")
#         logger.info(f"Access Key: {AWS_ACCESS_KEY_ID[:4]}**")  # Hide the full key for security
#         logger.info("Services ready to use.")
#     except Exception as e:
#         logger.error(f"Error initializing AWS services: {str(e)}")

# # Link Lex Bot Creation
# def create_lex_bot():
#     try:
#         logger.info("\nStep 1: Creating Lex bot...")
#         lex_bot.create_bot()  # Calls the create_bot.py script in the lex module
#         logger.info("Lex bot created successfully!")
#     except Exception as e:
#         logger.error(f"Error creating Lex bot: {str(e)}")

# # Link DynamoDB Table Setup
# def setup_dynamodb():
#     try:
#         logger.info("\nStep 2: Setting up DynamoDB table...")
#         dynamodb_setup.setup_table()  # Calls the setup_table.py script in the dynamodb module
#         logger.info("DynamoDB table set up successfully!")
#     except Exception as e:
#         logger.error(f"Error setting up DynamoDB table: {str(e)}")

# # Link S3 Log Upload
# def upload_logs_to_s3():
#     try:
#         logger.info("\nStep 3: Uploading logs to S3...")
#         bucket_name = "chatbot-logs"
#         log_file = "test_log.txt"
#         log_data = "This is a sample log file."
#         s3_uploader.upload_log(bucket_name, log_file, log_data)  # Calls the upload_log.py script in the s3 module
#         logger.info(f"Log file '{log_file}' uploaded to bucket '{bucket_name}' successfully!")
#     except Exception as e:
#         logger.error(f"Error uploading log to S3: {str(e)}")

# # Main Workflow
# if __name__ == "__main__":
#     try:
#         logger.info("Starting Chatbot Integration with AWS...")
#         initialize_aws_services()

#         # Run steps in sequence
#         create_lex_bot()
#         setup_dynamodb()
#         upload_logs_to_s3()

#         logger.info("\nAll steps completed successfully!")
#     except Exception as e:
#         logger.error(f"Error in main workflow: {str(e)}") table)
import boto3
import logging

logger = logging.getLogger(__name__)

def create_bot(bot_name: str, intent_name: str) -> None:
    """
    Create a Lex bot.

    Args:
        bot_name (str): The name of the bot to create.
        intent_name (str): The name of the intent to create.

    Returns:
        None
    """
    try:
        if not bot_name or not intent_name:
            raise ValueError("Invalid bot name or intent name")

        lex = boto3.client('lex')
        response = lex.put_bot(
            name=bot_name,
            description='A bot to book hotels',
            intents=[
                {
                    'intentName': intent_name,
                    'intentVersion': '$LATEST'
                }
            ]
            locale='en-US',
            processBehavior='SAVE'
        )
        logger.info("Bot created: %s", response)
    except lex.exceptions.ConflictException:
        logger.error("Bot already exists")
    except lex.exceptions.LimitExceededException:
        logger.error("Limit exceeded, cannot create bot")
    except Exception as e:
        logger.error("Unexpected error: %s", e)