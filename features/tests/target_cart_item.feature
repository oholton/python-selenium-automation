# Created by leoh2 at 4/9/2024
Feature: Cart Item Test
  # Enter feature description here

  Scenario: User can see item in cart
    Given Open the main page
    When Search for cake in search field
    Then Add product into cart
    Then Proceed to cart
    Then Verify item in cart