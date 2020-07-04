from user import user_profile
from user import user_profile_setname
from user import user_profile_setemail
from user import user_profile_sethandle
from auth import auth_register, auth_login
from error import InputError
import pytest

""" 
Test for a valid user
Assume that login and register works 
Assume that register also logs in
"""
def test_valid_profile():
    # Valid user tests: 
    # User 1:
    user1 = auth_register('cs1531@cse.unsw.edu.au', 
    'haydEn123', 'Hayden', 'Smith')
    u_id = user1['u_id']
    token = user1['token']
    assert user_profile(token, u_id) == {
        'user': {
        	'u_id': 1,
        	'email': 'cs1531@cse.unsw.edu.au',
        	'name_first': 'Hayden',
        	'name_last': 'Jacobs',
        	'handle_str': 'hjacobs',
        },
    }
    """
    Below are users who don't exist in user.py user_profile return 
    """
    """
    # User 2:
    user2 = auth_register('abdullah1@cse.unsw.edu.au', 
    'Abdullah1', 'Abdullah', 'Ahmed')
    u_id = user2['u_id']
    token = user2['token']
    assert user_profile(token, u_id) == {
        'user': {
            'u_id': 1,
            'email': 'abdullah1@cse.unsw.edu.au',
        	'name_first': 'Abdullah',
        	'name_last': 'Ahmed',
        	'handle_str': 'abdullahahmed',
        },
    }
    # User 3:
    user3 = auth_register('z526272@cse.unsw.edu.au', 
    'Aa527382', 'David', 'Smiths')
    u_id = user3['u_id']
    token = user3['token']
    assert user_profile(token, u_id) == {
        'user': {
            'u_id': 1,
            'email': 'z526272@cse.unsw.edu.au',
        	'name_first': 'David',
        	'name_last': 'Smiths',
        	'handle_str': 'davidsmiths',
        },
    }
    # User 4: 
    user4 = auth_register('UTSkid@cse.unsw.edu.au', 
    'sriVathsan123', 'Srivathsan', 'Ravichandran')
    u_id = user4['u_id']
    token = user4['token']
    assert user_profile(token, u_id) == {
        'user': {
            'u_id': 1,
            'email': 'UTSkid@cse.unsw.edu.au',
        	'name_first': 'Srivathsan',
        	'name_last': 'Ravichandran',
        	'handle_str': 'srivathsanravichandr',
        },
    }
"""
# Invalid user tests: 
def test_invalid_profile():
    # Invalid u_ids:
    user1 = auth_register('cs1531@cse.unsw.edu.au', 
    'haydEn123', 'Hayden', 'Smith')
    u_id = user1['u_id']
    token = user1['token']

    with pytest.raises(InputError) as e:
        user_profile(token, u_id+3)

    with pytest.raises(InputError) as e:
        user_profile(token, u_id+10)

    with pytest.raises(InputError) as e:
        user_profile(token, u_id-1)

    # Invalid tokens
    with pytest.raises(InputError) as e:
        user_profile('invalid', u_id)

    with pytest.raises(InputError) as e:
        user_profile('123456', u_id)

    with pytest.raises(InputError) as e:
        user_profile('token1', u_id)

def test_valid_profile_setname():
    # Test for some valid names
    # User 1:
    user1 = auth_register('cs1531@cse.unsw.edu.au', 
    'haydEn123', 'Hayden', 'Smith') 
    token = user1['token']
    assert user_profile_setname(token, 'Hayden', 
    'Jacobs') == {}

    # User 2: 
    user2 = auth_register('abdullah1@cse.unsw.edu.au', 
    'Abdullah1', 'Abdul', 'Ahmed')
    token = user2['token']
    assert user_profile_setname(token, 'Abdullah',
    'Mukhtar Ahmed') == {}

    # User 3: 
    user3 = auth_register('imValidPls@cse.unsw.edu.au', 
    'Invalid1', 'Invalid'*50, 'Dude') 
    token = user3['token']
    assert user_profile_setname(token, 'Valid', 
    'Dude') == {}

    # User 4: 
    user4 = auth_register('profJoeWolfe@phys.unsw.edu.au', 
    'JoePhysics1', 'Joe', 'Wolfe') 
    token = user4['token']
    assert user_profile_setname(token, 'JOE', 
    'WOOF') == {}    

def test_invalid_profile_setname():
    # InputError tests: 
    # User 1: 
    user1 = auth_register('cs1531@cse.unsw.edu.au', 
    'haydEn123', 'Hayden', 'Smith')
    token = user1['token']
    with pytest.raises(InputError) as e:
        user_profile_setname(token, '', 
        'LastNameOnly')
    # User 2: 
    user2 = auth_register('abdullah1@cse.unsw.edu.au', 
    'Abdullah1', 'Abdul', 'Ahmed')
    token = user2['token']
    with pytest.raises(InputError) as e:
        user_profile_setname(token, 
        'Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas \
        Uvuvwevwevwe Uvuvwevwevwe Onyetenyevwe \
        Ugwemuhwem OsasOnyetenyevwe Ugwemuhwem Osas', 
        'Osas')
    # User 3: 
    user3 = auth_register('z420420@cse.unsw.edu.au', 
    'passw000rD', 'Jeff', 'Mynameis')    
    token = user3['token']
    with pytest.raises(InputError) as e:
        user_profile_setname(token,'John', 
        'pneumonoultramicroscopicsilicovolcanoconiosispneu \
        monoultramicroscopicsilicovolcanoconiosispneumonou \
        ltramicroscopicsilicovolcanoconiosis')
    # User 4: 
    user4 = auth_register('HELLO!!@cse.unsw.edu.au', 
    'HiHiHi', 'Sometimes', 'Itdobelikethat')
    token = user4['token']
    with pytest.raises(InputError) as e:
        user_profile_setname(token, 'ImagineHaving \
        aLastName', '')

def test_valid_profile_setemail():
    # A few valid emails:
    # user1 : 
    user1 = auth_register('cs1531@cse.unsw.edu.au', 
    'haydEn123', 'Hayden', 'Smith')
    token = user1['token']
    assert user_profile_setemail(token,
    'cs1531@cse.unsw.edu.au') == {}

    # user2 : 
    user2 = auth_register('randomgmail@codecamp.org', 
    'haydEn123', 'Hayden', 'Smith')
    token = user2['token']
    assert user_profile_setemail(token, 
    'randomgmail@codecamp.org') == {}   

    # user3 : 
    user3 = auth_register('abdullah527382@gmail.com', 
    'passw0rD', 'Abdul', 'Ahmed')
    token = user3['token']
    assert user_profile_setemail(token, 
    'abdullah527382@gmail.com') == {}

    # user4 :
    user4 = auth_register('timeforthai@hotmail.com', 
    'Timeforth4i', 'Mathews', 'Foodcourt')
    token = user4['token']
    assert user_profile_setemail(token, 
    'timeforthai@hotmail.com') == {}

def test_invalid_profile_setemail():
    # Register some valid users with valid emails: 
    # Then check invalid

    user1 = auth_register('myValidEmail123@cse.unsw.edu.au', 
    'Em4il123', 'Emailia', 'Compose')
    token = user1['token']

    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'Thisisntanemail.com')
    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'USYD.unsw@.edu.au') 
    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'UNeverSleepWell.com')

    user2 = auth_register('abdullah527382@.edu.unsw.com', 
    'Abdullah1', 'Abdul', 'Ahmed')
    token = user2['token']

    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'ThisisntanemailYouGenius.com')
    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'microsoft.com')
    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'myValidEmail123@cse.unsw.edu.au')
    
    user3 = auth_register('memelord420@.edu.unsw.com', 
    'Jeffrey', 'Mynameis', 'Mypassword')
    token = user3['token']

    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'ThisisntanemailYouGenius.com')
    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'myValidEmail123@cse.unsw.edu.au')
    with pytest.raises(InputError) as e:
        user_profile_setemail(token, 
        'abdullah527382@.edu.unsw.com')


def test_valid_profile_sethandle():

    # Valid profile handles: 
    user1 = auth_register('cs1531@cse.unsw.edu.au', 
    'haydEn123', 'Hayden', 'Smith')
    token = user1['token']

    assert user_profile_sethandle(token, 
    'haydensmith') == {}

    user2 = auth_register('abdullah527382@gmail.com', 
    'passw0rD', 'Abdul', 'Ahmed')   
    token = user2['token']

    assert user_profile_sethandle(token, 
    'abdulahmed') == {}

    user3 = auth_register('memelord420@.edu.unsw.com', 
    'Jeffrey', 'Mynameis', 'Mypassword')  
    token = user3['token']  

    assert user_profile_sethandle(token, 
    'jeffreymynameis') == {}
    
    user4 = auth_register('timeforthai@hotmail.com', 
    'Timeforth4i', 'Mathews', 'Foodcourt')
    token = user4['token']

    assert user_profile_sethandle(token, 
    'mathewsfoodcourt') == {}

def test_invalid_profile_sethandle():

    # Invalid profile handles:  
    user1 = auth_register('abdullah.ahmed2@cse.unsw.edu.au', 
    'abdullah1A', 'Abdullah', 'Ahmed')
    token = user1['token']

    # More than 20 characters 
    with pytest.raises(InputError) as e:
        user_profile_sethandle(token, 
        'In this house we obey the law of thermodynamics')

    # Less than 3 characters
    with pytest.raises(InputError) as e:
        user_profile_sethandle(token, 'hi')

    # 0 characters
    with pytest.raises(InputError) as e:
        user_profile_sethandle(token, '')

    # Handle already used by another user: 
    user2 = auth_register('cs1531@cse.unsw.edu.au', 
    'haydEn123', 'Hayden', 'Smith') 
    token = user2['token']

    with pytest.raises(InputError) as e:
        user_profile_sethandle(token, 'abdullahahmed')   

        

