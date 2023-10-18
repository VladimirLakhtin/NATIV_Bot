from aiogram import Router

from .users import router as user_router
from .admin import router as admin_router


router = Router()
router.include_routers(admin_router, user_router)
