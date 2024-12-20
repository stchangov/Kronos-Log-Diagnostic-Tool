import re
from datetime import datetime
import sys

def mark_begin(start_line, start_time, input_file, output_f):
    output_f.write("Device Boot Report\n")
    output_f.write(f"{start_line}({input_file}): {start_time} Boot Start\n")

def mark_end(end_line, end_time, input_file, output_f, start_time):
    output_f.write(f"{end_line}({input_file}): {end_time} Boot Completed\n")
    
    start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    elapsed_time = int((end_dt - start_dt).total_seconds() * 1000)  # Convert to ms

    output_f.write(f"\tBoot Time: {elapsed_time}ms\n\n")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python ps7.py <log_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    timestamp_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")

    startup_message = "(log.c.166) server started"
    end_message = "oejs.AbstractConnector:Started SelectChannelConnector@0.0.0.0:9080"

    output_file = input_file.replace(".log", ".log.rpt")

    seq_incomplete = False

    with open(input_file, "r") as input_f, open(output_file, "w") as output_f:
        for line_number, line in enumerate(input_f, start = 1):  # Line starts at 1
            if startup_message in line:  # Start message found
                match = timestamp_pattern.search(line)
                if match:
                    current_time = match.group()
                    if not seq_incomplete:
                        # First start message
                        start_line = line_number
                        start_time = current_time
                        seq_incomplete = True
                        mark_begin(start_line, start_time, input_file, output_f)
                    else:
                        # Second start message found before an end message
                        output_f.write("**** Incomplete boot ****\n\n")
                        # Reset
                        start_line = line_number
                        start_time = current_time
                        mark_begin(start_line, start_time, input_file, output_f)
            elif end_message in line and seq_incomplete:  # End message found
                match = timestamp_pattern.search(line)
                if match:
                    end_line = line_number
                    end_time = match.group()
                    mark_end(end_line, end_time, input_file, output_f, start_time)
                    seq_incomplete = False

        # End of file
        if seq_incomplete:
            output_f.write("**** Incomplete boot ****\n\n")