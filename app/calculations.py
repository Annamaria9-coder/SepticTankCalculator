# calculations.py
from app.constants import SLUDGE_ACCUMULATION_RATE, FLUSH_COUNT, CISTERN_SIZE, LIQUID_DEPTH, FREEBOARD


def calculate_volume_liquid(household_size):
    return FLUSH_COUNT * CISTERN_SIZE * household_size

def calculate_volume_sludge(household_size):
    return SLUDGE_ACCUMULATION_RATE * household_size

def calculate_total_volume(volume_liquid, volume_sludge):
    return volume_liquid + volume_sludge
