from aiogram import Router

from middleware.isbanned_middleware import UserBannedMessage, UserBannedCallback

from handlers.user.start_bot import start_router

user_router = Router()
user_router.message.middleware(UserBannedMessage())
user_router.callback_query.middleware(UserBannedCallback())


user_router.include_routers(
    start_router
)

