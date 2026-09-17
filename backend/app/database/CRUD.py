from sqlalchemy.orm import Session


def create_record(db: Session, model, data: dict):
    """
    Create a new database record.
    """

    record = model(**data)

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_record(db: Session, model, record_id):
    """
    Get a record by ID.
    """

    return (
        db.query(model)
        .filter(model.id == record_id)
        .first()
    )


def get_all_records(db: Session, model):
    """
    Get all records.
    """

    return db.query(model).all()


def delete_record(db: Session, model, record_id):
    """
    Delete a record.
    """

    record = (
        db.query(model)
        .filter(model.id == record_id)
        .first()
    )

    if record:
        db.delete(record)
        db.commit()

        return True

    return False