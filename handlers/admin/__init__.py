from aiogram import Router
from .start import router as start_router
from .add_question import router as add_question_router


router = Router()
router.include_routers(start_router, add_question_router)
