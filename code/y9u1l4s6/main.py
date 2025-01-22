from mitdb_data import load, plot
heartbeat_data = load(1000)
plot(heartbeat_data, 'heartbeats.png')
previous = -1.0
for value in heartbeat_data:
  if value > 0:
    if previous < 0:
      print("heartbeat detected")
  previous = value