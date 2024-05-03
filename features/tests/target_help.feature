# Created by leoh2 at 4/30/2024
Feature: Tests for Help pages

  Scenario: User can select Help topic Gift Cards
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select help topic Gift Cards
    Then Verify help Gift Cards page opened