from selene import browser, have, be, by
import os.path


def test_reg_form():
    browser.open('/automation-practice-form')
    browser.element('.pattern-backgound').should(have.exact_text('Practice Form')).click()

    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('ivan@petrov.com')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('9042223322')

    browser.element('#dateOfBirthInput').click()
    browser.element('option:nth-child(7)').click()
    browser.element('option:nth-child(94)').click()
    browser.element('div.react-datepicker__day--018').click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#currentAddress').type('Moscow, 123')
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Merrut').press_enter()

    browser.element('#uploadPicture').send_keys(os.path.abspath('picture1.jpeg'))
    browser.element('#submit').press_enter()


    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table td:nth-child(2)').should(
        have.texts(
            'Ivan Petrov',
            'ivan@petrov.com',
            'Female', '9042223322',
            '01 October,2000',
            'Math',
            'Reading',
            'picture1.jpeg',
            'Moscow, 123',
            'Uttar Pradesh Merrut'
        )
    )

    browser.element('#closeLargeModal').press_enter()
