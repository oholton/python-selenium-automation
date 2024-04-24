# Created by leoh2 at 4/3/2024
Feature: Cart test
  # Enter feature description here

  Scenario: User can see empty cart
    Given Open Target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: User can see item in cart
    Given Open the main page
    When Search for cake in search field
    Then Add product into cart
    Then Proceed to cart
    Then Verify item in cart


    # Enter steps here