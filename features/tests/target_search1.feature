# Created by leoh2 at 3/30/2024
Feature: Search tests

  Scenario: User can search for a product
    Given Open Target main page
    When Search for coffee
    Then Verify search results are for coffee
