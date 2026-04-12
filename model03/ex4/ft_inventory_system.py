import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    seen_items: set[str] = set()
    order_of_appearance: list[str] = []

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name, quantity_str = parts

        if item_name in seen_items:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
            seen_items.add(item_name)
            order_of_appearance.append(item_name)
        except ValueError:
            msg = (
                f"Quantity error for '{item_name}': "
                f"invalid literal for int() with base 10: '{quantity_str}'"
            )
            print(msg)

    if not inventory:
        return

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    # Percentages
    for item, quantity in inventory.items():
        percentage = (quantity / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    # Most abundant (first in case of tie)
    most_abundant = order_of_appearance[0]
    for item in order_of_appearance:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item

    # Least abundant (first in case of tie)
    least_abundant = order_of_appearance[0]
    for item in order_of_appearance:
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}"
    )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}"
    )

    # Add new item
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
