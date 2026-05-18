"""
Configuration settings for Passport Photo Generator
Professional studio-grade photo processing
"""

import os
from dataclasses import dataclass
from typing import Tuple

@dataclass
class PassportPhotoConfig:
    """Passport photo specifications and processing parameters"""
    
    # ============ PASSPORT PHOTO DIMENSIONS ============
    # Standard passport photo size: 3.5cm x 4.5cm
    PASSPORT_WIDTH_CM: float = 3.5
    PASSPORT_HEIGHT_CM: float = 4.5
    DPI: int = 300  # Print resolution
    
    # Calculate pixel dimensions at 300 DPI
    # 1 inch = 2.54 cm, 1 inch = DPI pixels
    CM_TO_INCH: float = 0.393701
    PASSPORT_WIDTH_PX: int = int(PASSPORT_WIDTH_CM * CM_TO_INCH * DPI)   # ~413px
    PASSPORT_HEIGHT_PX: int = int(PASSPORT_HEIGHT_CM * CM_TO_INCH * DPI)  # ~531px
    
    # ============ A4 SHEET SPECIFICATIONS ============
    A4_WIDTH_MM: int = 210
    A4_HEIGHT_MM: int = 297
    A4_WIDTH_PX: int = int(A4_WIDTH_MM * CM_TO_INCH * DPI / 10)   # ~2480px
    A4_HEIGHT_PX: int = int(A4_HEIGHT_MM * CM_TO_INCH * DPI / 10)  # ~3508px
    
    # ============ A4 LAYOUT PARAMETERS ============
    A4_MARGIN_MM: int = 10  # Margins on all sides
    A4_MARGIN_PX: int = int(A4_MARGIN_MM * CM_TO_INCH * DPI / 10)
    A4_SPACING_MM: int = 3   # Space between photos
    A4_SPACING_PX: int = int(A4_SPACING_MM * CM_TO_INCH * DPI / 10)
    
    # ============ COLOR SPECIFICATIONS ============
    BACKGROUND_COLOR: Tuple[int, int, int] = (255, 255, 255)  # White RGB
    BACKGROUND_HEX: str = "#FFFFFF"
    BORDER_COLOR: Tuple[int, int, int] = (220, 220, 220)  # Light gray
    BORDER_THICKNESS_PX: int = 1  # 1px cutting guide
    
    # ============ IMAGE ENHANCEMENT PARAMETERS ============
    # Upscaling
    UPSCALE_FACTOR: int = 2  # 2x upscaling
    GFPGAN_MODEL: str = "detection_Resnet50_final.pth"  # Face restoration model
    
    # Denoising
    DENOISE_STRENGTH: float = 10.0  # Bilateral filter diameter
    DENOISE_COLOR_SIGMA: float = 0.1
    DENOISE_SPACE_SIGMA: float = 0.1
    
    # Sharpening
    SHARPEN_AMOUNT: float = 1.5  # Unsharp mask amount
    SHARPEN_RADIUS: float = 0.5
    SHARPEN_THRESHOLD: int = 0
    
    # ============ COLOR GRADING PARAMETERS ============
    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    CLAHE_CLIP_LIMIT: float = 3.0
    CLAHE_TILE_SIZE: int = 8
    
    # White Balance
    WHITE_BALANCE_METHOD: str = "gray_world"  # Options: "gray_world", "max_white"
    
    # Brightness & Contrast
    BRIGHTNESS_GAIN: float = 1.05  # 5% brightness increase
    CONTRAST_GAIN: float = 1.1    # 10% contrast increase
    SATURATION_GAIN: float = 1.08  # 8% saturation increase
    
    # ============ FACIAL REFINEMENT PARAMETERS ============
    # Eye Enhancement
    EYE_SHARPEN_RADIUS: float = 1.0
    EYE_BRIGHTNESS_BOOST: float = 1.15  # 15% brightness boost
    EYE_CONTRAST_BOOST: float = 1.2
    
    # Under-eye Shadow Reduction
    UNDER_EYE_SMOOTHING: float = 2.0
    SHADOW_REDUCTION_STRENGTH: float = 0.3
    
    # Face Clarity
    CLARITY_AMOUNT: float = 0.4
    CLARITY_RADIUS: float = 15
    
    # ============ CROPPING PARAMETERS ============
    # Head occupies 70-80% of frame height
    HEAD_SIZE_RATIO_MIN: float = 0.70
    HEAD_SIZE_RATIO_MAX: float = 0.80
    HEAD_SIZE_RATIO_TARGET: float = 0.75  # Target 75%
    
    # Top margin (space above head)
    TOP_MARGIN_RATIO: float = 0.05  # 5% of frame
    
    # ============ OUTPUT SETTINGS ============
    OUTPUT_DIR: str = "output"
    
    # Export formats
    EXPORT_PNG: bool = True
    EXPORT_JPEG: bool = True
    EXPORT_PDF: bool = True
    PNG_COMPRESSION: int = 9  # Max compression (0-9)
    JPEG_QUALITY: int = 95    # High quality (0-100)
    
    # PDF Settings
    PDF_DPI: int = 300
    PDF_MARGIN_MM: int = 5
    
    # ============ PROCESSING OPTIONS ============
    SAVE_INTERMEDIATE_STEPS: bool = False  # Save debug images
    VERBOSE: bool = True  # Print progress messages
    DEVICE: str = "cuda"  # Options: "cuda", "cpu"
    
    # ============ FACE DETECTION PARAMETERS ============
    FACE_CONFIDENCE_THRESHOLD: float = 0.5
    MIN_FACE_SIZE: int = 50  # Minimum face size in pixels
    
    # ============ BACKGROUND REMOVAL ============
    REMBG_MODEL: str = "u2net"  # Models: "u2net", "u2netp", "u2net_human_seg"
    EDGE_REFINEMENT_ITERATIONS: int = 3
    EDGE_REFINEMENT_KERNEL_SIZE: int = 3
    EDGE_FEATHER_RADIUS: int = 2  # Smooth edge transitions
    
    def __post_init__(self):
        """Ensure output directory exists"""
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)

# Global config instance
CONFIG = PassportPhotoConfig()

# ============ HELPER FUNCTIONS ============

def get_a4_grid_layout(passport_width: int, passport_height: int) -> Tuple[int, int, int, int]:
    """
    Calculate optimal grid layout for A4 sheet
    
    Returns:
        (photos_per_row, photos_per_column, photos_total, spacing_between)
    """
    margin = CONFIG.A4_MARGIN_PX
    spacing = CONFIG.A4_SPACING_PX
    
    # Calculate available space
    available_width = CONFIG.A4_WIDTH_PX - (2 * margin)
    available_height = CONFIG.A4_HEIGHT_PX - (2 * margin)
    
    # Calculate number of photos that fit
    photos_per_row = max(1, available_width // (passport_width + spacing))
    photos_per_col = max(1, available_height // (passport_height + spacing))
    
    # Adjust to standard grid layouts
    if photos_per_row > 3:
        photos_per_row = 3
    if photos_per_col > 5:
        photos_per_col = 5
    
    total_photos = photos_per_row * photos_per_col
    
    return photos_per_row, photos_per_col, total_photos, spacing

if __name__ == "__main__":
    print("Passport Photo Generator Configuration")
    print("=" * 50)
    print(f"Passport Photo: {CONFIG.PASSPORT_WIDTH_PX}x{CONFIG.PASSPORT_HEIGHT_PX} px")
    print(f"A4 Sheet: {CONFIG.A4_WIDTH_PX}x{CONFIG.A4_HEIGHT_PX} px @ {CONFIG.DPI} DPI")
    print(f"Output Directory: {CONFIG.OUTPUT_DIR}")
    
    rows, cols, total, spacing = get_a4_grid_layout(CONFIG.PASSPORT_WIDTH_PX, CONFIG.PASSPORT_HEIGHT_PX)
    print(f"\nOptimal A4 Layout: {rows}x{cols} grid = {total} photos")
