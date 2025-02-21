from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

app = FastAPI()

# Allow frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define required sizes
SIZES = [(300, 250), (728, 90), (160, 600), (300, 600)]

@app.post("/resize/")
async def resize_image(file: UploadFile = File(...)):
    try:
        # Open the uploaded image
        image = Image.open(io.BytesIO(await file.read()))
        resized_images = {}

        for width, height in SIZES:
            img_resized = image.resize((width, height))
            img_io = io.BytesIO()
            img_resized.save(img_io, format="PNG")
            img_io.seek(0)
            resized_images[f"{width}x{height}"] = img_io.getvalue()

        return {"message": "Images resized successfully", "sizes": list(resized_images.keys())}
    except Exception as e:
        return {"error": str(e)}
