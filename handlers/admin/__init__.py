from aiogram import Router

from handlers.admin.start_admin import admin_start

from filters.filters import IsAdmin


admin_router = Router()
admin_router.message.filter(IsAdmin())
admin_router.callback_query.filter(IsAdmin())


admin_router.include_routers(
    admin_start
)

