from typing import List, Optional

from pydantic import BaseModel, Field

class WxCheckAuth(BaseModel):
    """-"""
    signature: str = Field(description='微信加密签名')
    timestamp: str = Field(description='时间戳')
    nonce: str = Field(description='随机数')
    echostr: str = Field(description='随机字符串')
