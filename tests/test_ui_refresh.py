from pathlib import Path


def test_signup_refreshes_activity_list_and_clears_select_options():
    app_js = Path("src/static/app.js").read_text()

    assert "await fetchActivities();" in app_js
    assert "activitySelect.innerHTML = '<option value=\"\">-- Select an activity --</option>'" in app_js
