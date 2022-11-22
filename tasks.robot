*** Settings ***
Documentation       Template robot main suite.

Library             Collections
Library             MyLibrary
Library             myFunction.py
Resource            keywords.robot
Variables           variables.py


*** Tasks ***
Example task
    ${process_id}    Get Process Id
    ${process_list}    List All Process Ids
    Log    ${process_id}
    Example Keyword
    Example Python Keyword
    Log    ${TODAY}
