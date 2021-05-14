import pytest
import logging as logger
from api_testing.src.utilities.genericUtilities import generate_random_email_and_password
from api_testing.src.helpers.customers_helper import CustomerHelper
from api_testing.src.dao.customers_dao import CustomerDAO



@pytest.mark.tcid1
def test_create_customer_only_email_password():
    logger.info('TEST: Create new customer with email and password only.')

    rand_info = generate_random_email_and_password()

    email = rand_info['email']
    password = rand_info['password']
    import pdb; pdb.set_trace()

    # create payload

    payload = {'email':email, 'password':password}

    # make the call
    custom_object = CustomerHelper()
    cust_api_info = custom_object.create_customer(email=email, password=password)


    assert cust_api_info['email'] == email
    assert cust_api_info['meta_data'] == []



    cust_dao = CustomerDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    import pdb; pdb.set_trace()




    # verify status code of the call

    # verify email in the response

    # verify customer is created in database