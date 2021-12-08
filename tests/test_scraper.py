from lol_matches.scraper import MatchScraper

region = 'europe'
match_id = 5053413844


def test_scraper():
    scraper = MatchScraper(region)
    match = scraper.get_match(match_id)

    assert isinstance(match, dict)


def test_match_parser():
    scraper = MatchScraper(region)
    match = scraper.get_match(match_id)
    parsed = MatchScraper.parse_match_info(match)

    assert isinstance(parsed, dict)


def test_team_parser():
    scraper = MatchScraper(region)
    match = scraper.get_match(match_id)
    parsed = MatchScraper.parse_teams(match)

    assert isinstance(parsed, list)


def test_participant_parser():
    scraper = MatchScraper(region)
    match = scraper.get_match(match_id)
    parsed = MatchScraper.parse_participants(match)

    assert isinstance(parsed, list)
