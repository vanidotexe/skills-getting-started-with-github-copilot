from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "remove-me@mergington.edu"
    activity_name = "Chess Club"

    signup_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    assert email not in activities_response.json()[activity_name]["participants"]
