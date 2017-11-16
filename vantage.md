# Vantage Points

## Questions

5.1. Due to the need to repeat the name of a key in the JSON format whenever one of its values needs to be stored, since it stores data in key/value
pairs, the JSON format may create files of much larger sizes than the CSV format, in which the name of each key appears only once, does. Thus, it may take longer to parse
a JSON file than it would for a CSV file, thus hindering performance.

5.2. The CSV format is unable to distinguish between text and numeric values and is unable to handle null values. The JSON format, however, is able to
do both of those things.

5.3. https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NFLX&interval=1min&apikey=NAJXWIA8D6VN6A3K&datatype=csv

5.4. The TIME_SERIES_INTRADAY API’s JSON format is storing prices and the volume as text values, rather than numeric types of values. Since text
values typically take up more storage space than numeric values, the JSON format in this case is guilty of using more storage space
than it needs to, which would hinder efficiency.

## Debrief

a. https://blog.datafiniti.co/4-reasons-you-should-use-json-instead-of-csv-2cac362f1943, https://www.alphavantage.co/documentation/#intraday,
https://www.reddit.com/r/golang/comments/46leew/csv_vs_json_which_is_better_to_read_data_from/#bottom-comments,


b. 120 minutes
