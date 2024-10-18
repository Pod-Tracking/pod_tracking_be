# Pod Tracking

![Now this is podracing](https://i.makeagif.com/media/6-21-2014/ozc7Hm.gif)

***"Now THIS is Pod Tracking"***

## Introduction
Welcome to the initial repository of Pod Tracking! Pod Tracking is an application that allows Magic The Gathering players to track their group's game history, game and player statistics, and eventually, deck statistics. This repository houses the codebase for our backend services, crafted using Python and the Django REST framework.

---
## Table of Contents
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Directory](#directory)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [RESTful Endpoints](#restful-endpoints)
  - [Players](#players)
  - [Pods](#pods)
  - [Decks](#decks)
  - [Commanders](#commanders)
- [Dev Team](#dev-team)
- [Legal Disclaimer](#disclaimer)
---

## Directory
[Hosted Website]()

[Hosted Server]()

## Tech Stack
<a href="https://www.python.org/" target="_blank"><img style="margin: 15px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" height="50" /></a>
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 15px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django" height="50" /></a>

- **Python:** Our primary programming language offering simplicity and versatility
- **Django REST Framework:** Used for building API's, ensuring a scalable and secure connection between our frontend and backend services.

## Key Features 
1. **Feature 1:** 
2. **Data Management:** Employs Django ORM for seamless database queries and data manipulation.
3. **Feature 3:** 
---
## Getting Started
1. **Clone the Repository:** Get started with Pod Tracking Backend by cloning the repository to your local machine.
2. **Install Requirements:** Navigate into the cloned repository and install necessary dependencies
3. **Start the Server:** Start the Django server.
Note: Please ensure you have Python and pip installed on your machine before running these commands.

## RESTful Endpoints
Base url to reach the endpoints listed below:
```
http://127.0.0.1:8000/api/v1/
```

### Players
```
GET players/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
[ 
  {
    "id": 1,
    "name": "Timmy",
    "photo": null,
    "email": "timtim@gmail.com",
    "password": "password"
  },
  {
    "id": 2,
    "name": "Spike",
    "photo": null,
    "email": "spikeplays@gmail.com",
    "password": "password"
  }
]
```
</details>

---

```
POST players/
```
<details>
<summary> Endpoint Details </summary>

Request:
```json
{
  "name": "Jenny",
  "photo": null,
  "email": "wombo_combo@gmail.com",
  "password": "password"
}
```

| Code | Description |
| :--- | :--- |
| 201 | 'CREATED' |

Response:
```json
{
  "id": 3,
  "name": "Jenny",
  "photo": null,
  "email": "wombo_combo@gmail.com",
  "password": "password"
}
```
</details>

---

```
GET players/:player_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
{
  "id": 1,
  "name": "Timmy",
  "photo": null,
  "email": "timtim@gmail.com",
  "password": "password"
}
```
</details>

---

```
PUT players/:player_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```json
{
  "name": "Johnny"
}
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
{
  "id": 3,
  "name": "Johnny",
  "photo": null,
  "email": "wombo-combo@gmail.com",
  "password": "password"
}
```
</details>

---

```
DELETE players/:player_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 204 | 'NO CONTENT' |

</details>

---

### Pods


---

### Decks
```
GET players/:player_id/decks/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
[
  {
    "id": 1,
    "name": "Hungry Hydras",
    "player": 2,
    "colors": "Green",
    "wins": 0,
    "losses": 0
  },
  {
    "id": 3,
    "name": "Gunpingers",
    "player": 2,
    "colors": "Blue, Red",
    "wins": 0,
    "losses": 0
  }
]
```
</details>

```
POST players/:player_id/decks/
```
<details>
<summary> Endpoint Details </summary>

Request:
```json
{
  "name": "Ur-Dragon's Brood",
  "player": 2,
  "colors": "Green, White, Black, Blue, Red"
}
```

| Code | Description |
| :--- | :--- |
| 201 | 'CREATED' |

Response:
```json
{
  "id": 4,
  "name": "Ur-Dragon's Brood",
  "player": 2,
  "colors": "Green, White, Black, Blue, Red",
  "wins": 0,
  "losses": 0,
  "created_date": "2024-02-27T20:54:42.567663Z",
  "updated_date": "2024-02-27T20:54:42.572354Z"
}
```
</details>

```
GET players/:player_id/decks/:deck_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
[
  {
    "id": 2,
    "name": "Hungry Hydras",
    "player": 2,
    "colors": "Green",
    "wins": 0,
    "losses": 0,
    "created_date": "2024-02-27T20:54:42.567663Z",
    "updated_date": "2024-02-27T20:54:42.572354Z"
  },
  {
    "id": 3,
    "name": "Gunpingers",
    "player": 2,
    "colors": "Blue, Red",
    "wins": 0,
    "losses": 0,
    "created_date": "2024-02-27T20:54:42.567663Z",
    "updated_date": "2024-02-27T20:54:42.572354Z"
  }
]
```
</details>

```
PUT players/:player_id/decks/:deck_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```json
{
  "wins": 1,
  "losses": 0,
}
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
{
  "id": 2,
  "name": "Hungry Hydras",
  "player": 2,
  "colors": "Green",
  "wins": 1,
  "losses": 0,
  "created_date": "2024-02-27T20:54:42.567663Z",
  "updated_date": "2024-02-27T20:54:42.572354Z"
}
```
</details>

```
DELETE players/:player_id/decks/:deck_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 204 | 'NO CONTENT' |

</details>

---

### Commanders
```
GET decks/:deck_id/commanders/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
[
  {
    "id": 1,
    "name": "Gragos, Vicious Watcher",
    "colors": "Green",
    "img": "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=466926&type=card"
  }
]
```
</details>

```
POST decks/:deck_id/commanders/
```
<details>
<summary> Endpoint Details </summary>

Request:
```json
{
  "name": "Gragos, Vicious Watcher",
  "colors": "Green",
  "img": "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=466926&type=card"
}
```

| Code | Description |
| :--- | :--- |
| 201 | 'CREATED' |

Response:
```json
{
  "id": 1,
  "name": "Gragos, Vicious Watcher",
  "colors": "Green",
  "img": "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=466926&type=card"
}
```
</details>

```
GET decks/:deck_id/commanders/:commander_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
{
  "id": 1,
  "name": "Gragos, Vicious Watcher",
  "colors": "Green",
  "img": "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=466926&type=card"
}
```
</details>

```
PUT decks/:deck_id/commanders/:commander_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```json
{
  "name": "Zaxara, the Exemplary",
  "colors": "Black, Green, Blue",
  "img": "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=484727&type=card"
}
```

| Code | Description |
| :--- | :--- |
| 200 | 'OK' |

Response:
```json
{
  "id": 1,
  "name": "Zaxara, the Exemplary",
  "colors": "Black, Green, Blue",
  "img": "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=484727&type=card"
}
```
</details>

```
DELETE decks/:deck_id/commanders/:commander_id/
```
<details>
<summary> Endpoint Details </summary>

Request:
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 204 | 'NO CONTENT' |

</details>

---

## Dev Team

<table>
  <tr>
    <th>Ethan Van Gorkom</th>
  </tr>

<tr>
  <td><img src="https://avatars.githubusercontent.com/u/132889569?v=4" width="135" height="135"></td>
</tr>


  <tr>
    <td>
      <a href="https://github.com/EVanGorkom" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/evangorkom/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
  </tr>
</table>

## Disclaimer

**Legal Disclaimer: Use of MTG Cards in Application**

This application utilizes Magic: The Gathering (MTG) cards as part of its core functions. By using this application, you acknowledge and agree to the following:

1. **Ownership and Rights:** MTG cards, including their names, images, and associated content, are owned and copyrighted by Wizards of the Coast LLC ("Wizards"). This application is not affiliated with or endorsed by Wizards, and the use of MTG cards within this application does not imply any official association with Wizards.

2. **Fair Use:** The use of MTG cards within this application is intended for informational and entertainment purposes only. This application is designed to provide users with tools and resources related to MTG gameplay, strategy, and community engagement. Any references to MTG cards are made under the principles of fair use, and no infringement of Wizards' intellectual property rights is intended.

3. **Accuracy and Reliability:** While every effort has been made to ensure the accuracy and reliability of the information provided within this application, including MTG card data, we cannot guarantee its completeness or correctness. Users should independently verify any information obtained from this application before making decisions based on it.

4. **No Endorsement:** The inclusion of MTG cards within this application does not constitute an endorsement or recommendation of any specific cards, strategies, products, or services by Wizards or any other party. Users are encouraged to use their own judgment and discretion when utilizing MTG card information provided by this application.

5. **Limitation of Liability:** In no event shall the developers, creators, or distributors of this application be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) arising in any way out of the use of this application, even if advised of the possibility of such damage.

6. **Modification and Termination:** We reserve the right to modify, suspend, or terminate this application or any part thereof at any time without prior notice. This includes, but is not limited to, the availability of MTG card data and features within the application.

By using this application, you agree to abide by the terms and conditions outlined in this disclaimer. If you do not agree with these terms, you should refrain from using this application.