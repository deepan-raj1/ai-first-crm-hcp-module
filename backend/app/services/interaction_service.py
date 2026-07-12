from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate, InteractionUpdate


def create_interaction(db: Session, interaction: InteractionCreate):
    db_interaction = Interaction(**interaction.model_dump())

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_all_interactions(db: Session):
    return db.query(Interaction).all()


def get_interaction_by_id(db: Session, interaction_id: int):
    return (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )


def update_interaction(
    db: Session,
    interaction_id: int,
    interaction: InteractionUpdate,
):
    db_interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not db_interaction:
        return None

    update_data = interaction.model_dump()

    for key, value in update_data.items():
        setattr(db_interaction, key, value)

    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def delete_interaction(db: Session, interaction_id: int):
    db_interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not db_interaction:
        return None

    db.delete(db_interaction)
    db.commit()

    return db_interaction