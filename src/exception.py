import sys
from src.logger import logging


def error_messsage_detail(error , error_detail:sys):
  _, _, exc_tb = error_detail.exc_info()

  file_name = exc_tb.tb_frame.f_code.co_filename
  error_message = f'error occured in python script named : {file_name}, in line number : {exc_tb.tb_lineno} and the error message is : {str(error)}'

  return error_message


class CustomException(Exception):
    
    def __init__(self , error_message,error_detail : sys):

      # super() function Initialize the Parent Class: It ensures that the parent class is properly initialized. This is important because the parent class might have its own initialization logic that needs to be executed.

      super().__init__(error_message)
      self.error_message= error_messsage_detail(error_message,error_detail=error_detail)
      # thus whatever error message we will get above it will be automatically inherited over here and the message will be tracked by sys 
    
    def __str__(self):
        # it will print the custom exception
        return self.error_message
    

# now whenever we will use try catch block we can raise this custom error


