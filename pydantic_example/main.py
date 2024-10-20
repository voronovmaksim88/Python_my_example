from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import List
from datetime import date


#  poetry add pydantic@^2.0.0
#  poetry add pydantic[email]

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)
    is_active: bool = True
    tags: List[str] = []
    birth_date: date


# Создание экземпляра модели
try:
    user = User(
        id=1,
        name="John Doe",
        email="john@example.com",
        age=30,
        tags=["python", "developer"],
        birth_date=date(1992, 5, 15)  # Прямое использование объекта date
    )
    print("User object:", user)
    print("User data as dictionary:", user.model_dump())  # Используем model_dump() вместо dict()

    # Пример использования model_dump() с дополнительными параметрами
    print("User data (exclude unset):", user.model_dump(exclude_unset=True))
    print("User data (include only name and email):", user.model_dump(include={"name", "email"}))
except ValidationError as e:
    print(f"Ошибка валидации: {e}")

# Попытка создать невалидный экземпляр
try:
    invalid_user = User(
        id="not an integer",
        name="A",
        email="not_an_email",
        age=150,
        birth_date="invalid_date"
    )
except ValidationError as e:
    print(f"Ошибка валидации: {e}")
