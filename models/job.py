import sqlalchemy as sa


class Job:
    # __tablename__ = "jobs"
    # __table_args__ = (sa.PrimaryKeyConstraint("object_id", "job_id", name="jobs_pkey"),)
    #
    # object_id = sa.Column(sa.String(), nullable=False, primary_key=True)
    # job_id = sa.Column(sa.String(), nullable=False, primary_key=True)
    # status = sa.Column(sa.String(), nullable=False, primary_key=True)
    # timestamp = sa.Column(
    #     sa.DateTime(timezone=False), nullable=False)

    def get_job_by_object_id(self, id: str):
        # session = sa.orm.session.Session()
        # try:
        #     return session.query(Greyhound).filter(Greyhound.name == name).one()
        # except sa.orm.exc.NoResultFound:
        #     raise errors.NoResultFound(self.grey_not_found_error_code)
        pass

    def create_or_update_job(self):
        pass
