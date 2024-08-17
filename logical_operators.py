traveler_profile = {
    "passport":True,
    "tickets":True,
}

if traveler_profile['passport'] and traveler_profile["tickets"]:
    print("You are ready for the initial phase of travel preparation.")
else:
    print("Please snsure you have both your passport and tickets.")