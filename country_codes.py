import csv

# Open CSV file
with open('country_codes_redis.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    
    with open('bulk_data.txt', 'w', encoding='utf-8') as outfile:
        for row in reader:
            # Example format: HMSET user:1 name "John" age 30
            redis_command = f'{row["command"].strip()} "{row["key"].strip()}" {row["country"].strip()}\n'
            outfile.write(redis_command)

print("CSV converted to Redis commands in bulk_data.txt")
