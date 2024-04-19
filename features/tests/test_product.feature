# Created by leoh2 at 4/17/2024
Feature: Product color test


  Scenario: User can select product of different color
    Given Open product page
    When Click on each color of product
    Then Verify expected colors are selectable