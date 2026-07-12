from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.interaction import (
    InteractionCreate,
    InteractionUpdate,
    InteractionResponse,
)
from app.services.interaction_service import (
    create_interaction,
    get_all_interactions,
    get_interaction_by_id,
    update_interaction,
    delete_interaction,
)

router = APIRouter(
    prefix="/api/interactions",
    tags=["Interactions"],
)


@router.post("/", response_model=InteractionResponse)
def create_new_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):
    return create_interaction(db, interaction)


@router.get("/", response_model=list[InteractionResponse])
def get_interactions(
    db: Session = Depends(get_db),
):
    return get_all_interactions(db)


@router.get("/{interaction_id}", response_model=InteractionResponse)
def get_interaction(
    interaction_id: int,
    db: Session = Depends(get_db),
):
    interaction = get_interaction_by_id(db, interaction_id)

    if not interaction:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    return interaction


@router.put("/{interaction_id}", response_model=InteractionResponse)
def update_existing_interaction(
    interaction_id: int,
    interaction: InteractionUpdate,
    db: Session = Depends(get_db),
):
    updated = update_interaction(
        db,
        interaction_id,
        interaction,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    return updated


@router.delete("/{interaction_id}")
def delete_existing_interaction(
    interaction_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_interaction(
        db,
        interaction_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    return {
        "message": "Interaction deleted successfully"
    }