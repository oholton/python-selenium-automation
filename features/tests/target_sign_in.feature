# Created by leoh2 at 4/3/2024
Feature: Target sign in test
  # Enter feature description here

  Scenario: Logged out user can navigate to Sign In
    Given Open Target page
    When Click on sign in
    When From right side navigation menu, click on sign in
    Then Verify sign in form opened
