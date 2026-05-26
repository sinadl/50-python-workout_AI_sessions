def logfile_rep(filename):
    result = []
    with open(f'/Users/sina/Desktop/mentoring_data/50-python-workout_AI_sessions/6/{filename}','r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word == '404':
                    result.append(words[0])
    return(result)

print(logfile_rep('apache_log_file.log'))