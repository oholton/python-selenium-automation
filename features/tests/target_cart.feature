# Created by leoh2 at 4/3/2024
Feature: Cart test
  # Enter feature description here

  Scenario: User can see empty cart
    Given Open Target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown


    # Enter steps here