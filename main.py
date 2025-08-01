import asyncio

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
import jwt, hashlib
from datetime import datetime, timedelta, timezone
import yaml, json, requests


app = FastAPI()





yaml_path = "version_output/output.yaml"
yaml_path_test = "version_output/output_result.yaml"
yaml_path_test_mashed = "version_output/output_result_mashed.yaml"
@app.get('/yaml_zamen.result', response_class=PlainTextResponse, tags=["yaml_zamen.result"])
async def yaml_zamen():
    """
    Замена пути YAML.

    :return: Содержимое YAML-файла.
    """
    try:
        with open(yaml_path_test, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {yaml_path_test}")
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в YAML: {str(e)}")

    return yaml.dump(yaml_data, allow_unicode=True, default_flow_style=False)

@app.get('/yaml_zamen', response_class=PlainTextResponse, tags=["yaml_zamen"])
async def yaml_zamen():
    """
    Замена пути YAML.

    :return: Содержимое YAML-файла.
    """
    try:
        with open(yaml_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {yaml_path}")
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в YAML: {str(e)}")

    return yaml.dump(yaml_data, allow_unicode=True, default_flow_style=False)

@app.get('/yaml_zamen.result:{group_id}', response_class=PlainTextResponse, tags=["yaml_zamen.result:group"])
async def yaml_zamen_result_group(group_id: str):
    """
    Замена пути YAML.

    :return: Содержимое YAML-файла.
    """
    try:
        with open(yaml_path_test, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
        zamen = yaml_data.get(group_id)
        response = {group_id: zamen if zamen is not None else "Нету замен или такой группы"}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {yaml_path_test}")
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в YAML: {str(e)}")

    return yaml.dump(response, allow_unicode=True, default_flow_style=False)

@app.get('/yaml_zamen:{group_id}', response_class=PlainTextResponse, tags=["yaml_zamen:group"])
async def yaml_zamen_group(group_id: str):
    """
    Замена пути YAML.

    :return: Содержимое YAML-файла.
    """
    try:
        with open(yaml_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
        zamen = yaml_data.get(group_id)
        response = {group_id: zamen if zamen is not None else "Нету замен или такой группы"}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {yaml_path}")
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в YAML: {str(e)}")

    return yaml.dump(response, allow_unicode=True, default_flow_style=False)

@app.get('/yaml_zamen.result.vip', response_class=PlainTextResponse, tags=["yaml_zamen.result.vip"])
async def yaml_zamen_result_vip():
    """
    Замена пути YAML.

    :return: Содержимое YAML-файла.
    """
    try:
        with open(yaml_path_test_mashed, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {yaml_path_test_mashed}")
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в YAML: {str(e)}")

    return yaml.dump(yaml_data, allow_unicode=True, default_flow_style=False, sort_keys=False)


json_path = "version_output/output.json"
json_path_test = "version_output/output_result.json"
json_path_test_mashed = "version_output/output_result_mashed.json"
@app.get('/json_zamen', response_class=PlainTextResponse, tags=["json_zamen"])
async def json_zamen():
    """
    Замена пути JSON.

    :return: Содержимое JSON-файла.
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {json_path}")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в JSON: {str(e)}")

    return json.dumps(json_data, ensure_ascii=False, indent=4)

@app.get('/json_zamen:{group_id}', response_class=PlainTextResponse, tags=["json_zamen:group"])
async def json_zamen_group(group_id: str):
    """
    Замена пути JSON.

    :return: Содержимое JSON-файла.
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        zamen = json_data.get(group_id)
        response = {group_id: zamen if zamen is not None else "Нету замен или такой группы"}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {json_path}")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в JSON: {str(e)}")

    return json.dumps(response, ensure_ascii=False)

@app.get('/json_zamen.result', response_class=PlainTextResponse, tags=["json_zamen.result"])
async def json_zamen_result():
    """
    Замена пути JSON.

    :return: Содержимое JSON-файла.
    """
    try:
        with open(json_path_test, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {json_path_test}")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в JSON: {str(e)}")

    return json.dumps(json_data, ensure_ascii=False, indent=4)

@app.get('/json_zamen.result:{group_id}', response_class=PlainTextResponse, tags=["json_zamen.result:group"])
async def json_zamen_result_group(group_id: str):
    """
    Замена пути JSON.

    :return: Содержимое JSON-файла.
    """
    try:
        with open(json_path_test, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        zamen = json_data.get(group_id)
        response = {group_id: zamen if zamen is not None else "Нету замен или такой группы"}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {json_path_test}")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в JSON: {str(e)}")

    return json.dumps(response, ensure_ascii=False)

@app.get('/json_zamen.result.vip', response_class=PlainTextResponse, tags=["json_zamen.result.vip"])
async def json_zamen_result_vip():
    """
    Замена пути JSON.

    :return: Содержимое JSON-файла.
    """
    try:
        with open(json_path_test_mashed, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл не найден: {json_path_test_mashed}")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в JSON: {str(e)}")

    return json.dumps(json_data, ensure_ascii=False, indent=4)

JSON_FILE = "array_test.json"
JSON_FILE_ORIG = "array.json"
SYNC_PASSWORD = "SJjGbHQeCBgsgwZmG_VbL8OO-xaWy5"  # Задайте тот же пароль, что используется на отправляющем сервере
JWT_token_SYNC = 'DsgJwsD-saqqsagmbc-dsaqkwelqweqsabvc'
URL_SERVER_ONE = 'https://server-obrabotka-one.alwaysdata.net/sync_update'


@app.post("/update_json")
async def update_json(request: Request):
    form = await request.form()
    
    password = form.get("password")
    if password != SYNC_PASSWORD:
        raise HTTPException(status_code=403, detail="Access denied: Invalid password")
    
    data_str = form.get("data")
    if not data_str:
        raise HTTPException(status_code=400, detail="Missing data")
    
    token = form.get("token")
    if not token:
        raise HTTPException(status_code=403, detail="Missing token")
    
    try:
        payload = jwt.decode(token, JWT_token_SYNC, algorithms=["HS256"])
        # Проверяем, что данные в токене совпадают с переданными
        if payload.get("data") != data_str:
            raise HTTPException(status_code=403, detail="Invalid token data")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Expired token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
    
    try:
        new_data = json.loads(data_str)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    with open(JSON_FILE_ORIG, "w", encoding="utf-8") as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)
    
    return {"message": "JSON обновлён"}


def send_file_back_to_previous():
    # Читаем и сериализуем данные (без изменений)
    with open(JSON_FILE_ORIG, "r", encoding="utf-8") as file:
        data = json.load(file)
    data_str = json.dumps(data, ensure_ascii=False, indent=4)

    # Генерируем JWT (без изменений)
    payload = {
        "data": data_str,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
        "iat": datetime.now(timezone.utc)
    }
    token = jwt.encode(payload, JWT_token_SYNC, algorithm="HS256")

    # Отправляем POST-запрос через requests
    response = requests.post(
        URL_SERVER_ONE,
        data={
            "password": SYNC_PASSWORD,  # Можно убрать, если не используется
            "data": data_str,
            "token": token
        }
    )

    # Проверяем статус ответа (логика без изменений)
    if response.status_code == 200:
        print("Файл успешно отправлен:", response.text)
    else:
        print("Ошибка при отправке файла:", response.text)




if __name__ == "__main__":
    

    # Запуск FastAPI в асинхронном режиме
    uvicorn.run(app, host="::", port=8100, proxy_headers=True, forwarded_allow_ips="::1")