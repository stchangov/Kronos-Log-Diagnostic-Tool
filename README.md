# Kronos Log Diagnostic Tool

A Python utility that parses Kronos server logs to track boot sequences, calculate boot times, and generate easy-to-read reports, while flagging incomplete boots.  

## Features

- Detects boot start and end events automatically  
- Calculates boot durations with millisecond precision  
- Flags incomplete boot sequences  
- Generates structured output reports  

## Requirements

- Python 3.7 or higher  

## Usage

Run the script with:  

```bash
python ps7.py <log_file>
```

- `<log_file>` is the path to the Kronos log file you want to analyze.  
- The tool will create a report file in the same directory with the `.log.rpt` extension.  

## Example Output

```text
Device Boot Report
23(log.c.166): 2025-09-06 08:12:05 Boot Start
42(log.c.200): 2025-09-06 08:12:12 Boot Completed
    Boot Time: 7000ms
```

## Notes

- Multiple boot sequences in a single log are handled one after the other.  
- Incomplete boot sequences are clearly flagged in the report.  

## License

MIT License © 2024 Stephan Tchangov
