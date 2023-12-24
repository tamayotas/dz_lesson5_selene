from selene import browser, have, be, by
import os.path


def test_reg_from():
    browser.open('/automation-practice-form')

    browser.element('.pattern-backgound').should(have.exact_text('Practice Form')).click()

    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('ivan@petrov.com')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('9042223322')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(by.text('2000')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(by.text('October')).click()
    browser.element('.react-datepicker__day--001').click()

    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#subjectsInput').type('Chemistry').press_enter()

    browser.element('#uploadPicture').send_keys(os.path.abspath('picture1.jpeg'))

    browser.element('#currentAddress').should(be.blank).type('Moscow, 123')
    browser.element('#react-select-3-input').type('Kaluga').press_enter()
    browser.element('#react-select-4-input').type('Omsk').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table td:nth-child(2)').should(
        have.texts(
            'Ivan Petrov',
            'ivan@petrov.com',
            'Female', '9042223322',
            '01 October,2000',
            'Math',
            'Chemistry',
            'picture1.jpeg',
            'Moscow, 123',
            'Kaluga Omsk'
        )
    )

    browser.element('#closeLargeModal').press_enter()
    # изменения