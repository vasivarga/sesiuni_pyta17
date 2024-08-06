Feature: Register

  Background: Open register page
    Given I am on the register page

  Scenario: Validate mandatory fields
    When I click Register button
    Then "First name is required." error text is displayed for first name field
    And "Last name is required." error text is displayed for last name field
    And "Email is required." error text is displayed for email field
    And "Password is required." error text is displayed for password field

  @passcheck
  Scenario: Validate password min length
    When I set "Python" as first name
    And I set "Automation" as last name
    And I select "10" "August" "1996" as birth date
    And I set "pyta17@gmail.com" as email
    And I set "12345" as password
    And I set "12345" as password confirm
    And I click Register button
    Then I should see "Password must meet the following rules:" and "must have at least 6 characters and not greater than 64 characters" in the password error message


  # Tema: validati ca parolele coincid
  # Tema: test care face register complet si verifica mesajul de succes de la final

