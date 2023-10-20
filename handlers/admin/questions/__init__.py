from aiogram import Router
from .add import router as add_question_router
from .get_info import router as questions_list_router
from .update import router as update_question_router
from .delete import router as delete_question_router


router = Router()
router.include_routers(
    add_question_router,
    questions_list_router,
    update_question_router,
    delete_question_router,
)
