from aiogram import Router

from .start import router as start_router
from .questions import router as question_router

router = Router()
router.include_routers(start_router, question_router)
