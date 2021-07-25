from app.models import Job, Status
import factory


class JobFactory(factory.Factory):
    class Meta:
        model = Job

    id = factory.Sequence(lambda n: f"some-job-id-{n}")
    status = Status.processing
