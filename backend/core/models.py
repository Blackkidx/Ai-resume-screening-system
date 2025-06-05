# =============================================================================
# 📝 PYDANTIC MODELS - สำหรับ API Request/Response
# =============================================================================
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional
from enum import Enum

# =============================================================================
# ENUMS 🏷️
# =============================================================================
class UserType(str, Enum):
    STUDENT = "Student"
    HR = "HR"
    ADMIN = "Admin"

# =============================================================================
# AUTH MODELS 🔐
# =============================================================================
class UserRegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str
    phone: Optional[str] = None
    user_type: UserType = UserType.STUDENT
    
    @validator('username')
    def username_must_be_valid(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        if not v.replace('_', '').replace('-', '').isalnum():
            raise ValueError('Username can only contain letters, numbers, underscore and hyphen')
        return v
    
    @validator('password')
    def password_must_be_strong(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    full_name: str
    phone: Optional[str] = None
    user_type: UserType
    is_active: bool
    created_at: datetime

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    user_info: UserResponse

class UserUpdateRequest(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str
    
    @validator('new_password')
    def password_must_be_strong(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v

# =============================================================================
# RESUME MODELS 📄
# =============================================================================
class ResumeUploadResponse(BaseModel):
    id: str
    user_id: str
    file_path: str
    file_type: str
    original_filename: str
    uploaded_at: datetime

# =============================================================================
# JOB POSITION MODELS 💼
# =============================================================================
class JobPositionCreate(BaseModel):
    title: str
    description: str
    department: str
    duration: int  # วัน
    requirements: Optional[str] = None
    
class JobPositionResponse(BaseModel):
    id: str
    title: str
    description: str
    department: str
    duration: int
    is_active: bool
    created_by: str
    created_at: datetime

# =============================================================================
# SKILL MODELS 🛠️
# =============================================================================
class SkillCreate(BaseModel):
    name: str
    type: str  # Hard Skill, Soft Skill
    category: str

class SkillResponse(BaseModel):
    id: str
    name: str
    type: str
    category: str

# =============================================================================
# MATCHING MODELS 🎯
# =============================================================================
class MatchingResultResponse(BaseModel):
    id: str
    resume_id: str
    position_id: str
    technical_score: float
    soft_skill_score: float
    matching_score: float
    status: str
    created_at: datetime