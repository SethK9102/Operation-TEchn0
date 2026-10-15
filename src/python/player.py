from entities import Character


class Player(Character):
    def __init__(self, class):
        match class:
            case "Warrior":
                None
            case "White Mage":
                None
            case "Rogue":
                None
            case "Black Mage":
                None
            case "Monk":
                None
            default:
                raise ValueError(f"Invalid class: {class}")
        