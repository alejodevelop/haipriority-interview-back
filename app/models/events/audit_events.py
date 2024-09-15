from sqlalchemy import event
from sqlalchemy.orm.attributes import get_history
from datetime import datetime
import json

from app.models.auditlog_model import AuditLog, AuditAction
from app.models.creditcard_model import CreditCard
from app.models.debitcard_model import DebitCard
from app.models.loan_model import Loan


# Helper function to convert object state to dictionary
def get_model_data(instance):
    data = {}
    for c in instance.__table__.columns:
        value = getattr(instance, c.name)
        if isinstance(value, datetime):
            value = value.isoformat()  # Convert datetime to ISO format string
        data[c.name] = value
    return data


# Event listener for inserts
@event.listens_for(CreditCard, 'after_insert')
@event.listens_for(DebitCard, 'after_insert')
@event.listens_for(Loan, 'after_insert')
def after_insert(mapper, connection, target):
    audit_log = AuditLog(
        table_name=target.__tablename__,
        record_id=target.id,
        old_values=None,
        new_values=json.dumps(get_model_data(target)),
        action=AuditAction.CREATE,
        user_id=target.user_id,  # Replace this with current user context
    )
    connection.execute(AuditLog.__table__.insert(), audit_log.__dict__)


# Event listener for updates
@event.listens_for(CreditCard, 'before_update')
@event.listens_for(DebitCard, 'before_update')
@event.listens_for(Loan, 'before_update')
def before_update(mapper, connection, target):
    old_values = {}
    for key, value in get_model_data(target).items():
        history = get_history(target, key)
        if history.has_changes():
            old_values[key] = history.deleted[0] if history.deleted else None
    target._old_values = old_values


@event.listens_for(CreditCard, 'after_update')
@event.listens_for(DebitCard, 'after_update')
@event.listens_for(Loan, 'after_update')
def after_update(mapper, connection, target):
    audit_log = AuditLog(
        table_name=target.__tablename__,
        record_id=target.id,
        old_values=json.dumps(target._old_values),
        new_values=json.dumps(get_model_data(target)),
        action=AuditAction.UPDATE,
        user_id=target.user_id,  # Replace this with current user context
    )
    connection.execute(AuditLog.__table__.insert(), audit_log.__dict__)


# Event listener for deletes
@event.listens_for(CreditCard, 'before_delete')
@event.listens_for(DebitCard, 'before_delete')
@event.listens_for(Loan, 'before_delete')
def before_delete(mapper, connection, target):
    target._old_values = get_model_data(target)


@event.listens_for(CreditCard, 'after_delete')
@event.listens_for(DebitCard, 'after_delete')
@event.listens_for(Loan, 'after_delete')
def after_delete(mapper, connection, target):
    audit_log = AuditLog(
        table_name=target.__tablename__,
        record_id=target.id,
        old_values=json.dumps(target._old_values),
        new_values=None,
        action=AuditAction.DELETE,
        user_id=target.user_id,  # Replace this with current user context
    )
    connection.execute(AuditLog.__table__.insert(), audit_log.__dict__)
