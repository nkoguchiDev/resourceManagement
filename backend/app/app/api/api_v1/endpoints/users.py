import uuid

from fastapi import APIRouter, Depends
from fastapi import APIRouter, Body, Depends, HTTPException
from neo4j import GraphDatabase

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_super_user(
    user: schemas.User,
    db: GraphDatabase = Depends(
        deps.get_db)):
    result = crud.user.create(db, email=user.email, password=user.password)
    result["password"] = "******"
    return result
