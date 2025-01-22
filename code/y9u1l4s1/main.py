from mitdb_data import load, plot
heartbeat_data = load(100)
plot(heartbeat_data, 'heartbeats.png')