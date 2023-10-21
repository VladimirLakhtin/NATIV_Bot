from aiogram import Router

from middlewares.track_actions import TrackChatActionMiddleware, TrackChatActionCallbackMiddleware
from .start import router as start_router
from .questions import router as questions_router
from .contacts import router as contacts_router
from .consultation import router as consult_router
from .lesson import router as lesson_router
from .connect import router as connect_router

router = Router()
router.message.middleware(TrackChatActionMiddleware())
router.callback_query.outer_middleware(TrackChatActionCallbackMiddleware())
router.include_routers(
    start_router,
    questions_router,
    contacts_router,
    consult_router,
    lesson_router,
    connect_router,
)
