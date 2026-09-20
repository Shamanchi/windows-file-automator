from fastapi import APIRouter

router = APIRouter()

@router.get('/health')
async def health():
    return {'status': 'ok'}

@router.get('/watched-paths')
async def watched_paths():
    from app.core.config import settings
    return {'paths': settings.watch_paths}