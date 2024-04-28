# Created by leoh2 at 4/3/2024
Feature: Target sign in test
  # Enter feature description here

  Scenario: Logged out user can navigate to Sign In
    Given Open Target page
    When Click on sign in
    When From right side navigation menu, click on sign in
    Then Verify sign in form opened

  Scenario: User can open and close Terms and Conditions from sign in page
   Given Open sign in page
   When Store original window
   And Click on Target terms and conditions link
   And Switch to the newly opened window
   Then Verify Terms and Conditions page is opened
   And User can close new window and switch back to original
