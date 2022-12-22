# -*- coding: utf-8 -*-
from typing import List


class ErrorResponseException(Exception):
    def __init__(
        self,
        is_success: bool = False,
        data: List = None,
        status_code: int = 200,
    ) -> None:
        self.is_success = is_success
        self.data = data
        self.status_code = status_code
        self.length_data = len(data) if data else None
