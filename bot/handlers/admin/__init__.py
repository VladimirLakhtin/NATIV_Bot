from aiogram import Router, F

from filters.admin import AdminFilter
from .start import router as start_router
from .questions import router as question_router
from .consultation import router as consult_router
from .lesson import router as lesson_router
from .chats import router as chats_router


router = Router()
router.message.filter(AdminFilter())
router.include_routers(
    start_router,
    question_router,
    consult_router,
    chats_router,
    lesson_router,
)
