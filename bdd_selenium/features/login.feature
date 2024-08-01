Feature: Login Page

  Scenario: Log in with unregistered email
    Given I am on the login page
    When I enter "pyta17@gmail.com" in the email input
    And I enter "12345678" in the password input
    And I click the login button
    Then I should see "No customer account found" message