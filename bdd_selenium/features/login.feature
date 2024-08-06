Feature: Login Page

  Background: Open login page
    Given I am on the login page

  @regression @smoke
  Scenario: Log in with unregistered email
    When I enter "pyta17@gmail.com" in the email input
    And I enter "12345678" in the password input
    And I click the login button
    Then I should see "No customer account found" message

  @sanity @regression
  Scenario: Check that the URL of the Login Page is correct
    Then The URL of the page is "https://demo.nopcommerce.com/login"

  # Tema: Implementati un test similar cu cel de check URL pentru a verifica titlul paginii
  # Hint: Se va declara o functie in base page care va putea fi apelata din orice pagina


  @regression
  Scenario Outline: Log in with unregistered email
    When I enter "<email>" in the email input
    And I enter "<password>" in the password input
    And I click the login button
    Then I should see "No customer account found" message
    Examples:
      | email            | password    |
      | pyta17@gmail.com | 12345678    |
      | pyta17@yahoo.com | asdsafsadfs |
      | 17@dfdjffsd.com  | dsfsdfdsfds |
      | pyta17@bing.com  | blablabla   |
