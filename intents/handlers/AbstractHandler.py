from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

"""
    責任鏈結基礎介面
    @author: Gordon Fang
    @date: 2022-06-27
"""
class AbstractHandler(ABC):
    """
        指定責任鏈下一個處理器
        @:param self : 物件本身
        @:param handler: 下一個處理器
    """

    @abstractmethod
    def set_next(self, handler: AbstractHandler):
        pass

    """
        指定責任鏈下一個處理器
        @:param self : 物件本身
        @:param handler: 下一個處理器
    """

    @abstractmethod
    def handle(self, request):
        pass
