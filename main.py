import speedtest
#Creating a new speed test
speed_test = speedtest.Speedtest()
#Taking the best server
speed_test.get_best_server()
#Results ping,download, upload
print(f"Your ping is: {speed_test.results.ping} ms")

print(f"Your download speed: {round(speed_test.download() / 1000 / 1000, 1)} Mbit/s")

print(f"Your upload speed: {round(speed_test.upload() / 1000 / 1000, 1)} Mbit/s")