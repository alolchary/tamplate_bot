from aiogram import Router


from filters.filters import ChatTypeFilter

from handlers.user import user_router
from handlers.admin import admin_router

from middleware.database_middleware import DataBaseMiddleware





main_router = Router()
main_router.message.filter(ChatTypeFilter(['private']))

main_router.message.middleware(DataBaseMiddleware())
main_router.callback_query.middleware(DataBaseMiddleware())



main_router.include_routers(
    user_router, admin_router
)