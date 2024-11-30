
from sqlalchemy import select, update, delete, insert
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from utils.db_api.models.users import User
from typing import Union



class UserDataBase:
    def __init__(self, session: AsyncSession):
        self.session = session


        # async with engine.begin() as conn:
        #     await conn.run_sync(Base.metadata.create_all)


    
    async def get_info(self, user_id: int) -> Union[User, None]:
        sql = select(User).where(
            User.user_id == user_id
        )
        info = await self.session.execute(sql)
        info = info.scalar()
        return info


    async def add_user(self, user_id: int, username: str) -> None:
        info = await self.get_info(user_id)
        print(info)


    async def get_ban(self, user_id: int) -> bool:
        sql = select(User).where((User.user_id == user_id) & (User.banned == 1))
        f = await self.session.execute(sql)
        return f.fetchone()