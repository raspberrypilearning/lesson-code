from mitdb_data import load, plot
mins = 15
heartbeat_data = load(mins*60*360)
plot(heartbeat_data, 'heartbeats.png')
count = 0
previous = -1.0
for value in heartbeat_data:
  if value > 0 and previous < 0:
      count = count + 1
  previous = value
print(count, "heartbeats detected")
print("average heart rate is", count/mins)