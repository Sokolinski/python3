# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jp <jp@student.42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/02 12:58:44 by jp                #+#    #+#              #
#    Updated: 2026/03/02 15:11:57 by jp               ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None: 
    if seed_type.lower() == "tomato" and unit.lower == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif seed_type.lower() == "carrot" and unit.lower == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif seed_type.lower() == "lettuce" and unit.lower() == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} quare meters")
    else:
        print("Unknown unit type")

ft_seed_inventory("Tomato", 15, "packets")