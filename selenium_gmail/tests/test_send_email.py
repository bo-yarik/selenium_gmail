# -*- coding: utf-8 -*-
import pytest
from snippets.users import *
from snippets.tools import *


@pytest.allure.story("Checking the sending, receiving and responding to a letter")
def test_send_email():
    with pytest.allure.step('SetUp users logins and passwords'):
        first_user_params = {'name': 'Test_user1 Test', 'login': 'testuserforwisebits1@gmail.com', 'password': 'WiseBits1'}
        second_user_params = {'name': 'Test_user2 Test', 'login': 'testuserforwisebits2@gmail.com', 'password': 'WiseBits2'}
        letter = {'subject': 'Hello!', 'message': 'How are you?', 'answer': 'Im fine thanks'}

    with pytest.allure.step('Create 2 users and log into their mail and delete previous letters if exist'):
        first_user = create_new_user(first_user_params, browser='Chrome')
        second_user = create_new_user(second_user_params, browser='Chrome')
        first_user.mail.delete_all_letters()
        second_user.mail.delete_all_letters()

    with pytest.allure.step('The first user creates a new message and send it to the second user'):
        first_user.mail.new_letter()
        first_user.mail.fill_recipients(second_user_params['login'])
        first_user.mail.fill_subject(letter['subject'])
        first_user.mail.fill_message(letter['message'])
        first_user.mail.send_letter()

    with pytest.allure.step('Verify that the email was sent'):
        waiting_for(first_user.wd, 'class_name', 'vh')

    with pytest.allure.step('The second user receives a letter and checks it'):
        second_user.mail.open_letter(first_user_params['name'])

        subject = second_user.mail.get_text('.hP')
        assert letter['subject'] == subject

        message = second_user.mail.get_text('.ii.gt ')
        assert letter['message'] == message

    with pytest.allure.step('The second user responds to the letter'):
        second_user.mail.answer_letter(letter['answer'])
        second_user.mail.send_letter()

    with pytest.allure.step('The first user receives a letter and checks it'):
        first_user.mail.receive_letter()

        subject = first_user.mail.get_text('.hP')
        assert letter['subject'] == subject

        answer = first_user.mail.get_text('.ii.gt ')
        assert letter['answer'] in answer.split('/n')[0]


