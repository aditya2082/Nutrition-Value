# Foodee

Foodee is a health assistance application designed to provide detailed nutritional information about various foods. This project includes a robust backend built with Django and a single-page application (SPA) frontend for seamless user interaction. Users can search for different foods to get their nutritional values and insights on how much physical activity is required to burn off certain nutrients.

![Foodee](https://github.com/aditya2082/Nutrition-Value/blob/main/Foodee.png)

## Features

- **Food Search**: Search for calories and nutritional values in different foods.
- **Nutritional Information**: Detailed nutritional values per 100 grams of food.
- **Physical Activity Recommendations**: Suggestions on physical activities needed to burn off consumed calories.
- **Premium Features**: Exclusive nutritional information available for premium users.

## Technology Stack

- **Backend**: Django
- **Frontend**: Single Page Application (SPA) framework
- **Database**: SQLite (development), PostgreSQL (production)

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/aditya2082/Nutrition-Value.git
    cd Nutrition-Value
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Run the Django server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

1. Open your browser and navigate to `http://localhost:8000` for the Application.
2. Search for your desired food items to see their nutritional values and physical activity recommendations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
