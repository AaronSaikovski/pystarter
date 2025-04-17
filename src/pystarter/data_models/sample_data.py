# from typing import List

# from pydantic import BaseModel, HttpUrl, field_validator

# # ******************************************************************************** #


# # Define the Pydantic model
# class URLItem(BaseModel):
#     """Define the Pydantic model for the URLItem.

#     Args:
#         BaseModel (_type_): _description_

#     Raises:
#         ValueError: _description_

#     Returns:
#         _type_: _description_
#     """

#     website_name: str
#     website_url: HttpUrl
#     output_file: str

#     # Ensure output_file has a .md extension
#     @field_validator("output_file")
#     @classmethod
#     def validate_output_file(cls, value: str) -> str:
#         if not value.endswith(".md"):
#             raise ValueError("output_file must have a .md extension")
#         return value


# # ******************************************************************************** #


# class URLConfig(BaseModel):
#     """Define the Pydantic model for the URLConfig.

#     Args:
#         BaseModel (_type_): _description_
#     """

#     urls: List[URLItem]


# # ******************************************************************************** #
