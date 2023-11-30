from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from yaml import safe_load

from typing import Union

CONFIG_FILE = str(Path(__file__).parent.absolute()) + "/settings.yaml"


class App(BaseModel):
    endpoint: str
    environment: str
    origins: list[str]
    static_dir: str = "static"


class Postgres(BaseModel):
    host: str
    user: str
    password: str
    database: str
    port: int


class Settings(BaseSettings):
    app: App
    postgres: Postgres


def load_settings(path: Union[Path, str] = CONFIG_FILE) -> Settings:
    if isinstance(path, str):
        path = Path(path)
    with path.open() as f:
        return Settings.parse_obj(safe_load(f))
