# ������� ����������� ���������
py -m venv .venv_home

# ���������, ���������� �� ���� ��������� (������ �� ��������� � ����� Scripts)
$activateScript = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    # ���������� ����������� ���������
    & $activateScript
} else {
    Write-Error "�� ������� ����� ������ ���������: $activateScript"
    exit 1
}

# ��������� pip �� ��������� ������
python -m pip install --upgrade pip

# ���������, ���������� �� ���� requirements.txt
$requirementsFile = "requirements.txt"
if (Test-Path $requirementsFile) {
    # ������������� ������
    pip install -r $requirementsFile
} else {
    Write-Error "�� ������� ����� ����: $requirementsFile"
    exit 1
}

# ���������� ������������� ������
pip list

pause