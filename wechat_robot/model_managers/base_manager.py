import logging
from typing import Dict, List

logger = logging.getLogger("ModelManager")


class BaseManager:
    def __init__(self, model=None):
        self.model = model
        self.model_name = model._meta.db_table

    @classmethod
    async def get_by_id(cls, _id):
        """根据ID获取信息"""
        obj = await cls.model.filter(id=_id).first()
        return obj

    @classmethod
    async def get_values_with_params(cls, filter_params, values_field=None):
        """-"""
        return await cls.model.filter(**filter_params).values(*values_field)

    @classmethod
    async def get_with_params(cls, filter_params):
        """ 普通查询 """
        return await cls.model.filter(**filter_params)

    @classmethod
    async def get_all_with_params(cls, filter_params):
        """ .all """
        return await cls.model.filter(**filter_params).all()

    @classmethod
    async def get_with_params_first(cls, filter_params):
        """ 普通查询 """
        return await cls.model.filter(**filter_params).first()

    @classmethod
    async def get_values_list_with_params(cls, filter_params, values_list_field=None, flat=True):
        """ .values_list """
        return await cls.model.filter(**filter_params).values_list(values_list_field, flat=flat)

    @classmethod
    async def get_by_limit_and_value(cls, value, offset=0, limit=8):
        """-"""
        return await cls.model.filter().offset(offset).limit(limit).values_list(value, flat=True)

    @classmethod
    async def create(cls, to_create: Dict):
        """
        创建一个
        """
        try:
            obj = await cls.model.create(**to_create)
            logger.info(f"{cls.model.__name__}.create 创建成功 id: {obj.id}")
            return obj
        except Exception:
            logger.exception(f"{cls.model.__name__}.create 创建失败")
            return None

    async def bulk_create(self, to_creates: List[Dict], using_db=None) -> bool:
        """
        批量创建
        """
        if not to_creates:
            return False
        try:
            models = [self.model(**to_create) for to_create in to_creates]
            await self.model.bulk_create(models, using_db=using_db)
            logger.info(
                f"{self.model.__name__}.bulk_create 批量创建成功 数量: {len(models)}")
            return True
        except Exception:
            logger.exception(f"{self.model.__name__}.bulk_create 批量创建失败")
            return False
