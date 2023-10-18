from aiogram import Router
from handlers.admin.questions.add import router as add_question_router
from .get_info import router as questions_list_router
from handlers.admin.questions.update import router as update_question_router
from handlers.admin.questions.delete import router as delete_question_router


router = Router()
router.include_routers(
    start_router,
    add_question_router,
    questions_list_router,
    update_question_router,
    delete_question_router,
)
