from unittest.mock import patch
from app.domain import jobs, models


@patch("app.adapters")
class TestProcess:
    def test_object_id_not_found_in_db_and_all_calls_succeed(self, adapters):
        print("adapters mock: ", adapters)
        some_object_id = "some-object-id"
        adapters.db.Jobs.get_by_object_id.return_value = []
        created_job = models.Job(
            id="some-job-id",
            object_id=some_object_id,
        )
        adapters.db.Jobs.create_or_update.return_value = created_job
        adapters.queues.Processing.enqueue.assert_called_once_with(str(created_job.id))
        expected_response = {"job_id": f"{created_job.id}"}
        assert jobs.process(some_object_id) == expected_response

    def test_object_id_found_in_db_newer_than_five_minutes(self, adapters):
        pass

    def test_object_id_found_in_db_older_than_five_minutes(self, adapters):
        pass

    def test_reading_from_db_fails(self, adapters):
        pass

    def test_writing_to_db_fails(self, adapters):
        pass

    def test_enqueuing_fails(self, adapters):
        pass


@patch("app.adapters")
class TestRetrieve:
    def test_job_is_found_in_db(self, adapters):
        pass

    def test_job_not_found_in_db(self, adapters):
        pass

    def test_reading_from_db_fails(self, adapters):
        pass
