from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.orm import Session

class Cursor:

    def __init__(self, model: object, session: Session):
        self._model = model
        self._session = session

    def commit(self):
        self._session.commit()

    def close(self):
        self._session.close()

    def paste_row(self, row: dict):
        query = (
            insert(self._model).
                values(**row)
        )
        self._session.execute(query)

    def paste_rows(self, *rows: dict):
        query = (
            insert(self._model)
                .values([row for row in rows])
        )
        self._session.execute(query)

    def delete_row_by_criteria(self, criteria: dict):
        query = (
            delete(self._model)
                .filter_by(**criteria)
        )
        self._session.execute(query)

    def delete_all_rows(self):
        query = delete(self._model)
        self._session.execute(query)

    def update_row_by_criteria(self, criteria: dict, values: dict):
        query = (
            update(self._model)
                .filter_by(**criteria)
                .values(values)
        )
        self._session.execute(query)

    def get_row_by_criteria(self, criteria: dict):
        query = (
            select(self._model)
                .filter_by(**criteria)
        )
        return (self._session.execute(query)).first()

    def get_rows_offset_limit(self, limit: int, offset: int):
        query = (
            select(self._model)
                .limit(limit)
                .offset(offset)
        )
        execute = self._session.execute(query)

        if limit == 1:
            return execute.first()
        else:
            return execute.all()

    def get_all_rows(self):
        query = select(self._model)
        return (self._session.execute(query)).all()

    def get_rows_count(self):
        query = (
            select([func.count()])
                .select_from(self._model)
        )
        return (self._session.execute(query)).fetchone()[0]