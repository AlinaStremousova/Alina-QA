import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('alinastre')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 43
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('alinastr_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_with_single_char_be_found(github_api):
    r = github_api.search_repo('a')
    assert r['total_count'] != 0

@pytest.mark.api
def test_emoji_exists(github_api):
    emoji = github_api.get_emojis('cat')
    assert emoji['login'] == 'cat'

@pytest.mark.api
def test_emoji_not_exists(github_api):
    emoji = github_api.get_emojis('russiaisaterroriststate')
    assert emoji['message'] == 'Not Found'


@pytest.mark.api
def test_commit_message_in_commit_request(github_api):
    commits = github_api.get_commit('AlinaStremousova', 'Alina-QA')
    print(commits)
    assert any(commit['sha'] == "ebd4efc8e23bf447ddee43e1ba4e34a7761bd1e7" for commit in commits), "Commit with specified SHA not found!"
