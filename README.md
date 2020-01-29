**Human resources management system**

The goal of this project is to develop a human resource management system
 for models and actors

**Stack:**
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Docker-compose

**Current status:**
- [X] Authorization
- [X] Token authentication
- [X] Data Models
- [ ] Booker dashboard
- [ ] Manager dashboard

Available endpoints

|       Endpoint         |  Description|
| ----------------       | ------- |
| auth/                  |Standart Djoser endpoint|
| booker_profile/        |Authenticated booker personal page|
| booker_list/           | Show all actors for authenticated booker|
| dashboard/             | Show all agencies|
| dashboard/agency/\<pk>/  | Edit agency profiles |
| dashboard/agency/\<pk>/bookers/  | List all bookers or create new one for selected agency|
| dashboard/agency/\<pk>/bookers/<booker_id>   | Edit selected booker profile|