import pandas as pd
import random
from datetime import datetime, timedelta

def expand_airline_data(target_count=100):
    # Route configuration based on your provided data
    route_configs = [
        {"to": "CGP", "dur": 0.83, "ac": "A320", "cost": 300},
        {"to": "CXB", "dur": 1.00, "ac": "A320", "cost": 360},
        {"to": "ZYL", "dur": 0.75, "ac": "ATR72", "cost": 220},
        {"to": "JSR", "dur": 0.83, "ac": "ATR72", "cost": 240},
        {"to": "SPD", "dur": 1.00, "ac": "ATR72", "cost": 250},
        {"to": "RJH", "dur": 1.00, "ac": "A320", "cost": 280},
        {"to": "BZL", "dur": 1.00, "ac": "A320", "cost": 320}
    ]
    
    data = []
    current_time = datetime.strptime("06:00", "%H:%M")
    
    for i in range(1, target_count + 1, 2):
        # Pick a random route configuration
        config = random.choice(route_configs)
        
        # --- OUTBOUND FLIGHT (DAC to City) ---
        f_out_id = f"F{i:02d}"
        # Randomize departure slightly to spread the schedule
        dep_out = current_time + timedelta(minutes=random.randint(0, 120))
        arr_out = dep_out + timedelta(hours=config["dur"])
        
        # Night flag logic (if dep or arr is between 22:00 and 06:00)
        is_night_out = 1 if (dep_out.hour >= 22 or dep_out.hour < 6 or arr_out.hour >= 22 or arr_out.hour < 6) else 0
        
        data.append({
            "FlightID": f_out_id, "From": "DAC", "To": config["to"],
            "DepTime": dep_out.strftime("%H:%M"), "ArrTime": arr_out.strftime("%H:%M"),
            "Duration": config["dur"], "Aircraft": config["ac"], "Base": "DAC",
            "FlightCost": config["cost"], "Night": is_night_out
        })
        
        # --- RETURN FLIGHT (City to DAC) ---
        if i + 1 <= target_count:
            f_ret_id = f"F{i+1:02d}"
            # 50-90 minute turnaround time
            dep_ret = arr_out + timedelta(minutes=random.randint(50, 90))
            arr_ret = dep_ret + timedelta(hours=config["dur"])
            
            is_night_ret = 1 if (dep_ret.hour >= 22 or dep_ret.hour < 6 or arr_ret.hour >= 22 or arr_ret.hour < 6) else 0
            
            data.append({
                "FlightID": f_ret_id, "From": config["to"], "To": "DAC",
                "DepTime": dep_ret.strftime("%H:%M"), "ArrTime": arr_ret.strftime("%H:%M"),
                "Duration": config["dur"], "Aircraft": config["ac"], "Base": "DAC",
                "FlightCost": config["cost"], "Night": is_night_ret
            })
        
        # Increment base time for the next set of flights
        current_time += timedelta(minutes=30)
        if current_time.hour >= 23: # Reset to early morning if we run out of day
            current_time = datetime.strptime("01:00", "%H:%M")

    return pd.DataFrame(data)

# Generate 100 flights
df_expanded = expand_airline_data(100)

# Save and Preview
df_expanded.to_csv("expanded_airline_crew_data.csv", index=False)
print(df_expanded.head(10))
print(f"\nTotal flights generated: {len(df_expanded)}")
