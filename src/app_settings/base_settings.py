# -*- coding: utf-8 -*-
import os

SELECT_ENV_NAME = os.environ.get("APP_ENV_NAME")


class BaseSettingsMixin:
    def select_env(self) -> str:
        if SELECT_ENV_NAME in ("dev", "stg", "prod", "local", "redirect"):
            env_name = f"{SELECT_ENV_NAME}.env"
        else:
            env_name = ".env"
        return env_name

    def setup_proxy(self):
        self.add_custom_proxy()
        self.show_proxy_configuration()

    def add_custom_proxy(self):
        if (
            not hasattr(self, "APP_USE_PROXY")
            or not hasattr(self, "APP_PROXY_ADD")
            or not hasattr(self, "APP_NO_PROXY")
        ):
            print("Not found proxy configurations")

        if not getattr(self, "APP_USE_PROXY"):
            return

        no_proxy = os.environ.get("no_proxy")

        if getattr(self, "APP_USE_PROXY"):
            for i in ["http", "https"]:
                os.environ[i] = getattr(self, "APP_USE_PROXY")
        if getattr(self, "APP_NO_PROXY"):
            if no_proxy:
                os.environ["no_proxy"] = (
                    no_proxy + "," + getattr(self, "APP_NO_PROXY")
                )  # noqa
            else:
                os.environ["no_proxy"] = getattr(self, "APP_NO_PROXY")

    def show_proxy_configuration(self):
        print("*" * 50)
        print(f'http_proxy {os.environ.get("http_proxy")}')
        print(f'https_proxy {os.environ.get("https_proxy")}')
        print(f'no_proxy {os.environ.get("no_proxy")}')
        print("*" * 50)
