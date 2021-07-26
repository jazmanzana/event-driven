import requests
import time


class TestFlow:
    # This test requires the 4 containers to be running
    def test_happy_path(self):
        my_object_id = "some-object-id"
        data = {"id": my_object_id}
        headers = {"Content-Type": "application/json"}
        res = requests.post(
            "http://0.0.0.0:8000/jobs/process", headers=headers, json=data
        )
        result = res.json()["result"]
        assert result["object_id"] == my_object_id

        my_job_id = result["id"]
        res = requests.get(f"http://0.0.0.0:8000/jobs/{my_job_id}")
        result = res.json()["result"]
        assert result["object_id"] == my_object_id
        assert result["id"] == my_job_id
        assert result["status"] == "processing"

        time.sleep(20)
        res = requests.get(f"http://0.0.0.0:8000/jobs/{my_job_id}")
        result = res.json()["result"]
        assert result["object_id"] == my_object_id
        assert result["id"] == my_job_id
        assert result["status"] == "done"
