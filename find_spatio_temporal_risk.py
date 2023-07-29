


robot_plan =  [2050, 2124, 2198, 2271, 2345, 2345]
distance_vector = [10.38, 10.2, 10.02, 9.75, 9.58, 9.58]

def find_spatio_temporal_risk (distance_vector, safe_threshold =3, human_traj = robot_plan):
    is_risk_detected = False
    risk_index_wrt_human = 0
    for i in range (len(distance_vector)):
        if (distance_vector[i] < safe_threshold):
            is_risk_detected = True
            risk_index_wrt_human = human_traj[i]
            break
    
    return is_risk_detected, risk_index_wrt_human


if __name__ == "__main__":
    robot_plan =  [2050, 2124, 2198, 2271, 2345, 2345]
    distance_vector = [10.38, 10.2, 10.02, 9.75, 9.58, 9.58]

    print ("robot_plan:", robot_plan)
    safe_path = fi
    