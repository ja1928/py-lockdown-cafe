import datetime

from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

        if friend["vaccine"]["expiration_date"] < datetime.date.today():
            return "All friends should be vaccinated"

    for friend in friends:
        if friend["wearing_a_mask"] is False:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
