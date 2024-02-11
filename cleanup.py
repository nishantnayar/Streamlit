from utils import logger, cleanup_logs, shutdown, header

header("starting cleanup process")

# Close the logger at the end
shutdown()

# Use the script at the end of your program:
cleanup_logs()

print("All programs finished and log files cleaned up.")