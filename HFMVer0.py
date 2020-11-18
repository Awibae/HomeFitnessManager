import random
import sys

bodyweight_quad_workouts = ["Quads Stretch", "Squat", "Forward Lunge", "Jump Squat", "Bulgarian Split\
 Squat", "Side Lunge"]
weight_quad_workouts = ["Squat", "Goblet Squat", "Forward Lunge", "Step Ups", "Lateral Lunge", "Reverse Lunge", "Heels\
 Up Goblet Squat"]
bodyweight_hamstrings_workouts = ["Hamstrings Stretch", "Single Legged Romanian Deadlift", "Kickbacks", "Nordic\
 Hamstring Curl", "Good Morning"]
weight_hamstrings_workouts = ["Squat", "Stiff Leg Deadlift", "Staggered Deadlift", "Kettlebell Swing", "Single\
 Leg Deadlift", "Deadlift"]
bodyweight_calf_workouts = ["Calves Stretch", "Walking Calf Raise", "Tip Toe Walking", "Calf Raise"]
weight_calf_workouts = ["Calf Raise", "Single Leg Calf Raise", "Seated Calf Raise"]
bodyweight_glute_workouts = ["Glutes Stretch", "Squat", "Glute Bridge", "Forward Lunges", "Good Morning", "Jump\
 Squat", "Side Lunge", "Single Leg Glute Bridge"]
weight_glute_workouts = ["Squat", "Barbell Hip Thrust", "Hip Thrust", "Glute Bridge", "Single Leg Glute\
 Bridge", "Single Leg Hip Thrust"]

user_name = input("Please enter your name: ")
answer1 = input("Hello, " + user_name + ", would you like to do a leg workout today?(Yes/No): ")
if answer1 == "Yes" or answer1 == "yes":
    answer2: str = input("Great! Do you have access to weights?(Yes/No): ")
else:
    print("I'm afraid leg workouts are the only thing coded into this project so far. Sorry")
    input("Press enter to exit") and sys.exit()

if answer2 == "No" or answer2 == "no":
    print("Don't worry! That's fine! Here are some workouts for each lower muscle group that don't require weights:")
    print(random.choice(bodyweight_quad_workouts) + " for quads, " + random.choice(bodyweight_hamstrings_workouts)
          + " for hamstrings, " + random.choice(bodyweight_calf_workouts) + " for calves, and finally "
          + random.choice(bodyweight_glute_workouts) + " for glutes! Now go and get that burn on, " + user_name + "!")

if answer2 == "Yes" or answer2 == "yes":
    print("Great! Here are some workouts for each lower muscle group that require weights:")
    print(random.choice(weight_quad_workouts) + " for quads, " + random.choice(weight_hamstrings_workouts)
          + " for hamstrings, " + random.choice(weight_calf_workouts) + " for calves, and finally "
          + random.choice(weight_glute_workouts) + " for glutes! Now go and get that burn on, " + user_name + "!")
input("Press enter to exit.")
