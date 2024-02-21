# gdg-hack-24-server

1. **Occupation**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | name | String | Primary Key, Max Length: 50 |

2. **Deliverables**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | name | String | Primary Key, Max Length: 50 |

3. **Feedback**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | rating | Integer | Choices: 1 to 5 |
   | comment | Text |  |

4. **Profile**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | email | String | Primary Key, Email Format |
   | password | String | Max Length: 256 |
   | first_name | String | Max Length: 20 |
   | last_name | String | Max Length: 20 |
   | discord_id | String | Unique, Nullable, Max Length: 32 |
   | phone_number | String | Unique, Max Length: 10 |
   | created | DateTime | Auto-set on creation |
   | is_occupied | Boolean | Default: False |

5. **Admin**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | profile | Foreign Key | References Profile, On Delete: Protect |

6. **Event**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | id | String | Primary Key, Max Length: 20 |
   | name | String | Max Length: 20 |
   | start_date_time | DateTime |  |
   | end_date_time | DateTime |  |
   | submissions_deadline | DateTime |  |
   | leader | Foreign Key | References Profile, On Delete: Protect |
   | created | DateTime | Auto-set on creation |

7. **TeamRegistration**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | event | Foreign Key | References Event, On Delete: Protect |
   | name | String | Max Length: 20 |
   | number_of_team | Integer | Positive Small Integer, Default: 0 |

8. **ParticipantRegistration**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | motivation_letter | Text |  |
   | profile | Foreign Key | References Profile, On Delete: Protect |
   | team | Foreign Key | References TeamRegistration, On Delete: Protect |
   | occupation | Foreign Key | References Occupation, On Delete: Protect |

9. **Challenges**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | event | Foreign Key | References Event, On Delete: Protect |
   | name | String | Max Length: 20 |
   | description | Text |  |
   | number_of_outputs | Integer | Positive Small Integer |

10. **Agenda**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | event | Foreign Key | References Event, On Delete: Protect |
   | date_time | DateTime |  |
   | activity | String | Max Length: 20 |

11. **Mentor**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | profile | Foreign Key | References Profile, On Delete: Protect |
   | event | Foreign Key | References Event, On Delete: Protect |
   | occupation | Foreign Key | References Occupation, On Delete: Protect |

12. **Participant**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | profile | Foreign Key | References Profile, On Delete: Cascade |
   | event | Foreign Key | References Event, On Delete: Cascade |
   | occupation | Foreign Key | References Occupation, On Delete: Cascade |
   | team_name | String | Nullable, Max Length: 50 |
   | joined | DateTime | Auto-set on join |

13. **Submission**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | id | String | Primary Key, Max Length: 20 |
   | team | Foreign Key | References Team, On Delete: Cascade |
   | event | Foreign Key | References Event, On Delete: Cascade |

14. **Submission_Output**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | id | String | Primary Key, Max Length: 20 |
   | submission | Foreign Key | References Submission, On Delete: Cascade |
   | output | Foreign Key | References Output, On Delete: Cascade |

15. **Judge**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | profile | Foreign Key | References Profile, On Delete: Cascade |
   | event | Foreign Key | References Event, On Delete: Cascade |

16. **JudgeEventFeedback**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | event_Feedback | Foreign Key | References Event, On Delete: Protect |
   | feedback | Foreign Key | References Feedback, On Delete: Protect |
   | judge | Foreign Key | References Judge, On Delete: Protect |

17. **Team**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | event | Foreign Key | References Event, On Delete: Protect |
   | name | String | Max Length: 20 |

18. **ParticipantMentorFeedback**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | mentor | Foreign Key | References Mentor, On Delete: Protect |
   | participant | Foreign Key | References Participant, On Delete: Protect |
   | feedback | Foreign Key | References Feedback, On Delete: Protect |

19. **ParticipantEventFeedback**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | event_Feedback | Foreign Key | References Event, On Delete: Protect |
   | Feedback | Foreign Key | References Feedback, On Delete: Protect |

20. **RequestMentor**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | team | Foreign Key | References Team, On Delete: Protect |
   | mentor | Foreign Key | References Mentor, On Delete: Protect |
   | requested | DateTime | Auto Now Add: True |

23. **WebsiteSession**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | event | One to One | References Event, On Delete: Protect, Primary Key: True |
   | grant_to_judge | Boolean | Default: False |
   | grant_to_participants | Boolean | Default: False |

22. **Outputs**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | coefficient | Integer | Positive Small Integer, Default: 1 |
   | event | Foreign Key | References Event, On Delete: Protect |
   | output | Foreign Key | References Deliverables, On Delete: Protect |
   | challenges | Foreign Key | References Challenges, On Delete: Protect |
   | processed_by | Foreign Key | References Occupation, On Delete: Protect |

23. **OutputResult**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | team | Foreign Key | References Team, On Delete: Protect |
   | output | Foreign Key | References Outputs, On Delete: Protect |
   | rate | Integer | Positive Small Integer |
   | comment | Text |  |

24. **TotalResult**
   | Field Name | Data Type | Constraints |
   | --- | --- | --- |
   | team | One to One | References Team, On Delete: Protect, Primary Key: True |
   | rate | Integer | Positive Small Integer |

25. **Winner**
    | Field Name | Data Type | Constraints |
    | --- | --- | --- |
    | team | One to One | References Team, On Delete: Protect, Primary Key: True |
