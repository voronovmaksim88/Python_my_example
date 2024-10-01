# Создаем виртуальное окружение
py -m venv .venv_home

# Проверяем, существует ли файл активации (обычно он находится в папке Scripts)
$activateScript = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    # Активируем виртуальное окружение
    & $activateScript
} else {
    Write-Error "Не удалось найти скрипт активации: $activateScript"
    exit 1
}

# Обновляем pip до последней версии
python -m pip install --upgrade pip

# Проверяем, существует ли файл requirements.txt
$requirementsFile = "requirements.txt"
if (Test-Path $requirementsFile) {
    # Устанавливаем пакеты
    pip install -r $requirementsFile
} else {
    Write-Error "Не удалось найти файл: $requirementsFile"
    exit 1
}

# Показываем установленные пакеты
pip list

pause