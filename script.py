import subprocess

log = subprocess.check_output(
    ["git", "log", "--pretty=format:%s"]
).decode().split("\n")

total_commits = 0
total_changes = 0
total_dmm = 0

for line in log:
    line = line.strip()
    if not line:
        continue

    total_commits += 1

    # metrics per commit
    unit_size = 0
    complexity = 0
    interfacing = 0

    if "Updates" in line:
        unit_size += 1
        complexity += 1

    if "dependency-name" in line:
        interfacing += 1

    changes = unit_size + complexity + interfacing

    total_changes += changes

    dmm = (unit_size + complexity + interfacing) / 3
    total_dmm += dmm

avg_files_changed = total_changes / total_commits if total_commits else 0
avg_dmm = total_dmm / total_commits if total_commits else 0

print("Total commits analyzed:", total_commits)
print("Avg files changed:", avg_files_changed)
print("Avg DMM metrics:", avg_dmm)