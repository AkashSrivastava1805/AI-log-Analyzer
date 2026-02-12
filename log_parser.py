def parse_log_file(file):
    content = file.read().decode("utf-8")
    lines = content.split("\n")

    error_lines = [line for line in lines if "ERROR" in line]
    warning_lines = [line for line in lines if "WARNING" in line]

    summary = f"""
Total Lines: {len(lines)}
Total ERROR: {len(error_lines)}
Total WARNING: {len(warning_lines)}
"""

    structured_data = f"""
Log Summary:
{summary}

Error Logs:
{chr(10).join(error_lines)}

Warning Logs:
{chr(10).join(warning_lines)}
"""

    return structured_data, summary
