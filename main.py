import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        # Guild
        guild = None

        if player_data["guild"] is not None:
            guild_data = player_data["guild"]

            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data["description"]
                }
            )

        # Race
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data["description"]
            }
        )

        # Skill
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                }
            )

        # Player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
