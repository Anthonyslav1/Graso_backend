# middleware/profile_upload.py
import os
from fastapi import HTTPException, UploadFile, File
from PIL import Image
import io
import time
upload_dir = "uploads/property"
os.makedirs(upload_dir, exist_ok=True)

async def save_property_picture(file: UploadFile = File(...)):
    """Saves a profile picture"""
    if not file.content_type.startswith('image'):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    file_name = f"{int(time.time())}_{file.filename}"
    file_path = os.path.join(upload_dir, file_name)

    try:
        image = Image.open(io.BytesIO(await file.read()))
        image.save(file_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return file_name, file_path